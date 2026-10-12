# GRAD-302 · POST /bill-payments — Kommunal ödəniş etmək

Epic: EPIC-3 · Prioritet: Highest · Story point: 8
Hər ssenari yeni sandbox-da, 1000 (və ya lazım olan) AZN-lik yeni kartla başlayır — balans və
gündəlik limit hesablamaları başqa ssenarilərdən asılı deyil, nəticələr deterministikdir.
Sərhəd dəyərləri data-driven fayllardadır: grad302_amount_range.spec, grad302_fee_calculation.spec,
grad302_idempotency_key.spec.
TC-API-302-019/020 (perTransaction 300) manual qalır: hansı təchizatçı ilə 300 AZN-ə çatılacağı
backlog-da göstərilməyib (grooming №12).

tags: api, grad-302, payments

## TC-API-302-001 Etibarlı ödəniş
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "payId" olaraq yadda saxla
* Header "Location" deyerinde "/bill-payments/${payId}" olmalıdır
* Json cavabını cedvel ile yoxla

   |path         |value        |
   |-------------|-------------|
   |id           |@regex:^bpm_[a-z0-9]+$|
   |status       |SUCCESS      |
   |biller.id    |citynet      |
   |biller.name  |CityNet      |
   |subscriberNo |CN123456     |
   |amount       |50           |
   |fee          |0.5          |
   |total        |50.5         |
   |currency     |AZN          |
   |cardId       |${cardId}    |
   |balanceAfter |949.5        |
   |createdAt    |@notEmpty    |

* Cavab "bill-payment.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-302-002 Ödənişdən sonra kartın balansı və spentToday
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "50"
* Kart "${cardId}" məlumatını al
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "949.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC-API-302-003 Qəbz nömrəsinin formatı və ardıcıllığı
tags: regression, positive, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "10"
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000001$" regex-ine uyğun olmalıdır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "10"
* Json cavabında "receiptNo" deyeri "^RCP-[0-9]{8}-000002$" regex-ine uyğun olmalıdır

## TC-API-302-004 Eyni açar + eyni body təkrar göndərilir — pul ikinci dəfə çıxmır
tags: regression, positive, AC-4

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "firstPayId" olaraq yadda saxla
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "firstPayId" ile eynidir
* Header "Idempotent-Replay" deyerinde "true" olmalıdır
* Kart "${cardId}" məlumatını al
* Json cavabında "availableBalance" deyeri "949.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC-API-302-005 Eyni açar + fərqli məbləğ
tags: regression, negative, AC-5

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "201" olmalıdır
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "60"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_CONFLICT" beraberdir

## TC-API-302-006 Idempotency-Key header yoxdur
tags: regression, negative, AC-6

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"cardId\":\"${cardId}\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}" metnini elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir

## TC-API-302-011 Azercell-ə Bakcell nömrəsi
tags: regression, negative, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "azercell" "551234567" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

## TC-API-302-012 CityNet formatına uyğun olmayan abunəçi (CN + 5 rəqəm)
tags: regression, negative, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN12345" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

## TC-API-302-021 Gündəlik limit dolub (500) — növbəti ödəniş rədd edilir
tags: regression, boundary, AC-12

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100001" "150"
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100002" "150"
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100003" "150"
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100004" "45.05"
* Json cavabında "total" deyeri "45.5" beraberdir
* Kart "${cardId}" məlumatını al
* Json cavabında "spentToday" deyeri "500" beraberdir
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN100005" "5"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "0" beraberdir

## TC-API-302-022 Balansdan 0.01 artıq ödəniş (49.51 > 49.50)
tags: regression, boundary, AC-13

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "50"
* Json cavabında "balanceAfter" deyeri "49.5" beraberdir
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "49.02"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC-API-302-023 Balansa bərabər ödəniş (49.50) — balanceAfter 0
tags: regression, boundary, AC-13

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "50"
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "49.01"
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "49.5" beraberdir
* Json cavabında "balanceAfter" deyeri "0" beraberdir

## TC-API-302-024 FROZEN kartla ödəniş
tags: regression, negative, AC-14

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC-API-302-025 USD kartla ödəniş
tags: regression, negative, AC-14

* User2 yeni sandbox ilə daxil olur
* "u1Token" deyişenine "${u2Token}" deyerini ver
* Kart buraxma sorğusu göndər "acc_003" "100" "USD kart"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "usdCardId" olaraq yadda saxla
* Ödəniş sorğusu göndər "${usdCardId}" "citynet" "CN123456" "50"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CURRENCY_NOT_SUPPORTED" beraberdir

## TC-API-302-026 amount mətn kimi ("10")
tags: regression, negative, AC-15

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "\"10\""
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC-API-302-027 amount 3 onluq, 0 və mənfi
tags: regression, negative

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10.555"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "amount" olmalıdır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "0"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "amount" olmalıdır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "-5"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC-API-302-028 Mövcud olmayan təchizatçı
tags: regression, negative

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "unknown" "CN123456" "10"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "BILLER_NOT_FOUND" beraberdir

## TC-API-302-029 Başqa istifadəçinin kartı ilə ödəniş
tags: regression, security

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "u1Original" deyişenine "${u1Token}" deyerini ver
* User2 ortaq sandbox ilə daxil olur
* "u1Token" deyişenine "${u2Token}" deyerini ver
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir
* "u1Token" deyişenine "${u1Original}" deyerini ver
* Kart "${cardId}" məlumatını al
* Json cavabında "availableBalance" deyeri "100" beraberdir

## TC-API-302-030 Uğursuz sorğu açarı "istifadə etmir"
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN12" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* "${idemKey}" açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir

## TC-API-302-031 Yoxlama ardıcıllığı: açar yoxdur + səhv body
tags: regression, decision-table

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"cardId\":\"vcd_zzzzzzzz\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":\"abc\"}" metnini elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir

## TC-API-302-032 Yoxlama ardıcıllığı: səhv abunəçi + mövcud olmayan kart
tags: regression, decision-table

* User1 ortaq sandbox ilə daxil olur
* Ödəniş sorğusu göndər "vcd_zzzzzzzz" "citynet" "CN1" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

## TC-API-302-033 Yoxlama ardıcıllığı: FROZEN kart + balansdan böyük məbləğ
tags: regression, decision-table

* User1 yeni sandbox ilə daxil olur
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "50"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC-API-302-035 Token olmadan ödəniş
tags: regression, security

* Tokensiz yeni sorğu hazırla
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "{\"cardId\":\"vcd_zzzzzzzz\",\"billerId\":\"citynet\",\"subscriberNo\":\"CN123456\",\"amount\":50}" metnini elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

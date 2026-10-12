# GRAD-303 · GET /bill-payments — Ödəniş tarixçəsi: filtr və səhifələmə

Epic: EPIC-3 · Prioritet: Medium · Story point: 5
Səhifələmə ssenariləri yeni sandbox-da 18 ödəniş (citynet 12 + azercell 6) yaradır — nəticələr
deterministikdir. Validasiya ssenariləri data yaratmır, ortaq sandbox-da işləyir.
QEYD: from/to Bakı vaxtı ilə işləyir; ${today} test maşınının tarixidir — testləri Bakı vaxt qurşağında işə salın.

tags: api, grad-303, payments

## TC-API-303-001 Parametrsiz tarixçə: page 1, limit 10, ən yeni birinci
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100001" "5"
* Uğurlu ödəniş edilir "${cardId}" "azercell" "501234567" "5"
* Json cavabında "id" deyerini "lastPayId" olaraq yadda saxla
* Ödəniş tarixçəsini al "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path        |value|
   |------------|-----|
   |page        |1    |
   |limit       |10   |
   |total       |2    |
   |items[0].id |${lastPayId}|
   |items[0].billerId|azercell|

* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır
* Cavab "bill-payment-list.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-303-002 18 ödəniş, limit 10 — 2-ci səhifədə 8 element
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Tarixçə üçün 18 ödəniş hazırla "${cardId}"
* Ödəniş tarixçəsini al "/bill-payments?page=2&limit=10"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "8" olmalıdır
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "page" deyeri "2" beraberdir

## TC-API-303-003 Mövcud olmayan səhifə — boş siyahı, xəta yoxdur
tags: regression, positive, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Tarixçə üçün 18 ödəniş hazırla "${cardId}"
* Ödəniş tarixçəsini al "/bill-payments?page=3"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
* Json cavabında "total" deyeri "18" beraberdir

## TC-API-303-004 limit 0 və 51 (sərhəddən kənar)
tags: regression, boundary, AC-4

* User1 ortaq sandbox ilə daxil olur
* Ödəniş tarixçəsini al "/bill-payments?limit=0"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "limit" olmalıdır
* Ödəniş tarixçəsini al "/bill-payments?limit=51"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "limit" olmalıdır

## TC-API-303-005 limit 1 və 50 (sərhədlər)
tags: regression, boundary, AC-4

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Tarixçə üçün 18 ödəniş hazırla "${cardId}"
* Ödəniş tarixçəsini al "/bill-payments?limit=1"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "totalPages" deyeri "18" beraberdir
* Ödəniş tarixçəsini al "/bill-payments?limit=50"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "18" olmalıdır
* Json cavabında "totalPages" deyeri "1" beraberdir

## TC-API-303-006 Səhv page dəyərləri (0, -1, abc)
tags: regression, negative, AC-4

* User1 ortaq sandbox ilə daxil olur
* Ödəniş tarixçəsini al "/bill-payments?page=0"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "page" olmalıdır
* Ödəniş tarixçəsini al "/bill-payments?page=-1"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "page" olmalıdır
* Ödəniş tarixçəsini al "/bill-payments?page=abc"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "page" olmalıdır

## TC-API-303-007 Mövcud olmayan tarix (2026-13-01)
tags: regression, negative, AC-5

* User1 ortaq sandbox ilə daxil olur
* Ödəniş tarixçəsini al "/bill-payments?from=2026-13-01"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-API-303-008 from > to
tags: regression, negative, AC-6

* User1 ortaq sandbox ilə daxil olur
* Ödəniş tarixçəsini al "/bill-payments?from=2026-10-10&to=2026-10-01"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-API-303-009 from = to = bu gün — günün bütün ödənişləri (sərhəd daxildir)
tags: regression, boundary, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100001" "5"
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN100002" "5"
* Ödəniş tarixçəsini al "/bill-payments?from=${today}&to=${today}"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir

## TC-API-303-010 Təchizatçı filtri — total filtrdən sonrakı ümumi saydır
tags: regression, positive, AC-8

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Tarixçə üçün 18 ödəniş hazırla "${cardId}"
* Ödəniş tarixçəsini al "/bill-payments?billerId=citynet"
* Status kodunun "200" olmalıdır
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır
* Json cavabında "total" deyeri "12" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır

## TC-API-303-011 Kart filtri
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "card1" olaraq saxlanılır
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "card2" olaraq saxlanılır
* Uğurlu ödəniş edilir "${card1}" "citynet" "CN100001" "5"
* Uğurlu ödəniş edilir "${card2}" "citynet" "CN100002" "5"
* Json cavabında "id" deyerini "card2PayId" olaraq yadda saxla
* Ödəniş tarixçəsini al "/bill-payments?cardId=${card2}"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].id" deyeri "${card2PayId}" beraberdir

## TC-API-303-012 Filtr + səhifələmə birlikdə
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Tarixçə üçün 18 ödəniş hazırla "${cardId}"
* Ödəniş tarixçəsini al "/bill-payments?billerId=citynet&limit=5&page=3"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "total" deyeri "12" beraberdir
* Json cavabında "totalPages" deyeri "3" beraberdir

## TC-API-303-015 Token olmadan tarixçə
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

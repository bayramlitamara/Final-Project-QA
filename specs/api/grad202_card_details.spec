# GRAD-202 · GET /cards/{id} — Kart məlumatına baxmaq

Epic: EPIC-2 · Prioritet: Medium · Story point: 2
TC-API-202-005 (spentToday-in 00:00-da sıfırlanması) manual qalır — gecə yarısını gözləmək tələb edir.

tags: api, grad-202, cards

## TC-API-202-001 Yeni kartın məlumatları POST cavabı ilə eynidir
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_002" "100" "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Json cavabında "maskedPan" deyerini "postPan" olaraq yadda saxla
* Json cavabında "expiry" deyerini "postExpiry" olaraq yadda saxla
* Json cavabında "createdAt" deyerini "postCreatedAt" olaraq yadda saxla
* Kart "${cardId}" məlumatını al
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "cardId" ile eynidir
* Json cavabında "maskedPan" deyeri "postPan" ile eynidir
* Json cavabında "expiry" deyeri "postExpiry" ile eynidir
* Json cavabında "createdAt" deyeri "postCreatedAt" ile eynidir
* Json cavabını cedvel ile yoxla

   |path                 |value   |
   |---------------------|--------|
   |status               |ACTIVE  |
   |availableBalance     |100     |
   |spentToday           |0       |
   |label                |Kommunal|
   |limits.dailyOnline   |500     |
   |limits.perTransaction|300     |

* Cavab "card.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-202-002 50.50 AZN ödənişdən sonra balans və spentToday yenilənir
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Uğurlu ödəniş edilir "${cardId}" "citynet" "CN123456" "50"
* Json cavabında "total" deyeri "50.5" beraberdir
* Kart "${cardId}" məlumatını al
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "949.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC-API-202-003 Başqa istifadəçinin kartına baxış
tags: regression, security, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* User2 ortaq sandbox ilə daxil olur
* "${u2Token}" tokeni ilə yeni sorğu hazırla
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-202-004 Mövcud olmayan kart
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* Kart "vcd_zzzzzzzz" məlumatını al
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-202-006 Token olmadan kart məlumatı
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "GET" sorğusu gönder "/cards/vcd_zzzzzzzz"
* Status kodunun "401" olmalıdır

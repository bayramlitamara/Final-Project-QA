# GRAD-201 · POST /cards — Virtual kart buraxmaq

Epic: EPIC-2 Virtual kartlar · Prioritet: High · Story point: 5
Kart limiti (3 ACTIVE/FROZEN) ssenarilər arasında toqquşmasın deyə kart yaradan hər ssenari yeni sandbox-da başlayır.
initialAmount sərhəd dəyərləri data-driven olaraq grad201_amount_validation.spec faylındadır.
QEYD (grooming №1): AC-5 başqasının hesabı üçün 403 gözləyir, ümumi qayda isə 404 deyir. Test AC-yə uyğun yazılıb.

tags: api, grad-201, cards

## TC-API-201-001 Etibarlı sorğu ilə kart buraxılması
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_002" "100" "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Header "Location" deyerinde "/cards/${cardId}" olmalıdır
* Json cavabını cedvel ile yoxla

   |path                 |value     |
   |---------------------|----------|
   |id                   |@regex:^vcd_[a-z0-9]+$|
   |accountId            |acc_002   |
   |label                |Kommunal  |
   |currency             |AZN       |
   |status               |ACTIVE    |
   |availableBalance     |100       |
   |limits.dailyOnline   |500       |
   |limits.perTransaction|300       |
   |spentToday           |0         |
   |blockReason          |null      |
   |blockedAt            |null      |
   |createdAt            |@notEmpty |

* Cavab "card.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-201-002 maskedPan və expiry formatı
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_002" "100" "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri "^4169 73[*]{2} [*]{4} [0-9]{4}$" regex-ine uyğun olmalıdır
* Json cavabında "expiry" deyeri "^(0[1-9]|1[0-2])/[0-9]{2}$" regex-ine uyğun olmalıdır
* Json cavabında "expiry" deyeri "^.*/29$" regex-ine uyğun olmalıdır

## TC-API-201-011 Başqa istifadəçinin hesabı ilə kart (AC-5: 403 FORBIDDEN)
tags: regression, security, AC-5

* User1 ortaq sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_003" "100" "Test"
* Status kodunun "403" olmalıdır
* Json cavabında "code" deyeri "FORBIDDEN" beraberdir

## TC-API-201-012 Mövcud olmayan hesab
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_999" "100" "Test"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "ACCOUNT_NOT_FOUND" beraberdir

## TC-API-201-013 user2 balansdan artıq məbləğ yükləyir (891 > 890.50)
tags: regression, boundary, AC-6

* User2 yeni sandbox ilə daxil olur
* "u1Token" deyişenine "${u2Token}" deyerini ver
* Kart buraxma sorğusu göndər "acc_003" "891" "Test"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC-API-201-014 user2 balansa bərabər məbləğ yükləyir (890.50)
tags: regression, boundary, AC-6

* User2 yeni sandbox ilə daxil olur
* "u1Token" deyişenine "${u2Token}" deyerini ver
* Kart buraxma sorğusu göndər "acc_003" "890.50" "Test"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "availableBalance" deyeri "890.5" beraberdir

## TC-API-201-015 3 ACTIVE/FROZEN kart olduqda 4-cü kart
tags: regression, boundary, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card1" olaraq saxlanılır
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card2" olaraq saxlanılır
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card3" olaraq saxlanılır
* Kart "${card3}" "TEMPORARY" səbəbi ilə bloklanır
* Kart buraxma sorğusu göndər "acc_002" "10" "Dördüncü"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC-API-201-016 BLOCKED kart limitə sayılmır
tags: regression, state-transition, AC-8

* User1 yeni sandbox ilə daxil olur
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card1" olaraq saxlanılır
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card2" olaraq saxlanılır
* User1 üçün "10" AZN-lik aktiv kart yaradılır və id "card3" olaraq saxlanılır
* Kart "${card3}" "LOST" səbəbi ilə bloklanır
* Kart buraxma sorğusu göndər "acc_002" "10" "Dördüncü"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir

## TC-API-201-017 label — 30 simvol (sərhəd) və 31 simvol (sərhəd + 1)
tags: regression, boundary

* User1 yeni sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_002" "10" "Abcdefghijabcdefghijabcdefghij"
* Status kodunun "201" olmalıdır
* Json cavabında "label" deyeri "Abcdefghijabcdefghijabcdefghij" beraberdir
* Kart buraxma sorğusu göndər "acc_002" "10" "Abcdefghijabcdefghijabcdefghijk"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "label" olmalıdır

## TC-API-201-018 label göndərilmədikdə null
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* "cardAccount" deyişenine "acc_002" deyerini ver
* "cardAmount" deyişenine "10" deyerini ver
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "card-no-label.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "label" açarı mövcud olmalıdır
* Json cavabında "label" deyeri null olmalıdır

## TC-API-201-019 Kart yükləməsi əsas hesab balansını dəyişmir (sandbox qaydası)
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "GET" sorğusu gönder "/me/accounts"
* Status kodunun "200" olmalıdır
* Cavab body-sinde "12500" olmalıdır

## TC-API-201-020 Məcburi accountId göndərilmir
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"initialAmount\":100}" metnini elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "accountId" olmalıdır

## TC-API-201-021 Token olmadan kart buraxılması
tags: regression, security

* Tokensiz yeni sorğu hazırla
* Body olaraq "{\"accountId\":\"acc_002\",\"initialAmount\":100}" metnini elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "401" olmalıdır

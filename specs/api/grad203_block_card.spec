# GRAD-203 · POST /cards/{id}/block — Kartı bloklamaq / dondurmaq

Epic: EPIC-2 · Prioritet: High · Story point: 3
Texnika: state transition. Task qeydinə uyğun olaraq vəziyyət keçid cədvəlinin hər xanası ayrıca test case-dir:

   ACTIVE  + TEMPORARY → 200 FROZEN        (TC-API-203-001)
   ACTIVE  + LOST      → 200 BLOCKED       (TC-API-203-002)
   ACTIVE  + STOLEN    → 200 BLOCKED       (TC-API-203-003)
   FROZEN  + STOLEN    → 200 BLOCKED       (TC-API-203-004)
   FROZEN  + LOST      → 200 BLOCKED       (TC-API-203-005)
   FROZEN  + TEMPORARY → 409 ALREADY_FROZEN(TC-API-203-006)
   BLOCKED + TEMPORARY → 409 CARD_BLOCKED  (TC-API-203-007)
   BLOCKED + STOLEN    → 409 CARD_BLOCKED  (TC-API-203-008)

tags: api, grad-203, cards

## TC-API-203-001 ACTIVE + TEMPORARY → FROZEN
tags: regression, state-transition, AC-1

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T.+Z$" regex-ine uyğun olmalıdır

## TC-API-203-002 ACTIVE + LOST → BLOCKED
tags: regression, state-transition, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "LOST" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır

## TC-API-203-003 ACTIVE + STOLEN → BLOCKED
tags: regression, state-transition, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "STOLEN" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir

## TC-API-203-004 FROZEN + STOLEN → BLOCKED (eskalasiya)
tags: regression, state-transition, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" "STOLEN" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir

## TC-API-203-005 FROZEN + LOST → BLOCKED
tags: regression, state-transition, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" "LOST" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir

## TC-API-203-006 FROZEN + TEMPORARY → 409 ALREADY_FROZEN
tags: regression, state-transition, AC-4

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "ALREADY_FROZEN" beraberdir

## TC-API-203-007 BLOCKED + TEMPORARY → 409 CARD_BLOCKED
tags: regression, state-transition, AC-5

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "LOST" səbəbi ilə bloklanır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC-API-203-008 BLOCKED + STOLEN → 409 CARD_BLOCKED
tags: regression, state-transition, AC-5

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "LOST" səbəbi ilə bloklanır
* Kart "${cardId}" "STOLEN" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC-API-203-009 İcazəsiz reason dəyəri (BROKEN)
tags: regression, negative, AC-6

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "BROKEN" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC-API-203-010 reason sahəsi yoxdur ({})
tags: regression, negative, AC-6

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{}" metnini elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC-API-203-011 Body ümumiyyətlə göndərilmir
tags: regression, negative

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC-API-203-012 Mövcud olmayan kart
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* Kart "vcd_zzzzzzzz" "TEMPORARY" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-203-013 Başqa istifadəçinin kartını bloklamaq
tags: regression, security

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* User2 ortaq sandbox ilə daxil olur
* "${u2Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"reason\":\"LOST\"}" metnini elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Kart "${cardId}" məlumatını al
* Json cavabında "status" deyeri "ACTIVE" beraberdir

## TC-API-203-014 Yoxlama ardıcıllığı: mövcud olmayan kart + səhv reason
tags: regression, decision-table

* User1 ortaq sandbox ilə daxil olur
* Kart "vcd_zzzzzzzz" "BROKEN" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-API-203-015 FROZEN kartla ödəniş
tags: regression, negative, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC-API-203-016 BLOCKED kartla ödəniş
tags: regression, negative, AC-7

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "LOST" səbəbi ilə bloklanır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC-API-203-019 Token olmadan bloklama
tags: regression, security

* Tokensiz yeni sorğu hazırla
* Body olaraq "{\"reason\":\"LOST\"}" metnini elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/block"
* Status kodunun "401" olmalıdır

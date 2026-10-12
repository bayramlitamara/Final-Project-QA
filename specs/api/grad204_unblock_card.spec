# GRAD-204 · POST /cards/{id}/unblock — Dondurulmuş kartı açmaq

Epic: EPIC-2 · Prioritet: Medium · Story point: 2 · Body göndərilmir.

tags: api, grad-204, cards

## TC-API-204-001 FROZEN kartın açılması
tags: regression, state-transition, AC-1

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" üçün unblock sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır

## TC-API-204-002 ACTIVE kartın açılması
tags: regression, state-transition, AC-2

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" üçün unblock sorğusu göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NOT_FROZEN" beraberdir

## TC-API-204-003 BLOCKED kartın açılması
tags: regression, state-transition, AC-3

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "STOLEN" səbəbi ilə bloklanır
* Kart "${cardId}" üçün unblock sorğusu göndər
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir

## TC-API-204-004 Açılmış kartla ödəniş uğurlu keçir
tags: regression, positive, AC-4

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" üçün unblock sorğusu göndər
* Status kodunun "200" olmalıdır
* Ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir

## TC-API-204-005 Tam dövr: dondur → aç → yenidən dondur
tags: regression, state-transition

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* Kart "${cardId}" üçün unblock sorğusu göndər
* Status kodunun "200" olmalıdır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklama sorğusu göndər
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir

## TC-API-204-006 Mövcud olmayan kart
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* Kart "vcd_zzzzzzzz" üçün unblock sorğusu göndər
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-204-007 Başqa istifadəçinin kartını açmaq
tags: regression, security

* User1 yeni sandbox ilə daxil olur
* User1 üçün "100" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Kart "${cardId}" "TEMPORARY" səbəbi ilə bloklanır
* User2 ortaq sandbox ilə daxil olur
* "${u2Token}" tokeni ilə yeni sorğu hazırla
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Kart "${cardId}" məlumatını al
* Json cavabında "status" deyeri "FROZEN" beraberdir

## TC-API-204-009 Token olmadan açma
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/unblock"
* Status kodunun "401" olmalıdır

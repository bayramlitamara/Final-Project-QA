# GRAD-103 · DELETE /beneficiaries/{id} — Alıcını silmək

Epic: EPIC-1 · Prioritet: Medium · Story point: 2

tags: api, grad-103, beneficiaries

## TC-API-103-001 Mövcud alıcının silinməsi — 204, body boş
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır

## TC-API-103-002 Silinmiş alıcı siyahıda yoxdur, total 1 azalıb
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* Alıcı yaradılır "Elvin Həsənov" "AZ77AIIB40060019440123456780" "AZN" "Qonşu" və id "benId2" olaraq saxlanılır
* Alıcılar siyahısını al
* Json cavabında "total" deyeri "2" beraberdir
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır
* Alıcılar siyahısını al
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items.id" deyerinde "${benId2}" olmalıdır

## TC-API-103-003 Eyni alıcının ikinci dəfə silinməsi
tags: regression, negative, AC-3

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "204" olmalıdır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-103-004 user2 user1-in alıcısını silməyə çalışır — 404 (403 yox)
tags: regression, security, AC-4

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* User2 ortaq sandbox ilə daxil olur
* "${u2Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${benId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir
* Alıcılar siyahısını al
* Json cavabında "items.id" deyerinde "${benId}" olmalıdır

## TC-API-103-005 Mövcud olmayan id ilə silmə
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/ben_zzzzzzzz"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC-API-103-007 Token olmadan silmə
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/ben_zzzzzzzz"
* Status kodunun "401" olmalıdır

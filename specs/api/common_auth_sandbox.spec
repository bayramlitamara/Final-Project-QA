# Ümumi qaydalar — autentifikasiya və sandbox

Bütün endpoint-lər üçün ümumi qaydalar (backlog-un "Başlamazdan əvvəl" bölməsi).
TC-API-GEN-005 (429 rate limit) manual qalır — paylaşılan serverə yük yaradır.

tags: api, common, auth

## TC-API-GEN-001 Saxta token
tags: regression, security

* Yeni API sorğusu hazırla
* Header elave et "Authorization" = "Bearer abc.def.ghi"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

## TC-API-GEN-002 "Bearer" prefiksi olmayan token
tags: regression, security

* User1 ortaq sandbox ilə daxil olur
* Yeni API sorğusu hazırla
* Header elave et "Authorization" = "${rawToken}"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

## TC-API-GEN-003 Səhv şifrə ilə login
tags: regression, negative

* Yeni API sorğusu hazırla
* Body olaraq "login-user1-wrong-password.json" faylını elave et
* "POST" sorğusu gönder "/auth/login"
* Status kodunun "401" olmalıdır
* Json cavabında "token" açarı olmamalıdır

## TC-API-GEN-004 Sandbox izolyasiyası: yeni login boş mühit açır
tags: regression, positive

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* Alıcılar siyahısını al
* Json cavabında "total" deyeri "1" beraberdir
* User1 yeni sandbox ilə daxil olur
* Alıcılar siyahısını al
* Json cavabında "total" deyeri "0" beraberdir

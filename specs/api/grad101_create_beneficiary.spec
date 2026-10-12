# GRAD-101 · POST /beneficiaries — Yeni alıcı əlavə etmək

Epic: EPIC-1 Saxlanmış alıcılar · Prioritet: High · Story point: 5
Test case-lər: Tamara_Məlikova_API_Test_Cases.xlsx → "Test Cases" (TC-API-101-*).
Resurs yaradan ssenarilər "User1 yeni sandbox ilə daxil olur" ilə başlayır: hər ssenari öz boş mühitində
işləyir, alıcı limiti (10) və dublikat qaydaları digər ssenarilərə təsir etmir → testlər flaky olmur.
Sərhəd dəyərləri (BVA) data-driven olaraq grad101_field_validation.spec faylındadır.

tags: api, grad-101, beneficiaries

## TC-API-101-001 Etibarlı sorğu ilə alıcı yaradılması
tags: regression, positive, AC-1

* User1 yeni sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Header "Location" deyerinde "/beneficiaries/${benId}" olmalıdır
* Json cavabını cedvel ile yoxla

   |path      |value                                              |
   |----------|---------------------------------------------------|
   |id        |@regex:^ben_[a-z0-9]{8}$                           |
   |fullName  |Nigar Əliyeva                                      |
   |iban      |AZ77AIIB40060019440123456789                       |
   |ibanMasked|@regex:^AZ77 [*]{4} [*]{4} [*]{4} [*]{4} 6789$     |
   |currency  |AZN                                                |
   |nickname  |Anam                                               |
   |createdAt |@regex:^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:.]+Z$      |

* Cavab "beneficiary.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-101-002 IBAN-ın normallaşdırılması (boşluq + kiçik hərf)
tags: regression, positive, AC-2

* User1 yeni sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "Nigar Əliyeva" "az77 aiib 4006 0019 4401 2345 6789" "AZN" "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ77AIIB40060019440123456789" beraberdir
* Json cavabında "ibanMasked" deyeri "^AZ77 .*6789$" regex-ine uyğun olmalıdır

## TC-API-101-003 nickname göndərilmədikdə null qaytarılması
tags: regression, positive, AC-3

* User1 yeni sandbox ilə daxil olur
* Lәqəbsiz alıcı yaratma sorğusu göndər "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır

## TC-API-101-004 Bir neçə səhv sahə eyni anda — details-də hamısı göstərilir
tags: regression, negative, AC-4

* User1 ortaq sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "A" "XX00" "GBP" "Anam"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.findAll { it.message == null }.size()" deyeri "0" beraberdir
* Cavab "error.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-101-012 fullName trim-dən sonra 1 simvol
tags: regression, boundary, AC-5

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"fullName\":\"   A   \",\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\"}" metnini elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC-API-101-021 Eyni IBAN ikinci dəfə əlavə edilir
tags: regression, negative, AC-7

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* Alıcı yaratma sorğusu göndər "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Bacım"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC-API-101-022 Eyni IBAN fərqli formatda (boşluqlu, kiçik hərf) ikinci dəfə
tags: regression, negative, AC-2, AC-7

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* Alıcı yaratma sorğusu göndər "Nigar Əliyeva" "az77 aiib 4006 0019 4401 2345 6789" "AZN" "Bacım"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC-API-101-023 Lәqəb böyük-kiçik hərf fərqi ilə təkrarlanır
tags: regression, negative, AC-8

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "anam" və id "benId" olaraq saxlanılır
* Alıcı yaratma sorğusu göndər "Leyla Əliyeva" "AZ77AIIB40060019440123456780" "AZN" "ANAM"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NICKNAME_TAKEN" beraberdir

## TC-API-101-024 İstifadəçinin öz hesabının IBAN-ı
tags: regression, negative, AC-9

* User1 ortaq sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "Öz Hesabım" "AZ29NABZ00000000137010002855" "AZN" "Mən"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## TC-API-101-025 Başqa istifadəçinin (admin) IBAN-ı alıcı kimi qəbul edilir
tags: regression, positive, AC-9

* User1 yeni sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "Admin İstifadəçi" "AZ21NABZ00000000137010001944" "AZN" "Admin"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ21NABZ00000000137010001944" beraberdir

## TC-API-101-026 10 alıcı olduqda 11-cinin əlavə edilməsi
tags: regression, boundary, AC-10

* User1 yeni sandbox ilə daxil olur
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456780"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456781"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456782"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456783"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456784"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456785"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456786"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456787"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456788"
* Lәqəbsiz alıcı yaradılır "AZ77AIIB40060019440123456789"
* Alıcılar siyahısını al
* Json cavabında "total" deyeri "10" beraberdir
* Lәqəbsiz alıcı yaratma sorğusu göndər "Test Alici" "AZ77AIIB40060019440123456799" "AZN"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "LIMIT_REACHED" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir

## TC-API-101-027 Yoxlama ardıcıllığı: öz IBAN-ı + səhv fullName
tags: regression, decision-table

* User1 ortaq sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər "A" "AZ29NABZ00000000137010002855" "AZN" "Mən"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-API-101-028 Yoxlama ardıcıllığı: dublikat IBAN + tutulmuş lәqəb
tags: regression, decision-table

* User1 yeni sandbox ilə daxil olur
* Alıcı yaradılır "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "Anam" və id "benId" olaraq saxlanılır
* Alıcı yaratma sorğusu göndər "Nigar Əliyeva" "AZ77AIIB40060019440123456789" "AZN" "anam"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC-API-101-029 Etibarsız JSON body
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"fullName\": \"Nigar\"," metnini elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC-API-101-030 Sahə tipi səhvdir (fullName rəqəm)
tags: regression, negative

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Body olaraq "{\"fullName\":12345,\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\"}" metnini elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır

## TC-API-101-031 Token olmadan alıcı yaradılması
tags: regression, security

* Tokensiz yeni sorğu hazırla
* Body olaraq "{\"fullName\":\"Nigar Əliyeva\",\"iban\":\"AZ77AIIB40060019440123456789\",\"currency\":\"AZN\"}" metnini elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

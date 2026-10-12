# GRAD-101 · Sahə validasiyası — data-driven (BVA + ekvivalent siniflər)

Hər cədvəl sətri ayrıca test case-dir (TC ID birinci sütundadır). Gauge ssenarini hər sətir üçün
ayrıca icra edir və hesabatda sətir-sətir göstərir. Uğurlu sətirlərdə alıcı yarandığı üçün hər icra
yeni sandbox-da başlayır.
Texnikalar: boundary value analysis (fullName 1/2/50/51, IBAN 27/28/29, nickname 20/21),
equivalence partitioning (icazəli/icazəsiz simvollar, ölkə kodu, bank kodu, valyuta).

   |tc          |fullName                                           |iban                          |currency|nickname             |status|checkPath    |checkValue      |
   |------------|---------------------------------------------------|------------------------------|--------|---------------------|------|-------------|----------------|
   |TC-API-101-005|A                                                |AZ77AIIB40060019440123456789  |AZN     |Anam                 |400   |details.field|fullName        |
   |TC-API-101-006|Al                                               |AZ77AIIB40060019440123456789  |AZN     |Anam                 |201   |fullName     |Al              |
   |TC-API-101-007|Abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij|AZ77AIIB40060019440123456789  |AZN     |Anam                 |201   |id           |ben_            |
   |TC-API-101-008|Abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijk|AZ77AIIB40060019440123456789 |AZN     |Anam                 |400   |details.field|fullName        |
   |TC-API-101-009|---                                              |AZ77AIIB40060019440123456789  |AZN     |Anam                 |400   |details.field|fullName        |
   |TC-API-101-010|Ali2                                             |AZ77AIIB40060019440123456789  |AZN     |Anam                 |400   |details.field|fullName        |
   |TC-API-101-011|Şəhla Qasımova-O'Neil                            |AZ77AIIB40060019440123456789  |AZN     |Anam                 |201   |fullName     |Şəhla Qasımova-O'Neil|
   |TC-API-101-013|Nigar Əliyeva                                    |AZ77AIIB4006001944012345678   |AZN     |Anam                 |400   |details.field|iban            |
   |TC-API-101-014|Nigar Əliyeva                                    |AZ77AIIB400600194401234567890 |AZN     |Anam                 |400   |details.field|iban            |
   |TC-API-101-015|Nigar Əliyeva                                    |GB77AIIB40060019440123456789  |AZN     |Anam                 |400   |details.field|iban            |
   |TC-API-101-016|Nigar Əliyeva                                    |AZ77123440060019440123456789  |AZN     |Anam                 |400   |details.field|iban            |
   |TC-API-101-017|Nigar Əliyeva                                    |AZ77AIIB40060019440123456789  |GBP     |Anam                 |400   |details.field|currency        |
   |TC-API-101-018|Nigar Əliyeva                                    |AZ77AIIB40060019440123456789  |AZN     |Abcdefghijabcdefghij |201   |nickname     |Abcdefghijabcdefghij|
   |TC-API-101-019|Nigar Əliyeva                                    |AZ77AIIB40060019440123456789  |AZN     |Abcdefghijabcdefghijk|400   |details.field|nickname        |

tags: api, grad-101, beneficiaries, data-driven

## Alıcı sahələrinin validasiyası (hər sətir = bir test case)
tags: regression, boundary, AC-5, AC-6

* User1 yeni sandbox ilə daxil olur
* Alıcı yaratma sorğusu göndər <fullName> <iban> <currency> <nickname>
* Status kodunun <status> olmalıdır
* Json cavabında <checkPath> deyerinde <checkValue> olmalıdır

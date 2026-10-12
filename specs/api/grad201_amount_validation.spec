# GRAD-201 · initialAmount validasiyası — data-driven (BVA + ekvivalent siniflər)

Hər cədvəl sətri ayrıca test case-dir. Sərhədlər: 1.00 – 1000.00, maksimum 2 onluq, yalnız number tipi.
"50" sətrində dəyər dırnaq içində göndərilir — JSON-da mətn (string) olur.

   |tc            |amount |status|checkPath       |checkValue      |
   |--------------|-------|------|----------------|----------------|
   |TC-API-201-003|0.99   |400   |code            |VALIDATION_ERROR|
   |TC-API-201-004|1.00   |201   |availableBalance|1               |
   |TC-API-201-005|1000.00|201   |availableBalance|1000            |
   |TC-API-201-006|1000.01|400   |code            |VALIDATION_ERROR|
   |TC-API-201-007|"50"   |400   |code            |VALIDATION_ERROR|
   |TC-API-201-008|10.555 |400   |code            |VALIDATION_ERROR|
   |TC-API-201-009|10.55  |201   |availableBalance|10.55           |
   |TC-API-201-010|0      |400   |code            |VALIDATION_ERROR|
   |TC-API-201-010|-5     |400   |code            |VALIDATION_ERROR|

tags: api, grad-201, cards, data-driven

## initialAmount sahəsinin validasiyası (hər sətir = bir test case)
tags: regression, boundary, AC-3, AC-4

* User1 yeni sandbox ilə daxil olur
* Kart buraxma sorğusu göndər "acc_002" <amount> "BVA"
* Status kodunun <status> olmalıdır
* Json cavabında <checkPath> deyerinde <checkValue> olmalıdır

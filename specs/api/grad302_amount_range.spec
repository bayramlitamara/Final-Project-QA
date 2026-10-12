# GRAD-302 · Təchizatçı məbləğ aralığı — data-driven BVA (Azercell: 0.50 – 200.00)

   |tc            |amount|status|checkPath|checkValue         |
   |--------------|------|------|---------|-------------------|
   |TC-API-302-013|0.49  |422   |code     |AMOUNT_OUT_OF_RANGE|
   |TC-API-302-014|0.50  |201   |status   |SUCCESS            |
   |TC-API-302-015|200.00|201   |status   |SUCCESS            |
   |TC-API-302-016|200.01|422   |code     |AMOUNT_OUT_OF_RANGE|

tags: api, grad-302, payments, data-driven

## Azercell məbləğ sərhədləri (hər sətir = bir test case)
tags: regression, boundary, AC-8

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" "azercell" "501234567" <amount>
* Status kodunun <status> olmalıdır
* Json cavabında <checkPath> deyeri <checkValue> beraberdir

# GRAD-302 · Komissiya hesablanması — data-driven

CityNet: 1%, minimum 0.20, maksimum 2.00 (AC-9). Aztelekom: sabit 0.50 (AC-10). total = amount + fee (AC-1).

   |tc            |biller   |subscriber|amount|fee |total |
   |--------------|---------|----------|------|----|------|
   |TC-API-302-017|citynet  |CN123456  |5     |0.2 |5.2   |
   |TC-API-302-017|citynet  |CN123456  |20    |0.2 |20.2  |
   |TC-API-302-017|citynet  |CN123456  |21    |0.21|21.21 |
   |TC-API-302-017|citynet  |CN123456  |150   |1.5 |151.5 |
   |TC-API-302-018|aztelekom|1234567   |10    |0.5 |10.5  |
   |TC-API-302-018|aztelekom|1234567   |100   |0.5 |100.5 |

tags: api, grad-302, payments, data-driven

## Komissiya və cəm (hər sətir = bir yoxlama)
tags: regression, boundary, AC-9, AC-10

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* Ödəniş sorğusu göndər "${cardId}" <biller> <subscriber> <amount>
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri <fee> beraberdir
* Json cavabında "total" deyeri <total> beraberdir

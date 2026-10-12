# GRAD-302 · Idempotency-Key uzunluğu — data-driven BVA (8 – 64 simvol)

   |tc            |key                                                               |status|checkPath|checkValue              |
   |--------------|------------------------------------------------------------------|------|---------|------------------------|
   |TC-API-302-007|abcdefg                                                           |400   |code     |IDEMPOTENCY_KEY_INVALID |
   |TC-API-302-008|abcdefgh                                                          |201   |status   |SUCCESS                 |
   |TC-API-302-009|abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefgh  |201   |status   |SUCCESS                 |
   |TC-API-302-010|abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghi |400   |code     |IDEMPOTENCY_KEY_INVALID |

tags: api, grad-302, payments, data-driven

## Idempotency-Key sərhədləri (hər sətir = bir test case)
tags: regression, boundary

* User1 yeni sandbox ilə daxil olur
* User1 üçün "1000" AZN-lik aktiv kart yaradılır və id "cardId" olaraq saxlanılır
* <key> açarı ilə ödəniş sorğusu göndər "${cardId}" "citynet" "CN123456" "10"
* Status kodunun <status> olmalıdır
* Json cavabında <checkPath> deyeri <checkValue> beraberdir

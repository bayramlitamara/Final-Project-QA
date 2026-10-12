# GRAD-301 · GET /billers — Xidmət təchizatçıları kataloqu

Epic: EPIC-3 Kommunal ödənişlər · Prioritet: Low · Story point: 2
Yalnız oxuma (read-only) endpoint-dir — ortaq sandbox kifayətdir.

tags: api, grad-301, billers

## TC-API-301-001 Parametrsiz kataloq: 6 təchizatçı, hər biri tam məlumatla
tags: regression, positive, AC-1

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.id" siyahısındakı deyerler unikal olmalıdır
* Cavab "billers.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabını cedvel ile yoxla

   |path                                             |value          |
   |-------------------------------------------------|---------------|
   |items.find { it.id == 'citynet' }.minAmount      |5              |
   |items.find { it.id == 'citynet' }.maxAmount      |150            |
   |items.find { it.id == 'citynet' }.fee.type       |PERCENT        |
   |items.find { it.id == 'citynet' }.subscriberPattern|@contains:CN|

## TC-API-301-002 MOBILE kateqoriyası: yalnız Azercell və Bakcell
tags: regression, positive, AC-2

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "category" = "MOBILE"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.category" siyahısındakı bütün deyerler "MOBILE" olmalıdır
* Json cavabında "items.id" deyerinde "azercell" olmalıdır
* Json cavabında "items.id" deyerinde "bakcell" olmalıdır

## TC-API-301-003 UTILITY və INTERNET kateqoriyaları
tags: regression, positive, AC-2

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "category" = "UTILITY"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.category" siyahısındakı bütün deyerler "UTILITY" olmalıdır
* Json cavabında "items.id" deyerinde "azerisiq" olmalıdır
* Json cavabında "items.id" deyerinde "azersu" olmalıdır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "category" = "INTERNET"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.category" siyahısındakı bütün deyerler "INTERNET" olmalıdır
* Json cavabında "items.id" deyerinde "citynet" olmalıdır
* Json cavabında "items.id" deyerinde "aztelekom" olmalıdır

## TC-API-301-004 İcazəsiz kateqoriya (GAS)
tags: regression, negative, AC-3

* User1 ortaq sandbox ilə daxil olur
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "category" = "GAS"
* "GET" sorğusu gönder "/billers"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC-API-301-006 Token olmadan kataloq
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "GET" sorğusu gönder "/billers"
* Status kodunun "401" olmalıdır

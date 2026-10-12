# GRAD-102 · GET /beneficiaries — Alıcılar siyahısı: axtarış, filtr, sıralama

Epic: EPIC-1 · Prioritet: Medium · Story point: 3
Bu spec ayrıca sandbox-da işləyir (login-user1-list.json ilə keşli token). Hər ssenaridən əvvəl eyni
5 alıcı yaradılmağa çalışılır: birinci ssenaridə yaranır, sonrakılarda 409 qaytarılır — data sabit qalır.
Test datası (yaradılma ardıcıllığı ilə): Nigar Əliyeva/AZN/Anam, Çingiz Abdullayev/USD/Dost,
Elvin Həsənov/EUR/Qonşu, İlqar Quliyev/AZN/Əmi, Ülvi Məmmədov/USD/Həmkar.

tags: api, grad-102, beneficiaries

* Siyahı testləri üçün 5 alıcı hazırla

## TC-API-102-001 Parametrsiz siyahı: total = items.length, ən yeni birinci
tags: regression, positive, AC-1

* Alıcılar siyahısını al
* Json cavabında "total" deyeri "5" beraberdir
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items[0].fullName" deyeri "Ülvi Məmmədov" beraberdir
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır
* Cavab "beneficiary-list.schema.json" JSON schema-sına uyğun olmalıdır

## TC-API-102-002 Ad üzrə artan sıralama — Azərbaycan əlifbası
tags: regression, positive, AC-2

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path              |value            |
   |------------------|-----------------|
   |items[0].fullName |Çingiz Abdullayev|
   |items[1].fullName |Elvin Həsənov    |
   |items[2].fullName |İlqar Quliyev    |
   |items[3].fullName |Nigar Əliyeva    |
   |items[4].fullName |Ülvi Məmmədov    |

## TC-API-102-003 Ad üzrə azalan sıralama
tags: regression, positive, AC-2

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "desc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items[0].fullName" deyeri "Ülvi Məmmədov" beraberdir
* Json cavabında "items[4].fullName" deyeri "Çingiz Abdullayev" beraberdir

## TC-API-102-004 Yaradılma tarixi üzrə artan sıralama
tags: regression, positive

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "sort" = "createdAt"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir
* Json cavabında "items.createdAt" siyahısı artan sırada olmalıdır

## TC-API-102-005 Valyuta filtri (USD)
tags: regression, positive, AC-3

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "currency" = "USD"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır

## TC-API-102-006 Axtarış: İ/I fərqi nəzərə alınmır (NİGAR və NIGAR)
tags: regression, positive, AC-4

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "NİGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "NIGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır

## TC-API-102-007 Axtarış: böyük-kiçik hərf fərqi nəzərə alınmır
tags: regression, positive, AC-4

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "nigar"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır

## TC-API-102-008 Axtarış lәqəbin bir hissəsi ilə
tags: regression, positive, AC-5

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "nam"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.nickname" deyerinde "Anam" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir

## TC-API-102-009 Axtarış — 1 simvol (sərhəd − 1)
tags: regression, boundary, AC-6

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "a"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "q" olmalıdır

## TC-API-102-010 Axtarış — 2 simvol (aşağı sərhəd)
tags: regression, boundary, AC-6

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "ni"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır

## TC-API-102-011 Nəticəsiz axtarış
tags: regression, positive, AC-7

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "zzzz"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-API-102-012 Parametrlərin birləşdirilməsi (AND məntiqi)
tags: regression, positive

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "q" = "li"
* Query parametri elave et "currency" = "AZN"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items[0].fullName" deyeri "İlqar Quliyev" beraberdir
* Json cavabında "items[1].fullName" deyeri "Nigar Əliyeva" beraberdir
* Json cavabında "items.currency" siyahısındakı bütün deyerler "AZN" olmalıdır

## TC-API-102-013 İcazəsiz currency / sort / order dəyərləri
tags: regression, negative

* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "currency" = "GBP"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "sort" = "iban"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "sort" olmalıdır
* "${u1Token}" tokeni ilə yeni sorğu hazırla
* Query parametri elave et "order" = "up"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "details.field" deyerinde "order" olmalıdır

## TC-API-102-014 user2 user1-in alıcılarını görmür
tags: regression, security

* User2 ortaq sandbox ilə daxil olur
* "${u2Token}" tokeni ilə yeni sorğu hazırla
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.findAll { it.fullName == 'Nigar Əliyeva' }.size()" deyeri "0" beraberdir

## TC-API-102-015 Token olmadan siyahı
tags: regression, security

* Tokensiz yeni sorğu hazırla
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

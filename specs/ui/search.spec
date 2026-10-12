# turbo.az · Əsas axtarış (TS-01)

Test case-lər: Tamara_Məlikova_Turbo.az_Test_Cases.xlsx → TC-SRCH-*.
Yoxlama prinsipi: konkret elana yox, QAYDAYA assert edilir. "Cards Not ..." locator-ları qaydanı pozan
elanları tapır və onların sayı 0 olmalıdır. Boş nəticə ilə yalançı PASS olmasın deyə əvvəlcə ən azı
1 elanın göstərildiyi yoxlanılır. Yalnız "ELANLAR" bölməsi yoxlanılır (VIP/Premium bloklar xaric).

tags: ui, search

## TC-SRCH-001 Marka filtri ilə axtarış
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Toyota" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not Toyota" elementlerinin sayı "0" olmalıdır

## TC-SRCH-002 Marka və model filtri ilə axtarış
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Toyota" seç
* "q_model" açılan siyahısından "Camry" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not Toyota Camry" elementlerinin sayı "0" olmalıdır

## TC-SRCH-003 Marka dəyişdikdə model siyahısının yenilənməsi
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Toyota" seç
* "xpath=//div[@data-id='q_model']//div[contains(@class,'tz-dropdown__option')][normalize-space()='Camry']" elementlerinin sayı en az "1" olmalıdır
* "xpath=//div[@data-id='q_model']//div[contains(@class,'tz-dropdown__option')][normalize-space()='X5']" elementlerinin sayı "0" olmalıdır
* "q_make" açılan siyahısından "BMW" seç
* "xpath=//div[@data-id='q_model']//div[contains(@class,'tz-dropdown__option')][normalize-space()='X5']" elementlerinin sayı en az "1" olmalıdır
* "xpath=//div[@data-id='q_model']//div[contains(@class,'tz-dropdown__option')][normalize-space()='Camry']" elementlerinin sayı "0" olmalıdır

## TC-SRCH-004 Şəhər filtri ilə axtarış
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_region" açılan siyahısından "Gəncə" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not In Gence" elementlerinin sayı "0" olmalıdır

## TC-SRCH-005 "Yeni" avtomobil filtri — ilk 3 elan "Yeni: Bəli"
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "Yeni" metnli elemente klik et
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Card Links" elementlerinin sayı en az "3" olmalıdır
* "First Card Link" elementinin "href" atributunu "ad1" olaraq yadda saxla
* "Second Card Link" elementinin "href" atributunu "ad2" olaraq yadda saxla
* "Third Card Link" elementinin "href" atributunu "ad3" olaraq yadda saxla
* "${ad1}" adresine keçid et
* "Ad New Value" elementinin metni "Bəli" olmalıdır
* "${ad2}" adresine keçid et
* "Ad New Value" elementinin metni "Bəli" olmalıdır
* "${ad3}" adresine keçid et
* "Ad New Value" elementinin metni "Bəli" olmalıdır

## TC-SRCH-007 Marka, model və şəhər kombinasiyası
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Hyundai" seç
* "q_model" açılan siyahısından "Santa Fe" seç
* "q_region" açılan siyahısından "Bakı" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not Hyundai Santa Fe" elementlerinin sayı "0" olmalıdır
* "Cards Not In Baku" elementlerinin sayı "0" olmalıdır

## TC-SRCH-008 Nəticəsi olmayan filtr kombinasiyası
tags: regression, negative

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Aston Martin" seç
* "q_region" açılan siyahısından "Lerik" seç
* Axtarışı göndər
* Sehifede "tapılmadı" yazısı olmalıdır
* "xpath=//div[contains(@class,'products-i__name')][starts-with(normalize-space(),'Aston Martin')]" sehifede mövcud olmamalıdır

## TC-SRCH-009 Filtrlər URL-də saxlanılır və yenilənmədən sonra qalır
tags: regression, positive

* Toyota elanları siyahısını aç
* URL "make" içermelidir
* Sehifeni yenile
* Sehifenin tam yüklenmesini gözle
* URL "make" içermelidir
* "Selected Make Options" elementlerinin sayı en az "1" olmalıdır
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not Toyota" elementlerinin sayı "0" olmalıdır

## TC-SRCH-010 "Sıfırla" düyməsi filtrləri təmizləyir
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Toyota" seç
* "q_region" açılan siyahısından "Bakı" seç
* "Price From Input" elementine "10000" yaz
* "Reset Link" elementine JavaScript ile klik et
* "2" saniye gözle
* "Selected Make Options" elementlerinin sayı "0" olmalıdır
* "Selected Region Options" elementlerinin sayı "0" olmalıdır
* "Price From Input" input deyeri "" olmalıdır

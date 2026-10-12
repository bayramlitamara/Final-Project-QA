# turbo.az · Qiymət və buraxılış ili filtrləri (TS-02, TS-03)

Qiymət yoxlaması yalnız ₼ ilə göstərilən elanlarda aparılır (USD/EUR elanlar konvertasiya olunduğu üçün kənarda qalır).

tags: ui, price, year

## TC-PRICE-001 Qiymət aralığı 10000 – 20000 AZN
tags: regression, positive

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "Price From Input" elementine "10000" yaz
* "Price To Input" elementine "20000" yaz
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List AZN Cards" elementlerinin sayı en az "1" olmalıdır
* "AZN Prices Outside 10000-20000" elementlerinin sayı "0" olmalıdır

## TC-PRICE-004 Minimum və maksimum qiymət bərabərdir (15000 – 15000)
tags: regression, boundary

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "Price From Input" elementine "15000" yaz
* "Price To Input" elementine "15000" yaz
* Axtarışı göndər
* "AZN Prices Not 15000" elementlerinin sayı "0" olmalıdır

## TC-PRICE-006 Qiymət sahəsi "-" simvolunu qəbul etmir
tags: regression, negative

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "Price From Input" elementine "-" yaz
* "Price From Input" input deyeri "" olmalıdır

## TC-PRICE-007 Qiymət sahəsi hərfləri qəbul etmir
tags: regression, negative

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "Price From Input" elementine "abcd" yaz
* "Price From Input" input deyeri "" olmalıdır

## TC-YEAR-001 Buraxılış ili aralığı 2015 – 2020
tags: regression, positive

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "q_year_from" açılan siyahısından "2015" seç
* "q_year_to" açılan siyahısından "2020" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Years Outside 2015-2020" elementlerinin sayı "0" olmalıdır

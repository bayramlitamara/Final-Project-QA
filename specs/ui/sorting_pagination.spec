# turbo.az · Sıralama və səhifələmə (TS-05, TS-06)

Sıralama yoxlaması: ardıcıl iki ₼ elanı müqayisə olunur; qaydanı pozan cüt tapılmamalıdır.
"Tarixə görə" sıralama bilərəkdən manual qalır ("İrəli çək" xidməti elanların yerini dəyişir → flaky).

tags: ui, sorting, pagination

## TC-SORT-001 "Əvvəlcə ucuz" sıralaması
tags: regression, positive

* Toyota elanları siyahısını aç
* Siyahını "Əvvəlcə ucuz" üzrə sırala
* "Main List Regular AZN Cards" elementlerinin sayı en az "2" olmalıdır
* "Price Ascending Violations" elementlerinin sayı "0" olmalıdır

## TC-SORT-002 "Əvvəlcə bahalı" sıralaması
tags: regression, positive

* Toyota elanları siyahısını aç
* Siyahını "Əvvəlcə bahalı" üzrə sırala
* "Main List Regular AZN Cards" elementlerinin sayı en az "2" olmalıdır
* "Price Descending Violations" elementlerinin sayı "0" olmalıdır

## TC-SORT-006 Sıralama dəyişdikdə filtrlər qorunur
tags: regression, positive

Bu ssenarinin əsas məqsədi sıralamadan sonra filtrlərin qorunmasıdır. Sıralama qaydasının özü SORT-001/002-də
ciddi yoxlanılır; burada isə nəticədə adi ₼ elanı az ola bilər (canlı data), ona görə qoruyucu yoxlama bütün elanlara aiddir.

* Turbo.az ana səhifəsini aç
* "q_make" açılan siyahısından "Toyota" seç
* "q_region" açılan siyahısından "Bakı" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* Siyahını "Əvvəlcə ucuz" üzrə sırala
* URL "make" içermelidir
* "Main List Cards" elementlerinin sayı en az "2" olmalıdır
* "Cards Not Toyota" elementlerinin sayı "0" olmalıdır
* "Cards Not In Baku" elementlerinin sayı "0" olmalıdır
* "Price Ascending Violations" elementlerinin sayı "0" olmalıdır

## TC-PAGE-002 Növbəti səhifəyə keçid
tags: regression, positive

* Toyota elanları siyahısını aç
* "First Card Link" elementinin "href" atributunu "page1FirstAd" olaraq yadda saxla
* "Pagination Page 2" elementine scroll et ve klik et
* URL "page=2" içermelidir
* Sehifenin tam yüklenmesini gözle
* URL "make" içermelidir
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Not Toyota" elementlerinin sayı "0" olmalıdır
* "xpath=(//div[contains(concat(' ',normalize-space(@class),' '),' products ')])[last()]//a[contains(@class,'products-i__link')][contains(@href, substring-after('${page1FirstAd}','turbo.az'))]" sehifede mövcud olmamalıdır

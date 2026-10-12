# turbo.az · Seçilmişlər və naviqasiya (TS-08, TS-09)

tags: ui, favorites, navigation

## TC-FAV-001 Elanın seçilmişlərə əlavə edilməsi
tags: regression, positive

* Toyota elanları siyahısını aç
* "First Card Link" elementinin "href" atributunu "favHref" olaraq yadda saxla
* "First Card Bookmark" elementine JavaScript ile klik et
* "2" saniye gözle
* "/bookmarks" adresine keçid et
* Sehifenin tam yüklenmesini gözle
* "xpath=//a[contains(@class,'products-i__link')][contains(@href, substring-after('${favHref}','turbo.az'))]" görünür olmalıdır

## TC-FAV-002 Elanın seçilmişlərdən silinməsi
tags: regression, positive

* Toyota elanları siyahısını aç
* "First Card Link" elementinin "href" atributunu "favHref" olaraq yadda saxla
* "First Card Bookmark" elementine JavaScript ile klik et
* "2" saniye gözle
* "/bookmarks" adresine keçid et
* "xpath=//a[contains(@class,'products-i__link')][contains(@href, substring-after('${favHref}','turbo.az'))]" görünür olmalıdır
* "xpath=//div[contains(@class,'products-i')][.//a[contains(@class,'products-i__link')][contains(@href, substring-after('${favHref}','turbo.az'))]]//a[contains(@href,'/bookmarks')]" elementine JavaScript ile klik et
* "2" saniye gözle
* Sehifeni yenile
* Sehifenin tam yüklenmesini gözle
* "xpath=//a[contains(@class,'products-i__link')][contains(@href, substring-after('${favHref}','turbo.az'))]" sehifede mövcud olmamalıdır

## TC-NAV-001 Rus dilinə keçid
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "RU" metnli elemente klik et
* URL "ru.turbo.az" içermelidir
* Sehifenin tam yüklenmesini gözle
* "Html Root" elementinin "lang" atributu "ru" olmalıdır

## TC-NAV-002 Əsas menyu linkləri düzgün bölmələri açır
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "Bütün elanlar" metnli elemente klik et
* URL "/autos" içermelidir
* "/" adresine keçid et
* "Dilerlər" metnli elemente klik et
* URL "/avtosalonlar" içermelidir
* "/" adresine keçid et
* "Avtokataloq" metnli elemente klik et
* URL "/autocatalog" içermelidir
* "/" adresine keçid et
* "Moto" metnli elemente klik et
* URL "/motosiklet" içermelidir

# turbo.az · Elan səhifəsi (TS-07)

Elan test zamanı siyahıdan dinamik seçilir — konkret elan ID-sinə bağlılıq yoxdur.

tags: ui, ad-page

## TC-AD-001 Elan kartındakı məlumat detal səhifə ilə uyğundur
tags: regression, positive

* Toyota elanları siyahısını aç
* "First Card Name" elementinin metnini "cardName" olaraq yadda saxla
* "First Card Price" elementinin metnini "cardPrice" olaraq yadda saxla
* "First Card Link" elementinin "href" atributunu "cardHref" olaraq yadda saxla
* "${cardHref}" adresine keçid et
* Sehifenin tam yüklenmesini gözle
* URL "/autos/" içermelidir
* Sehifede "${cardName}" yazısı olmalıdır
* Sehifede "${cardPrice}" yazısı olmalıdır

## TC-AD-002 Elan səhifəsində xüsusiyyətlər blokunun tamlığı
tags: regression, positive

* Toyota elanları siyahısını aç
* "First Card Link" elementinin "href" atributunu "cardHref" olaraq yadda saxla
* "${cardHref}" adresine keçid et
* "Ad Properties" elementlerinin sayı en az "10" olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Şəhər']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Marka']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Model']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Buraxılış ili']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Ban növü']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Rəng']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Mühərrik']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Yürüş']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Sürətlər qutusu']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Ötürücü']" görünür olmalıdır
* "xpath=//*[contains(@class,'product-properties__i-name')][normalize-space()='Yeni']" görünür olmalıdır

## TC-AD-008 Mövcud olmayan elan ID-si
tags: regression, negative

* Brauzeri aç ve keçid et "/autos/1"
* Sehifenin tam yüklenmesini gözle
* Sehifede "tapılmadı" yazısı olmalıdır
* "Ad Properties" sehifede mövcud olmamalıdır

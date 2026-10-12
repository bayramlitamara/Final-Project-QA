# turbo.az · Əlavə filtrlər (TS-04)

Yalnız elan kartında görünən məlumatla yoxlana bilən filtrlər avtomatlaşdırılıb (mühərrik növü, yürüş, mühərrik həcmi, "Kreditdədir").
Elektro: kartda litrlə mühərrik həcmi (məs. "1.5 L") görünən elan olmamalıdır. "kWh" yoxlanmır, çünki satıcı batareya həcmini doldurmaya bilər.

tags: ui, filters

## TC-FLTR-001 Yanacaq növü "Elektro"
tags: regression, positive

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "q_fuel_type" açılan siyahısından "Elektro" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards With Combustion Engine" elementlerinin sayı "0" olmalıdır

## TC-FLTR-004 Yürüş aralığı 0 – 50000 km
tags: regression, positive

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "Mileage From Input" elementine "0" yaz
* "Mileage To Input" elementine "50000" yaz
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Mileage Above 50000" elementlerinin sayı "0" olmalıdır

## TC-FLTR-006 "Kredit" filtri
tags: regression, positive

* Turbo.az ana səhifəsini aç
* "Loan Checkbox Label" elementine klik et
* "Loan Checkbox" seçilmiş olmalıdır
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Cards Without Loan Label" elementlerinin sayı "0" olmalıdır

## TC-FLTR-012 Mühərrik həcmi 1500 – 2000 sm³
tags: regression, positive

* Turbo.az ana səhifəsini aç
* Daha çox filtri aç
* "q_engine_volume_from" açılan siyahısından "1500" seç
* "q_engine_volume_to" açılan siyahısından "2000" seç
* Axtarışı təsdiqlə və nəticələri gözlə
* "Main List Cards" elementlerinin sayı en az "1" olmalıdır
* "Engine Outside 1.5-2.0 L" elementlerinin sayı "0" olmalıdır

# Bitirmə layihəsi — Tamara Məlikova

turbo.az (Web UI) və Banking API (https://api.anarabbas.com) üçün test layihəsi.
Avtomatlaşdırma müəllimin təqdim etdiyi arxitektura üzərində qurulub:
https://github.com/Anar95/Gauge-Test-Automation. **Arxitekturada heç bir dəyişiklik edilməyib** —
`src/test/java`, `pom.xml`, `manifest.json` olduğu kimi qalıb. Yalnız "öz layihənizə uyğunlaşdırın"
bölməsində göstərilən yerlər dolduruldu: `env/default/app.properties`, `specs/`, `src/test/resources/`
(locator, body, schema). Heç bir yeni Java step yazılmayıb — hər şey hazır step-lərlə yazılıb.

## 1. Tapşırıq tələbləri → harada
| Tələb | Fayl |
|---|---|
| Test plan (1 səhifə) | `docs/TEST_PLAN.md` |
| Test ssenariləri + test case-lər (Excel) | `docs/Tamara_Məlikova_Test_Cases.xlsx` (Web və API ayrı sheet-lərdə, "Xülasə" sheet-i ilə) |
| Manual / avtomat bölgüsü və səbəbi | Excel → "Execution Type" və "Manual / Automation əsaslandırması" sütunları |
| Traceability (AC → test case) | Excel → "API Traceability" sheet-i (69 AC-nin hamısı əhatə olunub) |
| Grooming sualları | Excel → "API Grooming Questions" sheet-i (15 sual) |
| CallMan collection + environment | `docs/CallMan/*.json` (Postman v2.1 formatı) |
| Tapıntılar (uyğunsuzluqlar) | Excel → "Tapıntılar" sheet-i |
| Regression avtomatlaşdırması — Web | `specs/ui/` (29 test case) |
| Regression avtomatlaşdırması — API | `specs/api/` (156 test case) |
| Test hesabatı (Allure əvəzinə) | Excel → "Test Report" sheet-i: nəticələr, qrafiklər, stabillik, tapıntılar |
| Gauge icra hesabatı | `reports/html-report/index.html` (hər icradan sonra yaranır) |

## 2. Quraşdırma və icra
```bash
brew install gauge maven            # Windows: choco install gauge maven
gauge install java && gauge install html-report

# PowerShell-də -D arqumentlərini dırnağa alın: mvn test "-Dgauge.specs.dir=specs/api"
mvn test                                            # hamısı (API + UI)
mvn test -Dgauge.specs.dir=specs/api                # yalnız API
mvn test -Dgauge.specs.dir=specs/ui                 # yalnız turbo.az
mvn test -Dgauge.specs.dir=specs/api/grad302_bill_payment.spec   # tək fayl
mvn test -Dtags="grad-302"                          # tək task
mvn test -Dtags="api & security"                    # bütün 401/404 izolyasiya testləri
mvn test -Denv=ci                                   # brauzer headless
```
> Testləri yalnız `mvn test` ilə işə salın (`gauge run` Maven asılılıqlarını görmür).

## 3. Struktur
```
specs/api/concepts/   auth.cpt · beneficiaries.cpt · cards.cpt · payments.cpt   (təkrarlanan addımlar)
specs/api/            hər task üçün bir spec + 5 data-driven spec (BVA)
specs/ui/concepts/    turbo.cpt  (açılan siyahıdan seçim, axtarışın təsdiqi, sıralama)
specs/ui/             search · price_year · filters · sorting_pagination · ad_page · favorites_navigation
src/test/resources/body/     request şablonları (${dəyişən} ilə)
src/test/resources/schema/   JSON Schema (beneficiary, card, billers, bill-payment, error ...)
src/test/resources/locator/  turbo-az.json — bütün turbo.az locator-ları bir yerdə
```
Hər ssenarinin başlığı Excel-dəki TC ID-si ilə başlayır (məs. `## TC-API-302-004 ...`), data-driven
spec-lərdə TC ID cədvəlin birinci sütunundadır → hesabatdakı hər nəticə birbaşa test case-ə bağlanır.

## 4. Dizayn qərarları
**Sandbox strategiyası (API).** Hər login yeni, boş sandbox açır. Resurs yaradan ssenarilər
`User1 yeni sandbox ilə daxil olur` concept-i ilə başlayır — hər biri öz mühitində işləyir, öz datasını yaradır.
Nəticə: ssenarilər ardıcıllıqdan asılı deyil, alıcı limiti (10), kart limiti (3), gündəlik limit (500)
və qəbz nömrəsi (000001) hər dəfə eyni nəticə verir — flaky test yoxdur. Data yaratmayan validasiya və
read-only ssenarilər keşli login-dən istifadə edir (`User1 ortaq sandbox ilə daxil olur`) — login sayı azalır.
GRAD-102 öz ayrıca sandbox-unda işləyir: hər ssenaridən əvvəl eyni 5 alıcı yaradılmağa çalışılır, sonrakı
cəhdlər 409 alır — data sabit qalır.

**Data-driven BVA.** Gauge-un spec səviyyəli cədvəlləri: `grad101_field_validation.spec`,
`grad201_amount_validation.spec`, `grad302_amount_range.spec`, `grad302_fee_calculation.spec`,
`grad302_idempotency_key.spec`. Hər sətir ayrıca test case kimi icra olunur və hesabatda ayrıca görünür.

**Assert-lər.** Yalnız status yox: `code`, `details[].field`, dəyərlər, header-lər (Location,
Idempotent-Replay), JSON Schema. Xəta mətninə yox, `code`-a assert edilir (backlog qaydası).
Onluq ədədlər mətn kimi müqayisə olunur ("949.5") — RestAssured JsonPath onluqları Float qaytarır və
rəqəm kimi müqayisədə 0.21 ≠ 0.21000000298 kimi yalançı xəta yaranır.

**Web yoxlamaları qaydaya əsaslanır.** "Cards Not Toyota", "AZN Prices Outside 10000-20000",
"Price Ascending Violations" kimi locator-lar qaydanı POZAN elanları tapır və onların sayı 0 olmalıdır.
Əvvəlcə "ən azı 1 nəticə" yoxlanılır ki, boş səhifədə yalançı PASS olmasın. Konkret elana bağlılıq
yoxdur — canlı saytda data dəyişsə də testlər sınmır. VIP/Premium bloklar yoxlamadan kənardadır (onlar sıralamaya tabe deyil).
Axtarışdan sonra URL-in dəyişməsi gözlənilir, sonra yoxlama edilir — köhnə səhifədə yoxlama riski yoxdur.

## 5. İcra nəticələri (02.10.2026)
| Paket | Ssenari | Nəticə |
|---|---|---|
| API (`specs/api`) | 161 (156 test case; data-driven cədvəllərdə hər sətir ayrıca ssenaridir) | Ardıcıl 3 icrada 161/161 keçdi |
| Web (`specs/ui`) | 29 | 29/29 keçdi |

Avtomat test case-lərin faktiki nəticəsi Excel-in "Actual Result" və "Status" sütunlarındadır.

**İlk icralarda düzəldilənlər (turbo.az).** Locator-lar ilk icradan sonra real DOM-a görə dəqiqləşdirildi: qiymət
elementi (`products-i__price`), əsas siyahı ("ELANLAR" başlığından sonrakı blok), sıralama (`select` elementi),
"Sıfırla" linki, açıq qalan şəhər siyahısının "Elanları göstər" düyməsini örtməsi (düymə JavaScript ilə basılır),
siyahı animasiyası zamanı yanlış seçim (açıldıqdan sonra 1 san. gözləmə). TC-FLTR-001 qaydası "kWh var" əvəzinə
"litrlə mühərrik həcmi yoxdur" oldu (satıcı batareya həcmini doldurmaya bilər). TC-SORT-006-nın ilkin yoxlaması
canlı datanın tərkibindən asılı olmasın deyə bütün elanlara aid edildi.

**Mühit müşahidəsi.** turbo.az bəzən səhifəni 3 dəqiqədən çox yükləyir (çoxlu reklam banneri). Belə halda test
`TimeoutException` (`get url=...` və ya klikdən sonra) ilə düşür və təkrar icrada keçir. Bu, test xətası deyil;
həmin spec-i yenidən işə salmaq kifayətdir: `mvn test "-Dgauge.specs.dir=specs/ui/<fayl>.spec"`.

## 6. Məhdudiyyətlər və qeydlər (müəllimə)
- **Allure / TestNG / POJO:** tapşırıqda qeyd olunub, lakin təqdim olunan arxitekturada yoxdur və arxitekturanı
  dəyişmək qadağandır. Müəllimin razılığı ilə Allure əvəzinə test hesabatı Excel-də ayrıca "Test Report" sheet-i
  kimi hazırlanıb (formullarla test case sheet-lərindən hesablanır). Hər icranın addım-addım detalları Gauge HTML
  hesabatındadır. RestAssured framework-ün içində işləyir.
- **Manual qalanlar:** API-də 13, web-də 99 test case — səbəbləri Excel-də. Xüsusilə:
  TC-API-302-019/020 (perTransaction 300) — hansı təchizatçı ilə 300-ə çatılacağı backlog-da yoxdur;
  TC-API-202-005 (00:00 sıfırlanma); TC-API-GEN-005 (429 rate limit — paylaşılan serverə yük).
- **Spesifikasiya ziddiyyəti:** GRAD-201 AC-5 başqasının hesabı üçün 403 FORBIDDEN gözləyir, ümumi
  qayda isə 404 deyir. Test AC-yə uyğun yazılıb, sual grooming siyahısındadır (№1).
- TC-API-201-002 expiry ilini `/29` kimi yoxlayır (2026 + 3). 2027-ci ildə yenilənməlidir.
- TC-API-303-009 `${today}` (kompüterin tarixi) istifadə edir — testləri Bakı vaxt qurşağında işə salın.
- 429 alınarsa: `env/default/app.properties` → `api_max_retries`, `api_retry_max_wait_seconds` artırın.

# Test Plan — Bitirmə layihəsi (turbo.az Web UI + Banking API)

**Müəllif:** Tamara Məlikova · **Versiya:** 1.0 · **Tarix:** 9 oktyabr 2026 · **Təhvil:** 13 oktyabr 2026

## 1. Məqsəd və obyektlər
| Obyekt | Mühit | Mənbə |
|---|---|---|
| Web UI — turbo.az (avtomobil elanları) | Production, https://turbo.az | Saytın özü (sənədləşdirilmiş tələb yoxdur → kəşfiyyat + domen bilikləri) |
| REST API — 10 task (GRAD-101…303), 3 epic, 37 SP | Test, https://api.anarabbas.com | Final project backlog (user story + acceptance criteria) |

## 2. Scope
**Daxildir:** turbo.az-ın əsas axını (axtarış, filtrlər, sıralama, səhifələmə, elan səhifəsi, seçilmişlər, dil/naviqasiya); giriş, yeni elan və ödənişli xidmətlər yalnız manual və məhdud şəkildə. API-nin 10 task-ının bütün AC-ləri (69 AC → Traceability).
**Daxil deyil (səbəbləri Excel-də "Web Test Scope" sheet-indədir):** Moto/ehtiyat hissələri, biznes hesabı, elanın real göndərilməsi, real ödənişlər, mobil tətbiq, performans və təhlükəsizlik (penetration) testləri, canlı sayta yük.

## 3. Yanaşma
- **Risk əsaslı prioritetləşdirmə:** API-də GRAD-302 (Highest, pul əməliyyatı) və High task-lar birinci.
- **Test dizayn texnikaları:** equivalence partitioning, boundary value (fullName 1/2/50/51, initialAmount 0.99/1.00/1000.00/1000.01, Idempotency-Key 7/8/64/65, balans 49.50/49.51 və s.), decision table (xəta yoxlama ardıcıllığı), state transition (GRAD-203/204 kart vəziyyətləri — hər xana ayrı test case).
- **Manual/avtomat bölgüsü:** avtomatlaşdırılan = regression paketi. Manual qalanlar: SMS/OTP, real elan və ödəniş, vizual/UX, cross-browser, davranışı sənədləşdirilməmiş hallar (grooming), vaxtdan asılı hallar (00:00 sıfırlanma), 429 rate limit. Hər qərarın səbəbi Excel-dədir.
- **Assert qaydaları:** status + body məzmunu + `code` (mətn yox) + `details[].field` + JSON schema. UI-da konkret elana yox, qaydaya assert (flaky-yə qarşı).

## 4. Test mühiti və alətlər
Java 11+, Maven, Gauge + Selenium 4 + RestAssured 5 (müəllimin təqdim etdiyi arxitektura, dəyişdirilmədən), Google Chrome, CallMan (manual API icrası), Gauge HTML report.
Test istifadəçiləri: admin / user1 (acc_002, AZN 12 500) / user2 (acc_003, USD 890.50). Hər login yeni sandbox açır; resurs yaradan hər avtomat ssenari öz sandbox-unda işləyir → ssenarilər bir-birindən asılı deyil.

## 5. Həcm (sayla)
| | Test case | Avtomat | Manual | Regression |
|---|---|---|---|---|
| Web (turbo.az) | 128 | 29 | 99 | 35 (6-sı manual regression) |
| API | 169 | 156 | 13 | 156 |

## 6. Giriş / çıxış kriteriləri
**Giriş:** backlog "Ready for QA", test mühiti əlçatan, test istifadəçiləri işləyir, grooming sualları göndərilib.
**Çıxış:** bütün High/Highest test case-lər icra olunub; avtomat paket ardıcıl 3 icrada stabil (flaky yoxdur); tapılan bug-lar və uyğunsuzluqlar sənədləşdirilib; Traceability-də əhatəsiz AC yoxdur.

## 7. Risklər və azaldılması
| Risk | Azaldılma |
|---|---|
| Spesifikasiyada ziddiyyət (GRAD-201 AC-5: 403 vs ümumi qayda 404) və qaranlıq yerlər | 15 grooming sualı; cavab gələnə qədər həmin hallar manual |
| turbo.az DOM-u dəyişə bilər | Locator-lar bir faylda (`locator/turbo-az.json`), qayda əsaslı yoxlamalar |
| Canlı saytda data daim dəyişir | Konkret elana bağlılıq yoxdur, "ən azı 1 nəticə" qoruyucu yoxlaması |
| turbo.az səhifəsi bəzən 3 dəqiqədən çox yüklənir | Belə düşən test təkrar icra olunur; xəta mesajı (TimeoutException) ilə test xətasından ayrılır |
| API rate limit (429) | Framework retry (Retry-After), `api_max_retries=4`; read-only testlər keşli login |
| Vaxt (2 həftə) | Prioritetlə icra: Highest → High → Medium → Low |

## 8. Təhvil veriləcəklər
Test plan (bu sənəd) · Test case-lər (1 Excel faylı: Web və API ayrı sheet-lərdə, traceability ilə) · CallMan collection + environment · Tapıntılar (bug report-lar və uyğunsuzluqlar) · Gauge avtomatlaşdırma layihəsi (GitHub) · Test Report (Excel sheet, Allure əvəzinə) + Gauge HTML hesabatı + təqdimat.

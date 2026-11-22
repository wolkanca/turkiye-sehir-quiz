# 🇹🇷 Türkiye'yi Ne Kadar Tanıyorsun? — Şehri Bul!

**Wolkanca Oyunları #03** — Türkiye'nin şehirlerini tanıtan, tamamen tarayıcıda çalışan, mobil uyumlu bir görsel quiz.

Önceki Wolkanca oyunlarının (`redlist-quiz`, `ai-or-real-quiz`, `zoom-object-quiz`) tek sayfalık, hızlı açılan ve WordPress'e iframe ile gömülen yaklaşımını sürdürür.

## Oyun özellikleri

- **34 farklı şehir** ve her şehir için **özgün SVG illüstrasyon** (fotoğraf değildir; bağımsız görsel sunucusuna ihtiyaç yoktur).
- **10 soru / tur**; yedi coğrafi bölgenin her birinden en az bir şehir gelir.
- **4 seçenek**; daha zorlayıcı olması için aynı coğrafi bölgeden çeldiriciler seçilir.
- İpucu (doğru cevap için kazanılabilecek puandan 35 düşürür), seri bonusu, **20 saniyelik isteğe bağlı mod**.
- Doğru cevaptan sonra **yapı/manzara adı** ve kısa şehir bilgisi.
- `localStorage` aracılığıyla cihazda tutulan kişisel rekor, yeniden oynama, paylaşma veya panoya kopyalama.
- Klavye kısayolları: **1, 2, 3, 4**.
- Harici JavaScript kütüphanesi, ücretli API veya backend **gerekmez**.

## Hemen çalıştır

`index.html` dosyasını tarayıcıda açmak yeterli. Tek HTML dosyası tüm görselleri ve verileri içerir. Alternatif:

```bash
python3 -m http.server 8000
```

Yerel adres: `http://localhost:8000/`.

## GitHub Pages'e yayımla

1. GitHub'da **`turkiye-sehir-quiz`** adında public bir repo aç.
2. Proje dosyalarını `main` dalına yükle. Ana sayfa için gereken tek dosya `index.html`.
3. **Settings → Pages → Deploy from a branch → main / (root)** ayarlarını kaydet.
4. Dağıtım etkinleştiğinde şu adres kullanılabilir: `https://wolkanca.github.io/turkiye-sehir-quiz/`.
5. WordPress yazısına `wordpress-embed.html` içeriğini **Özel HTML** bloğunda ekle.

> **SEO:** GitHub Pages üzerindeki oyun dosyasında `noindex,follow` yer alıyor. İçerik ve arama motoru trafiği için birincil açılış sayfasının wolkanca.com'daki blog yazısı olması amaçlandı. GitHub Pages sayfasını da indeksletmek istersen bu metayı kaldır.

## Proje yapısı

| Dosya | Görevi |
|---|---|
| `index.html` | Üretime hazır tek sayfalık oyun |
| `questions.json` | Tüm şehirler, ipuçları, bilgiler ve SVG illüstrasyon verisi |
| `index.template.html` | Geliştirmeye açık HTML/CSS/JavaScript şablonu |
| `build.py` | Şablon + soru verisi → dağıtıma hazır `index.html` |
| `wordpress-embed.html` | WordPress iframe kodu ve otomatik yükseklik seçeneği |

### Yeni şehir ekleme

Mevcut bir sorunun verisini `questions.json` içinde doğrudan düzenleyebilirsin. Örneğin şehir adını, bölgesini, ipucunu veya açıklamasını değiştirip çalıştır:

```bash
python3 build.py
```

Her soru kaydında şu alanlar bulunur:

```json
{
  "id": "city-01",
  "city": "İstanbul",
  "region": "Marmara",
  "landmark": "Galata Kulesi",
  "hint": "Tarihî taş kule, Haliç'e yakın bir semtte yükselir.",
  "fact": "Galata Kulesi İstanbul'un simge yapılarındandır.",
  "illustration": "<svg>...</svg>"
}
```

Başlangıç sorularındaki SVG illüstrasyonlar da doğrudan `questions.json` içindedir. Soru bankasını 81 ile genişletebilir veya fotoğraf modunu daha sonra ayrı bir soru kaynağı olarak ekleyebilirsin.

## Test

Oyunu `index.html` üzerinden açıp 10 soruluk bir tur tamamlayarak ipucu, zamanlayıcı, sonuç ekranı ve mobil yerleşimi doğrulayabilirsin. İlk sürüm masaüstü ve mobil tarayıcı akışlarında sınandı.

## Coğrafi bilgi ve görsel notu

Bu oyun **gerçek yapı fotoğrafları değil, simgeleri anlatan çizimler** kullanır. Çizimler şematik ve stilizedir; mimari yapıların ölçekli ve birebir tasviri değildir. Kaynakça ve çapraz kontrol için:

- [T.C. Kültür ve Turizm Bakanlığı — UNESCO Dünya Mirası Listesinde Türkiye](https://dosim.ktb.gov.tr/TR-218145/unesco-dunya-miras-listesinde-turkiye.html)
- [Türkiye Kültür Portalı](https://www.kulturportali.gov.tr/)
- [Sümela Manastırı — Türkiye Müzeleri](https://muze.gov.tr/muze-detay?DistId=MRK&SectionId=SML01)

Yayın öncesinde şehir açıklamalarını düzenli gözden geçirmek, özellikle yeni eklenen soruların şehirle ilişkisini doğrulamak iyi olur.
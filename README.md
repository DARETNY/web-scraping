# Web Scraping Projesi

Bu proje, `okul.com.tr` ve `mebbis.meb.gov.tr` sitelerinden veri çekerek, bu verileri normalize edip karşılaştıran bir **web scraping** projesidir. Proje, eksik kurumları tespit edip sonuçları CSV dosyası olarak kaydeder.

![Proje Önizleme](./present/output.gif)

---

## 🚀 Özellikler

✅ `okul.com.tr` ve `mebbis.meb.gov.tr` sitelerinden veri çekme  
✅ Verileri normalize ederek ortak bir formatta saklama  
✅ Eksik kurumları tespit etme ve CSV olarak kaydetme  
✅ Kolay kurulum ve kullanım  

---

## 📋 Gereksinimler

- **Python 3.7+**
- **Playwright** (Web scraping için)
- **Pandas** (Veri işleme için)
- **asyncio** (Asenkron işlemler için)

---

## 🔧 Kurulum

1. **Gerekli Python paketlerini yükleyin**:
    ```sh
    pip install pandas playwright asyncio
    ```

2. **Playwright’i kurun**:
    ```sh
    playwright install
    ```

---

## 🎯 Kullanım

1. **Verileri çekmek ve karşılaştırmak için `tf.py` dosyasını çalıştırın**:
    ```sh
    python tf.py
    ```

2. **Çalıştırma sonucunda aşağıdaki CSV dosyaları `result/` klasöründe oluşacaktır**:
    - 📂 `okul_verileri.csv`
    - 📂 `meb_verileri.csv`
    - 📂 `eksik_kurumlar.csv`

---

## 📂 Proje Dosyaları

| Dosya | Açıklama |
|--------|----------|
| `tf.py` | Ana çalışma dosyası. Scraper'ları çalıştırır, verileri karşılaştırır. |
| `OkulScarping.py` | `okul.com.tr` sitesinden veri çeken sınıf. |
| `MebScarping.py` | `mebbis.meb.gov.tr` sitesinden veri çeken sınıf. |
| `result/eksik_kurumlar.csv` | Eksik kurumları içeren sonuç dosyası. |

---


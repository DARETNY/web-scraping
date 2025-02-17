# Web Scraping Projesi

Bu proje, `okul.com.tr` ve `mebbis.meb.gov.tr` sitelerinden veri çekerek, bu verileri normalize edip karşılaştıran bir web scraping projesidir. Proje, eksik kurumları tespit edip sonuçları CSV dosyası olarak kaydeder.

<img alt="output.gif" height="400" src="presnt%2Foutput.gif" title="proje önizleme" width="400"/>

## Gereksinimler

- Python 3.7+
- Pandas
- Playwright
- asyncio

## Kurulum

1. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install pandas playwright asyncio
    ```

2. Playwright'i kurun:
    ```sh
    playwright install
    ```

## Kullanım

1. `tf.py` dosyasını çalıştırarak verileri çekin ve karşılaştırın:
    ```sh
    python tf.py
    ```

2. Çalıştırma sonucunda `result` klasöründe aşağıdaki dosyalar oluşturulacaktır:
    - `okul_verileri.csv`
    - `meb_verileri.csv`
    - `eksik_kurumlar.csv`

## Dosya Açıklamaları

- `tf.py`: Ana dosya. `OkulPageScraper` ve `MebPageScraper` sınıflarını kullanarak verileri çeker, normalize eder ve karşılaştırır.
- `OkulScarping.py`: `okul.com.tr` sitesinden veri çeken sınıfı içerir.
- `MebScarping.py`: `mebbis.meb.gov.tr` sitesinden veri çeken sınıfı içerir.
- `result/eksik_kurumlar.csv`: `okul.com.tr` ve `mebbis.meb.gov.tr` verilerini karşılaştırarak eksik olan kurumları listeler.

## Örnek Çıktı

`tf.py` dosyasını çalıştırdıktan sonra konsolda aşağıdaki gibi bir çıktı göreceksiniz:
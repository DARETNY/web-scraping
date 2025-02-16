from playwright.async_api import async_playwright
import asyncio
import pandas as pd  # Pandas'ı ekledik


class MebPageScraper:
    def __init__(self, browser_path: str, url: str, row_number: int = 5):
        self.browser_path = browser_path
        self.url = url
        self.row_number = row_number

    async def fetch_page_content(self):
        async with async_playwright() as p:
            try:
                print("🔹 Edge tarayıcısı başlatılıyor...")
                browser = await p.chromium.launch(executable_path=self.browser_path, headless=False)
                page = await browser.new_page()

                print("🔹 Sayfa açılıyor...")
                await page.goto(self.url, timeout=120000)
                await asyncio.sleep(1)

                print("🔹 Kurum türü seçiliyor...")
                await page.fill('input#cmbKurumTuru_I', 'Özel Kurumlar')
                await asyncio.sleep(1)

                print("🔹 İstanbul seçiliyor...")
                await page.click('input#cmbil_I')
                await asyncio.sleep(1)

                await page.evaluate("""
                    const inputElement = document.querySelector('input[name="cmbil"]');
                    inputElement.value = 'İSTANBUL';
                    const event = new Event('change');
                    inputElement.dispatchEvent(event);
                """)
                await asyncio.sleep(1)

                print("🔹 Kurum listeleme butonuna tıklanıyor...")
                await page.evaluate("document.querySelector('#btnKurumListelex_I').click()")
                await asyncio.sleep(5)  # Ekstra bekleme süresi ekledik

                print("🔹 Sayfa yükleniyor, lütfen bekleyin...")
                await page.wait_for_load_state('networkidle', timeout=180000)

                print("✅ Kurum listesini çekiyorum...")
                await asyncio.sleep(3)  # Ekstra bekleme (sayfanın tüm içeriğinin yüklenmesi için)

                rows = await page.query_selector_all("tr.dxgvDataRow_DevEx")
                print(f"✅ Bulunan satır sayısı: {len(rows)}")

                if not rows:
                    print("❌ HATA: Hiç satır bulunamadı!")
                    await browser.close()
                    return pd.DataFrame()

                kurumlar_listesi = []

                for i, row in enumerate(rows[:self.row_number]):
                    cells = await row.query_selector_all("td")

                    if not cells:
                        print(f"❌ HATA: Satır {i} içinde hiç <td> yok!")
                        continue

                    row_data = [await cell.evaluate("node => node.textContent.trim()") for cell in cells]

                    # İlk boş hücreyi satır numarasıyla doldur
                    row_data[0] = i + 1

                    kurumlar_listesi.append(row_data)
                    print(f"✅ Satır {i} Verileri: {row_data}")

                await browser.close()

                # Sütun adlarını güncelleyelim: Her satır için benzersiz bir ID (1, 2, 3...) ekle
                columns = ["ID", "İl", "İlçe", "Kurum Adı", "Kurum Türü", "Adres", "Telefon 1", "Telefon 2",
                           "Kurum Kodu", "Web Sitesi"]

                # Verileri DataFrame'e ekleyelim
                df = pd.DataFrame(kurumlar_listesi, columns=columns)

                return df

            except Exception as e:
                print(f"❌ Bir hata oluştu: {e}")
                return pd.DataFrame()


async def main():
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url = "https://mebbis.meb.gov.tr/kurumlistesi.aspx"

    scraper = MebPageScraper(browser_path, url)
    df_kurumlar = await scraper.fetch_page_content()

    if not df_kurumlar.empty:
        print("\n🔹 İlk 5 Kurum:")
        print(df_kurumlar)

        # CSV olarak kaydetmek istersen:
        df_kurumlar.to_csv("kurumlar_listesi.csv", index=False, encoding="utf-8-sig")



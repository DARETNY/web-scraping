import pandas as pd
from playwright.async_api import async_playwright


class OkulPageScraper:
    def __init__(self, browser_path: str, base_url: str, start_page: int, end_page: int):
        self.browser_path = browser_path
        self.base_url = base_url
        self.start_page = start_page
        self.end_page = end_page

    async def fetch_page_content(self, page_number: int):
        async with async_playwright() as p:
            try:
                url = f"{self.base_url}&page={page_number}"
                print(f"🔹 Sayfa {page_number} açılıyor...")
                browser = await p.chromium.launch(executable_path=self.browser_path, headless=False)
                page = await browser.new_page()

                print(f"🔹 Sayfa {page_number} yükleniyor, lütfen bekleyin...")
                await page.goto(url, timeout=120000)
                await page.wait_for_load_state('networkidle', timeout=120000)

                content_divs = await page.query_selector_all('div.col-md-12 div.content')

                if not content_divs:
                    print(f"❌ Sayfa {page_number}: İçerik bulunamadı!")
                    await browser.close()
                    return []

                okul_bilgileri = []

                for i, content_div in enumerate(content_divs):
                    is_visible = await content_div.is_visible()
                    if not is_visible:
                        continue

                    okul_adi_elem = await content_div.query_selector('span.three-dots')
                    okul_adi = await okul_adi_elem.inner_text() if okul_adi_elem else "Bilinmiyor"

                    ilce_elem = await content_div.query_selector('a.fc-2.address')
                    ilce = await ilce_elem.inner_text() if ilce_elem else "Bilinmiyor"

                    okul_aciklama_elem = await content_div.query_selector('q.fc-18')
                    okul_aciklama = await okul_aciklama_elem.inner_text() if okul_aciklama_elem else "Bilinmiyor"

                    okul_saatleri_elem = await content_div.query_selector('span.fs-14.f-wei-6')
                    okul_saatleri = await okul_saatleri_elem.inner_text() if okul_saatleri_elem else "Bilinmiyor"

                    okul_fiyati_elem = await content_div.query_selector('a.fs-14.fc-13.f-wei-6')
                    okul_fiyati = await okul_fiyati_elem.inner_text() if okul_fiyati_elem else "Bilinmiyor"

                    okul_bilgileri.append({
                        "id": f"sayfa {page_number}, içerik {i + 1}",
                        "il": "İstanbul",
                        "ilçe": ilce.strip(),
                        "okul adı": okul_adi.strip(),
                        "okul açıklaması": okul_aciklama.strip(),
                        "okul saatleri": okul_saatleri.strip(),
                        "okul fiyatı": okul_fiyati.strip()
                    })

                await browser.close()
                return okul_bilgileri

            except Exception as e:
                print(f"❌ Sayfa {page_number}: Bir hata oluştu: {e}")
                return []

    async def fetch_all_pages(self):
        all_okul_bilgileri = []
        for page_number in range(self.start_page, self.end_page + 1):
            okul_bilgileri = await self.fetch_page_content(page_number)
            if okul_bilgileri:
                all_okul_bilgileri.extend(okul_bilgileri)
        return all_okul_bilgileri


async def main():
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    base_url = "https://okul.com.tr/lise/istanbul?sector=ozel"

    start_page = 1
    end_page = 3

    scraper = OkulPageScraper(browser_path, base_url, start_page, end_page)
    all_okul_bilgileri = await scraper.fetch_all_pages()

    if all_okul_bilgileri:
        print("\n🔹 Tüm Okul Bilgileri:")
        for okul in all_okul_bilgileri:
            print(okul)

        df = pd.DataFrame(all_okul_bilgileri,
                          columns=["id", "il", "ilçe", "okul adı", "okul açıklaması", "okul saatleri", "okul fiyatı"])

        df.to_csv('okul_bilgileri.csv', index=False, encoding='utf-8')
        print("\n🔹 Okul bilgileri 'okul_bilgileri.csv' olarak kaydedildi.")

# asyncio.run(main())

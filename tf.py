import pandas as pd
import asyncio
from OkulScarping import OkulPageScraper
from MebScarping import MebPageScraper
import os


class CombinedScraper:
    def __init__(self, browser_path: str):
        self.browser_path = browser_path

    async def run_okul_scraper(self, base_url: str, start_page: int, end_page: int) -> pd.DataFrame:
        """Okul.com.tr verilerini çeker"""
        scraper = OkulPageScraper(self.browser_path, base_url, start_page, end_page)
        data = await scraper.fetch_all_pages()
        return pd.DataFrame(data)

    async def run_meb_scraper(self, url: str, row_number: int = 100) -> pd.DataFrame:
        """MEB verilerini çeker"""
        scraper = MebPageScraper(self.browser_path, url, row_number)
        return await scraper.fetch_page_content()

    @staticmethod
    def normalize_data(df: pd.DataFrame, source: str) -> pd.DataFrame:
        """Okul ve MEB verilerini normalize eder (büyük harf yapar, gereksiz karakterleri temizler)."""
        df = df.copy()
        if source == "okul":
            df["ilçe"] = df["ilçe"].str.split("/").str[0].str.strip().str.upper()
            df["okul adı"] = df["okul adı"].str.upper().str.replace(r"[^A-ZĞÜŞİÖÇ ]", "", regex=True)
        elif source == "meb":
            df["İlçe"] = df["İlçe"].str.upper().str.strip()
            df["Kurum Adı"] = df["Kurum Adı"].str.upper().str.replace(r"[^A-ZĞÜŞİÖÇ ]", "", regex=True)
        return df

    @staticmethod
    def compare_data(okul_df: pd.DataFrame, meb_df: pd.DataFrame) -> pd.DataFrame:
        """MEB ve Okul verilerini karşılaştırarak eksik olanları çıkarır."""
        # Veriyi temizle
        okul_df = CombinedScraper.normalize_data(okul_df, "okul")
        meb_df = CombinedScraper.normalize_data(meb_df, "meb")

        # Merge işlemi (karşılaştırma)
        merged = pd.merge(
            meb_df,
            okul_df,
            left_on=["İlçe", "Kurum Adı"],
            right_on=["ilçe", "okul adı"],
            how="left",
            indicator=True  # Hangi satırın nerede olduğunu belirle
        )

        # Sadece MEB'de olup okul.com'da olmayanları filtrele
        missing_in_okul = merged[merged["_merge"] == "left_only"]

        # İlgili sütunları seç
        result_df = missing_in_okul[[
            "Kurum Adı", "İlçe", "Kurum Türü", "Adres", "Telefon 1", "Web Sitesi"
        ]]

        return result_df


async def main():
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    # Scraper'ları başlat
    combined = CombinedScraper(browser_path)

    # Verileri çek
    okul_df, meb_df = await asyncio.gather(
        combined.run_okul_scraper(
            base_url="https://okul.com.tr/lise/istanbul?sector=ozel",
            start_page=1,
            end_page=3
        ),
        combined.run_meb_scraper(url="https://mebbis.meb.gov.tr/kurumlistesi.aspx")
    )
    comparison_df = CombinedScraper.compare_data(okul_df, meb_df)
    if not os.path.exists("result"):
        os.makedirs("result")
    # Sonuçları kaydet
    okul_df.to_csv("result/okul_verileri.csv", index=False, encoding="utf-8-sig")
    meb_df.to_csv("result/meb_verileri.csv", index=False, encoding="utf-8-sig")
    comparison_df.to_csv("result/eksik_kurumlar.csv", index=False, encoding="utf-8-sig")

    print(f"\n✅ {len(comparison_df)} adet eksik okul bulundu ve 'eksik_kurumlar.csv' olarak kaydedildi.")


if __name__ == "__main__":
    asyncio.run(main())

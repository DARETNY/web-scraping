import pytest
import pandas as pd
from MebScarping import MebPageScraper

@pytest.mark.asyncio
async def test_fetch_page_content():
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url = "https://mebbis.meb.gov.tr/kurumlistesi.aspx"
    scraper = MebPageScraper(browser_path, url, row_number=5)
    
    df = await scraper.fetch_page_content()
    
    assert isinstance(df, pd.DataFrame), "The result should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
    assert set(df.columns) == {"ID", "İl", "İlçe", "Kurum Adı", "Kurum Türü", "Adres", "Telefon 1", "Telefon 2", "Kurum Kodu", "Web Sitesi"}, "DataFrame columns do not match expected columns"

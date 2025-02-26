import pytest
import pandas as pd
from OkulScarping import OkulPageScraper

@pytest.mark.asyncio
async def test_fetch_page_content():
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    base_url = "https://okul.com.tr/lise/istanbul?sector=ozel"
    page_number = 1
    scraper = OkulPageScraper(browser_path, base_url, start_page=1, end_page=3)
    
    data = await scraper.fetch_page_content(page_number)
    
    assert isinstance(data, list), "The result should be a list"
    assert len(data) > 0, "The list should not be empty"
    assert set(data[0].keys()) == {"id", "il", "ilçe", "okul adı", "okul açıklaması", "okul saatleri", "okul fiyatı"}, "Data keys do not match expected keys"

from wikibot import scrape

def test_scrape():
    assert "Wikipedia" in scrape["Wikipedia"]
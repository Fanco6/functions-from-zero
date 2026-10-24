from unittest.mock import patch, MagicMock
from wikibot import scrape

@patch('wikipediaapi.Wikipedia')
def test_scrape(mock_wikipedia):
    # Setup mock behavior
    mock_instance = mock_wikipedia.return_value
    mock_page = MagicMock()
    mock_page.exists.return_value = True
    mock_page.summary = "Wikipedia is a free-content online encyclopedia."
    mock_instance.page.return_value = mock_page

    # Call the function correctly with parentheses ()
    assert "Wikipedia" in scrape("Wikipedia")

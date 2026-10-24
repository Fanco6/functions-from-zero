from unittest.mock import patch, MagicMock
from wikibot import scrape


@patch("wikipediaapi.Wikipedia")
def test_scrape_success(mock_wikipedia):
    # Setup mock behaviors for a successful page find
    mock_instance = mock_wikipedia.return_value
    mock_page = MagicMock()

    mock_page.exists.return_value = True
    mock_page.summary = "Sentence one. Sentence two. Sentence three. Sentence four."
    mock_instance.page.return_value = mock_page

    # Run the function with a constraint of 2 sentences
    result = scrape("Microsoft", max_sentences=2)

    # Assertions
    assert result == "Sentence one. Sentence two."
    mock_instance.page.assert_called_once_with("Microsoft")


@patch("wikipediaapi.Wikipedia")
def test_scrape_page_not_found(mock_wikipedia):
    # Setup mock behaviors for a missing page
    mock_instance = mock_wikipedia.return_value
    mock_page = MagicMock()

    mock_page.exists.return_value = False
    mock_instance.page.return_value = mock_page

    # Run the function
    result = scrape("FakePage123")

    # Assertions
    assert result == "Page 'FakePage123' not found."

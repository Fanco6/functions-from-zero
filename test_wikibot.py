from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from wikibot import scrape


@patch("wikipediaapi.Wikipedia")
def test_scrape_success(mock_wikipedia):
    # Setup mock behaviors for a successful page find
    mock_instance = mock_wikipedia.return_value
    mock_page = MagicMock()
    mock_page.exists.return_value = True
    mock_page.summary = "Sentence one. Sentence two. Sentence three. Sentence four."
    mock_instance.page.return_value = mock_page

    # Use CliRunner to invoke the click command with arguments
    runner = CliRunner()
    result = runner.invoke(scrape, ["--name", "Microsoft", "--max-sentences", "2"])

    # Assertions on terminal output instead of direct function return
    assert result.exit_code == 0
    assert "Sentence one. Sentence two." in result.output
    mock_instance.page.assert_called_once_with("Microsoft")


@patch("wikipediaapi.Wikipedia")
def test_scrape_page_not_found(mock_wikipedia):
    # Setup mock behaviors for a missing page
    mock_instance = mock_wikipedia.return_value
    mock_page = MagicMock()
    mock_page.exists.return_value = False
    mock_instance.page.return_value = mock_page

    # Use CliRunner to invoke the click command
    runner = CliRunner()
    result = runner.invoke(scrape, ["--name", "FakePage123"])

    assert result.exit_code == 0
    assert "Page 'FakePage123' not found." in result.output

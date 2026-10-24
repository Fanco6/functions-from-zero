import wikipediaapi


def scrape(name, max_sentences=2):
    wiki = wikipediaapi.Wikipedia(
        user_agent="MyWikiScraperBot/1.0 (contact@example.com)", language="en"
    )

    page = wiki.page(name)

    if page.exists():
        # Split the text by periods, take the first few elements, and rejoin them
        sentences = page.summary.split(". ")
        short_summary = ". ".join(sentences[:max_sentences])
        return short_summary + "."
    else:
        return f"Page '{name}' not found."


# Call it with a constraint
print(scrape("Wikipedia", max_sentences=2))

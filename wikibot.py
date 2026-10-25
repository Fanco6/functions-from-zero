import click
import wikipediaapi


@click.command()
@click.option(
    "--name",
    prompt="Enter Wikipedia topic",
    help="The person or topic to search on Wikipedia.",
)
@click.option("--max-sentences", default=2, help="Number of sentences for the summary.")
def scrape(name, max_sentences):
    # FIX: Pass the language directly as a string "en"
    wiki = wikipediaapi.Wikipedia(
        user_agent="MyWikiScraperBot/1.0 (contact@example.com)", language="en"
    )

    click.echo(click.style("Searching for topic...", fg="blue"), color=True)

    page = wiki.page(name)

    if page.exists():
        sentences = page.summary.split(". ")
        short_summary = ". ".join(sentences[:max_sentences])

        if not short_summary.endswith("."):
            short_summary += "."

        click.echo(short_summary)
    else:
        click.echo(click.style(f"Page '{name}' not found.", fg="red"), color=True)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    scrape()

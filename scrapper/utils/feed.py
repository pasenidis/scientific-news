from newspaper import Article


def parse_link(url):
    """Parses an article from a given link.

    Keyword arguments:
    url -- the url (protocol must be included) (no default)
    """
    a = Article(url)

    a.download()
    a.parse()

    return {
        'name': a.title,
        'text': a.text,
        'top_image': a.top_image,
        'author': a.authors,
        'source': a.source_url
    }

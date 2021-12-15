"""
Find news from Google News using the RSS feed.
"""

from datetime import date
from urllib.parse import quote
from urllib.request import urlopen
from xml.etree import ElementTree


# The feed URL.
FEED_URL = "https://news.google.com/rss/search"

# The ISO language and country code.
LANGUAGE = "en"
COUNTRY = "US"

# The default parameters for the Google News feed.
FEED_PARAMETERS = {
    "hl": LANGUAGE + "-" + COUNTRY,
    "gl": COUNTRY,
    "ceid": COUNTRY + ":" + LANGUAGE,
}


def get_feed_query(query: str, after: date = None, before: date = None) -> str:
    """
    Construct a Google News feed query from a query string and before and after dates.

    This feed query is escaped to be URL compatible.
    """

    if after is not None:
        query += " after:" + str(after)

    if before is not None:
        query += " before:" + str(before)

    return quote(query)


def get_feed_url(query) -> str:
    """
    Construct a Google News feed URL from a query.
    """

    url = FEED_URL

    parameters = {
        "q": query,
        **FEED_PARAMETERS,
    }

    # Add all of the parameters to the URL.
    url += "?"

    for key, value in parameters.items():
        url += key + "=" + value + "&"

    url = url.rstrip("&")

    return url


def get_feed_xml_tree(url: str) -> ElementTree:
    """
    Open a feed URL and parse the XML into a Python XML element tree.
    """

    with urlopen(url) as file:
        xml = file.read().decode("utf-8")

    xml_tree = ElementTree.fromstring(xml)

    return xml_tree


def get_feed_titles(
    after: date = None,
    before: date = None,
    query: str = "climate change",
) -> list[str]:
    """
    Find the titles of the Google News articles between two dates.
    """

    # TODO: Use the climate change topic built into Google News.

    query = get_feed_query(query, after, before)
    url = get_feed_url(query)
    tree = get_feed_xml_tree(url)
    channel = tree.find("channel")
    items = channel.iter("item")

    titles = []

    for item in items:
        titles.append(item.find("title").text)

    return titles

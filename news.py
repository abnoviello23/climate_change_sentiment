"""
Find news from Google News using the RSS feed.
"""

from datetime import date
from urllib.parse import quote
from urllib.request import urlopen
from xml.etree import ElementTree


# The feed URL.
FEED_URL = "https://news.google.com/rss"

# The ISO language and country code.
LANGUAGE = "en"
COUNTRY = "US"

# The default parameters for the Google News feed.
FEED_PARAMETERS = {
    "hl": LANGUAGE + "-" + COUNTRY,
    "gl": COUNTRY,
    "ceid": COUNTRY + ":" + LANGUAGE,
}


def feed_query(query: str, after: date = None, before: date = None) -> str:
    if after is not None:
        query += " after:" + str(after)

    if before is not None:
        query += " before:" + str(before)

    return quote(query)


def feed_url(query) -> str:
    url = FEED_URL

    parameters = {
        "q": query,
        **FEED_PARAMETERS,
    }

    # Add all of the parameters to the URL.
    url += "?"

    for key, value in parameters.items():
        url += key + "=" + value + "&"

    return url

def feed_xml_tree(url: str) -> ElementTree:
    with urlopen(url) as file:
        xml = file.read().decode("utf-8")

    xml_tree = ElementTree.fromstring(xml)

    return xml_tree

def feed_climate_change_titles(after: date = None, before: date = None) -> list[str]:
    query = feed_query("climate change", after, before)
    url = feed_url(query)
    tree = feed_xml_tree(url)
    channel = tree.find("channel")
    items = channel.iter("item")

    titles = []

    for item in items:
        titles.append(item.find("title").text)

    return titles

print(feed_climate_change_titles(date(2020, 10, 1), date(2020, 10, 31)))

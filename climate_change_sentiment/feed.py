"""
Find news from Google News using the RSS feed.
"""

import datetime
import urllib.parse
import urllib.request
import xml.etree.ElementTree

# The feed URL.
FEED_URL = "https://news.google.com/rss/search"


def get_feed_query(
    query: str,
    after: datetime.date = None,
    before: datetime.date = None,
) -> str:
    """
    Construct a Google News feed query from a query string and before and after dates.

    This feed query is escaped to be URL compatible.
    """

    if after is not None:
        query += " after:" + str(after)

    if before is not None:
        query += " before:" + str(before)

    return urllib.parse.quote(query)


def get_feed_url(query) -> str:
    """
    Construct a Google News feed URL from a query.
    """

    url = FEED_URL

    parameters = {
        "q": query,
    }

    # Add all of the parameters to the URL.
    url += "?"

    for key, value in parameters.items():
        url += key + "=" + value + "&"

    url = url.rstrip("&")

    return url


def get_feed_xml_tree(url: str) -> xml.etree.ElementTree:
    """
    Open a feed URL and parse the XML into a Python XML element tree.
    """

    with urllib.request.urlopen(url) as file:
        feed_xml = file.read().decode("utf-8")

    xml_tree = xml.etree.ElementTree.fromstring(feed_xml)

    return xml_tree


def get_feed_titles(
    query: str,
    after: datetime.date = None,
    before: datetime.date = None,
) -> list[str]:
    """
    Find the titles of the Google News articles between two dates.
    """

    query = get_feed_query(query, after, before)
    url = get_feed_url(query)
    tree = get_feed_xml_tree(url)
    channel = tree.find("channel")
    items = channel.iter("item")

    titles = []

    for item in items:
        titles.append(item.find("title").text)

    return titles

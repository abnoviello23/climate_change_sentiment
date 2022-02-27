"""
Load the volume and title for various queries.
"""

import pathlib

from climate_change_sentiment.volume import load_volume


DATA_PATH = pathlib.Path("data")

CLIMATE_CHANGE_QUERY = "climate change"

NATURAL_DISASTER_QUERIES = [
    "natural disaster",
    "cyclone",
    "hurricane",
    "tornado",
    "wildfire",
    "flood",
    "tsunami",
    "drought",
]


def get_query_path(query: str, suffix: str) -> pathlib.Path:
    """
    Get the path for the CSV file for a query.

    The suffix should be either "volume" or "titles."
    """

    # Format the query for file and folder names.
    query = query.lower().replace(" ", "_")

    # The filename for storing the query.
    query_filename = query + "_" + suffix + ".csv"

    return DATA_PATH / query_filename


load_volume(
    CLIMATE_CHANGE_QUERY,
    volume_path=get_query_path(CLIMATE_CHANGE_QUERY, suffix="volume"),
    titles_path=get_query_path(CLIMATE_CHANGE_QUERY, suffix="titles"),
)


for natural_disaster_query in NATURAL_DISASTER_QUERIES:
    load_volume(
        natural_disaster_query,
        volume_path=get_query_path(natural_disaster_query, suffix="volume"),
    )

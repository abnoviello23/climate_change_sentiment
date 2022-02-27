"""
Determine the volume of climate change articles for specific days.
"""

import csv
import datetime

import matplotlib

import climate_change_sentiment
import climate_change_sentiment.helpers
import climate_change_sentiment.feed

# Find a list of dates between the start of 2020 and today.
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

dates = climate_change_sentiment.helpers.get_date_range(start_date, end_date)


def load_volume() -> None:
    """
    Determine the volume of articles for each day.
    """

    with open(
        climate_change_sentiment.VOLUME_FILENAME,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Volume"])

    for date in dates:
        volume = len(
            climate_change_sentiment.feed.get_feed_titles(
                date, date + datetime.timedelta(days=1)
            )
        )

        with open(
            climate_change_sentiment.VOLUME_FILENAME,
            "a",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow([str(date), volume])

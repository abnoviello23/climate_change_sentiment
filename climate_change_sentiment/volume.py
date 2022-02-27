"""
Determine the volume of climate change articles for specific days.
"""

import csv
import pathlib
import datetime

import climate_change_sentiment
import climate_change_sentiment.helpers
import climate_change_sentiment.feed

# Find a list of dates between the start of 2020 and today.
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

dates = climate_change_sentiment.helpers.get_date_range(start_date, end_date)


def load_volume(
    query: str,
    volume_path: pathlib.Path = None,
    titles_path: pathlib.Path = None,
) -> None:
    """
    Determine the volume of articles for each day.
    """

    if volume_path:
        with volume_path.open("w") as file:
            writer = csv.writer(file)

            writer.writerow(["Date", "Volume"])

    if titles_path:
        with titles_path.open("w") as file:
            writer = csv.writer(file)

            writer.writerow(["Date", "Title"])

    for date in dates:
        titles = climate_change_sentiment.feed.get_feed_titles(
            query, date, date + datetime.timedelta(days=1)
        )

        volume = len(titles)

        if volume_path:
            with volume_path.open("w") as file:
                writer = csv.writer(file)

                writer.writerow([str(date), volume])

        if titles_path:
            with titles_path.open("w") as file:
                writer = csv.writer(file)

                for title in titles:
                    writer.writerow([str(date), title])

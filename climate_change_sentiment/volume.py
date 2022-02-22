"""
Determine the volume of climate change articles for specific days.
"""

import csv
import datetime

import matplotlib

from news import VOLUME_FILENAME
from news.feed import feed_titles
from news.helpers import date_range

# Find a list of dates between the start of 2020 and today.
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

dates = date_range(start_date, end_date)


def load_volume() -> None:
    """
    Determine the volume of articles for each day.
    """

    with open(VOLUME_FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Volume"])

    for date in dates:
        volume = len(feed_titles(date, date + datetime.timedelta(days=1)))

        with open(VOLUME_FILENAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([str(date), volume])
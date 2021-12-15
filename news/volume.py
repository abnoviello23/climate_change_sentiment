"""
Determine the volume of climate change articles for specific days.
"""

import csv
import datetime

from news import VOLUME_FILENAME
from news.crawler import get_feed_climate_change_titles


# Find a list of dates between the start of 2010 and today.
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

dates = [start_date]

while dates[-1] < end_date:
    dates.append(dates[-1] + datetime.timedelta(days=1))


def get_volume():
    """
    Determine the volume of articles for each day.
    """

    with open(VOLUME_FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Volume"])

    for date in dates:
        volume = len(
            get_feed_climate_change_titles(date, date + datetime.timedelta(days=1))
        )

        with open(VOLUME_FILENAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([str(date), volume])

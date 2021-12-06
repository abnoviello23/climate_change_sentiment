"""
Determine the volume of climate change articles for specific days.
"""

import csv
import datetime

from news.crawler import get_feed_climate_change_titles


ARTICLES_FILE = "articles.csv"

# Find a list of dates between the start of 2010 and today.
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

dates = [start_date]

while dates[-1] < end_date:
    dates.append(dates[-1] + datetime.timedelta(days=1))


def get_articles():
    """
    Determine the volume of articles for each day.
    """

    with open(ARTICLES_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Articles"])

    for date in dates:
        articles = len(
            get_feed_climate_change_titles(date, date + datetime.timedelta(days=1))
        )

        with open(ARTICLES_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([str(date), articles])

"""
Gather the article titles surrounding the date of a hurricane.
"""

import os
import csv
import datetime

from news import HURRICANES_FILE_NAME, HURRICANES_FOLDER_NAME
from news.helpers import get_date_range
from news.feed import get_feed_titles


# Only use hurricanes from 2020 onward.
MINIMUM_HURRICANE_DATE = datetime.date(2020, 1, 1)


def get_hurricanes():
    """
    Get all the hurricanes from the CSV file.
    """

    hurricanes = []

    with open(HURRICANES_FILE_NAME, newline="", encoding="utf-8") as file:
        all_hurricanes = list(csv.DictReader(file))

    for hurricane in all_hurricanes:
        date = datetime.datetime.strptime(hurricane["Date"], "%Y-%m-%d").date()

        if date > MINIMUM_HURRICANE_DATE:
            hurricanes.append(hurricane)

    return hurricanes


def get_hurricane_feed_titles(hurricane: dict):
    """
    Get the article titles around the date of one hurricane.

    The `hurricane` argument should be a dictionary
    from the list returned by `get_hurricanes()`.
    """

    # The folder to store data for the hurricane in.
    folder_name = os.path.join(
        HURRICANES_FOLDER_NAME,
        hurricane["Name"] + "-" + hurricane["Date"],
    )

    os.makedirs(folder_name, exist_ok=True)

    # The file with the feed titles.
    feed_titles_file_name = os.path.join(folder_name, "titles.csv")

    if os.path.exists(feed_titles_file_name):
        raise RuntimeError(
            "The feed titles file for Hurricane {} ({}) already exists.".format(
                hurricane["Name"], hurricane["Date"]
            )
        )

    with open(feed_titles_file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Title", "Date"])

    # The hurricane formation date.
    date = datetime.datetime.strptime(hurricane["Date"], "%Y-%m-%d").date()

    # The database dates are the dates of hurricane formation.
    # Hurricanes usually dissipate one week to one month after formation.
    # So, the date range is from 25 days before to 75 days after.
    start_date = date - datetime.timedelta(days=25)
    end_date = date + datetime.timedelta(days=75)

    dates = get_date_range(start_date, end_date)

    # Load and save the feed titles for each day.
    for date in dates:
        feed_titles = get_feed_titles(date, date + datetime.timedelta(days=1))

        with open(feed_titles_file_name, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            for title in feed_titles:
                writer.writerow([title, str(date)])

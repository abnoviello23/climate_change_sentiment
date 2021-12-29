"""
Helper functions for processing the news article data.
"""

import datetime


def date_range(start: datetime.date, stop: datetime.date) -> list:
    """
    Return the list of dates between the `start` and `stop` dates.
    """

    if not start <= stop:
        raise RuntimeError("The start date must be before the end date.")

    date_range = [start]

    next_date = start + datetime.timedelta(days=1)

    while next_date < stop:
        date_range.append(next_date)

        next_date += datetime.timedelta(days=1)

    return date_range

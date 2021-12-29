"""
Helper functions for processing the news article data.
"""

import datetime


def date_range(start: datetime.date, end: datetime.date) -> list:
    """
    Return the list of dates between a start and end date.

    Unlike the `range` function, this range is inclusive.
    """

    date_range = [start]

    while date_range[-1] < end:
        date_range.append(date_range[-1] + datetime.timedelta(days=1))

    return date_range

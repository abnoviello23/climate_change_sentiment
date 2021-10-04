from dataclasses import dataclass
from datetime import datetime

import requests
from bs4 import BeautifulSoup


@dataclass
class Hurricane:
    name: str
    category: int
    date: datetime


def all_hurricanes():
    hurricanes = []

    website = "https://products.climate.ncsu.edu/weather/hurricanes/database/"

    # The years from 2010 to 2021, inclusive.
    years = range(2010, 2022)

    for year in years:
        page = requests.get(
            website,
            params={
                "search": "year",
                "yr": str(year),
            },
        )

        soup = BeautifulSoup(page.text, "html.parser")

        tables = soup.find_all("div", {"class": "hurrdb_storms_table"})

        rows = []

        for table in tables:
            rows += table.find_all("div", {"class": "hurrdb_storms_table_row0"})
            rows += table.find_all("div", {"class": "hurrdb_storms_table_row1"})

        for row in rows:
            cells = row.find_all("div", {"class": "hurrdb_storms_table_cell"})

            if "Hurricane" in cells[0].text:
                # See website link above for formatting details.
                hurricane = Hurricane(
                    name=cells[1].text,
                    category=int(cells[0].text[-2]),
                    date=datetime.strptime(cells[2].text, "%b %d, %Y"),
                )

                # Choose all category 3 and above hurricanes.
                if hurricane.category >= 3:
                    hurricanes.append(hurricane)

    return hurricanes


for hurricane in all_hurricanes():
    print(hurricane)

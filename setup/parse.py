import argparse
import datetime
from calendar import month

ETS_OFFSET = datetime.timedelta(hours=5)


def err(msg):
    print(msg)
    exit(1)


def parseargs():
    now = datetime.datetime.now(datetime.UTC) - ETS_OFFSET
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-y",
        choices=range(2015, now.year + 1 if now.month == 12 else now.year),
        type=int,
        dest="year",
    )
    parser.add_argument("-d", choices=range(1, 26), type=int, dest="day")

    args = parser.parse_args()

    day = int(args.day)
    year = int(args.year)

    if year == now.year and day > now.day:
        ready_at = datetime.datetime(year, 12, day, tzinfo=datetime.UTC) - ETS_OFFSET
        err(f"Requested challenge is not ready yet. Will be ready in {ready_at - now}")

    return day, year

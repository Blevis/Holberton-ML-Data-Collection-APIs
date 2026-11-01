#!/usr/bin/env python3
"""Module for retrieving a GitHub user's location."""
import sys
import requests
from datetime import datetime, timezone


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.get("location"))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset = int(response.headers.get("X-Ratelimit-Reset"))
        now = datetime.now(timezone.utc).timestamp()
        minutes = int((reset - now) / 60)
        print("Reset in {} min".format(minutes))

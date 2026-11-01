#!/usr/bin/env python3
"""Module for filtering starships by passenger capacity."""
import requests


def availableShips(passengerCount):
    """Return ships capable of carrying at least passengerCount passengers."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "").strip()

            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]

    return ships

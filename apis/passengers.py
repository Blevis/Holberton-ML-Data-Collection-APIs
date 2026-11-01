#!/usr/bin/env python3
"""
Module for finding starships based on passenger capacity.
"""
import requests


def availableShips(passengerCount):
    """
    Returns a list of ships capable of holding passengerCount passengers.
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)

        if response.status_code != 200:
            return ships

        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"]

            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]

    return ships

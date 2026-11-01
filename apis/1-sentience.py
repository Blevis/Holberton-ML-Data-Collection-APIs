#!/usr/bin/env python3
"""Module for finding home planets of sentient species."""
import requests


def sentientPlanets():
    """Return the home planets of all sentient species."""
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data["results"]:
            classification = species["classification"].lower()
            designation = species["designation"].lower()

            if classification == "sentient" or designation == "sentient":
                homeworld = species["homeworld"]

                if homeworld is not None:
                    planet_response = requests.get(homeworld)
                    planet_data = planet_response.json()
                    planets.append(planet_data["name"])

        url = data["next"]

    return planets

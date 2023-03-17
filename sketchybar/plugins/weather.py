#!/usr/bin/env python3

import configparser
import requests
import json
import os

polybar_config = configparser.ConfigParser()

"""
Code	Description
0	Clear sky
1, 2, 3	Mainly clear, partly cloudy, and overcast
45, 48	Fog and depositing rime fog
51, 53, 55	Drizzle: Light, moderate, and dense intensity
56, 57	Freezing Drizzle: Light and dense intensity
61, 63, 65	Rain: Slight, moderate and heavy intensity
66, 67	Freezing Rain: Light and heavy intensity
71, 73, 75	Snow fall: Slight, moderate, and heavy intensity
77	Snow grains
80, 81, 82	Rain showers: Slight, moderate, and violent
85, 86	Snow showers slight and heavy
95 *	Thunderstorm: Slight or moderate
96, 99 *	Thunderstorm with slight and heavy hail
"""

weathercode_selector = {
    0: "󰖙",  # Clear sky
    1: "󰖙",  # Mainly clear
    2: "󰖐",  # Partly cloudy
    3: "󰖐",  # Overcast
    45: "",  # Fog
    48: "",  # Fog
    51: "",  # Light drizzle
    53: "",  # Moderate drizzle
    55: "",  # Dense drizzle
    56: "",  # Light freezing drizzle
    57: "",  # Dense freezing drizzle
    61: "",  # Slight rain
    63: "",  # Moderate rain
    65: "",  # Heavy rain
    66: "",  # Light freezing rain
    67: "",  # Heavy freezing rain
    71: "󰖘",  # Light snow fall
    73: "󰖘",  # Moderate snow fall
    75: "󰖘",  # Heavy snow fall
    77: "󰖘",  # Snow grains ??
    80: "",  # Light rain showers
    81: "",  # Moderate rain showers
    82: "",  # Violent rain showers
    85: "",  # Light snow shower
    86: "",  # Moderate snow shower
    95: "󰖓",  # Thunderstorm
    96: "󰖓",  # Thunderstorm
    99: "󰖓",  # Thunderstorm
}


polybar_config.read(f"{os.environ['HOME']}/.config/polybar/config.ini")

active_color = polybar_config["colors"]["light-text"]

alert_color = polybar_config["colors"]["alert"]


try:
    r = requests.get("https://ipinfo.io")
    r_json = r.json()

    lat, long = r_json["loc"].split(",")
except:
    output = "%{u" + alert_color + "}%{+u}" + "  "

    print(output)
    exit()

URL = (
    "https://api.open-meteo.com/v1/forecast?"
    + f"latitude={lat}&longitude={long}"
    + "&hourly=temperature_2m,weathercode"
    + "&current_weather=true"
    + "&temperature_unit=fahrenheit"
    + "&windspeed_unit=mph"
    + "&precipitation_unit=inch"
    + "&timeformat=unixtime"
    + "&timezone=America%2FChicago"
)

try:
    r = requests.get(URL)
    r_json = r.json()

    temperature = r_json["current_weather"]["temperature"]
    weathercode = r_json["current_weather"]["weathercode"]
    weather_symbol = weathercode_selector[weathercode]

    output = (
        "%{F" + active_color + "}" + f" {weather_symbol} {temperature} F " + "%{F-}"
    )
except:
    output = "%{u" + alert_color + "}%{+u}" + " 󰅤 "

print(output)

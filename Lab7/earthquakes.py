# earthquakes.py
from pathlib import Path

import requests
from datetime import datetime, timezone, timedelta
import csv
import io
from matplotlib import pyplot as plt
import json

def get_earthquakes_csv_string(n: int, magnitude: float) -> str:
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=n)
    end_time_iso8601 = end_time.strftime('%Y-%m-%dT%H:%M:%S%z')
    start_time_iso8601 = start_time.strftime('%Y-%m-%dT%H:%M:%S%z')

    baseurl = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    headers = {'User-Agent': 'no.uib.ii.inf100.h24.lab7.nilau0421'}
    params = {
        'format': 'csv',
        'starttime': start_time_iso8601,  # ISO 8601 format
        'endtime': end_time_iso8601,  # ISO 8601 format
        'minmagnitude': magnitude,
        'orderby': 'magnitude',
        'limit': 5000,
    }

    response = requests.get(baseurl, params=params, headers=headers)
    content = response.content.decode('utf-8')
    return content

def get_earthquake_list(csv_string: str) -> list:
    reader = csv.DictReader(io.StringIO(csv_string))
    earthquakes = [
        (float(row['longitude']), float(row['latitude']), float(row['mag']))
        for row in reader
    ]
    return earthquakes

def plot_earthquakes(data_points: list) -> None:
    longitudes, latitudes, magnitudes = zip(*data_points)
    sizes = [3**magnitude/10 for magnitude in magnitudes]
    plt.scatter(longitudes, latitudes, s=sizes, alpha=0.2)
    # https://www.geeksforgeeks.org/zip-in-python/

def load_coastlines() -> list:
    coastline_data = json.loads(Path('ne_110m_coastline.json').read_text(encoding='utf-8'))
    coordinates = [island['geometry']['coordinates'] for island in coastline_data['features']]
    return coordinates

def plot_coastlines(coordinates: list) -> None:
    for coastline in coordinates:
        x, y = zip(*coastline)
        plt.plot(x, y, color='grey')


if __name__ == '__main__':
    s = get_earthquakes_csv_string(50, 4) # Del A
    l = get_earthquake_list(s) # Del B
    plt.figure(figsize=(12, 8)) # Del F
    plt.grid(True)
    plot_earthquakes(l) # Del C
    cl = load_coastlines() # Del D
    plot_coastlines(cl) # Del E

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'Earthquakes with magnitude >= 4.0 in the last 50 days')
    plt.show()

# best_lk

Where in Sri Lanka would you like to live? This project helps people compare
places across the island, starting with the weather. For example, you can
compare Kandy and Colombo over the same year to see which had more cool
days or a wetter monsoon.

A place profile pairs a name and coordinates (latitude, longitude) with
the previous 365 complete days in Sri Lanka. For each date it records the
mean air temperature (°C), total rainfall (mm), mean relative humidity (%),
and both mean and maximum dew point (°C). Relative humidity measures how close the air is to
saturation at its current temperature. A higher dew point means the air
contains more moisture.
Recent measurements can be missing while the weather archive catches up.
The data comes from [Open-Meteo’s Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api).

## Compare places on the map

From the repository root, run:

```sh
python3 -m pip install -r requirements.txt
PYTHONPATH=src python3 -m best_lk.Map
```

Compare [Sri Lanka’s 25 district capitals](images/weather-map.png) or
[20 locations in Greater Colombo](images/greater-colombo.png). The regional
sample lies within 40 km straight-line distance of the project's Colombo
city point (6.93° N, 79.86° E).

Each point shows the percentage of assessed daytime hours that suited a dry
walk in shade. We use hourly temperature, dew point and wind to estimate
thermal stress. An hour qualifies when the Universal Thermal Climate Index
is above 9 °C and at or below 26 °C, with less than 0.1 mm of rain.
The profile stores the qualifying and assessed hour counts for each day.
Nearby suburbs can share the same weather grid cell.
[Research, assumptions and scoring method](docs/outdoor-comfort.md)

Profiles are cached in `data/profiles/` as `<lat>_<lng>_<name>.json`,
for example `6.97_80.77_Nuwara Eliya.json`. Repeated runs on
the same Sri Lankan date reuse the saved data. The first run on a new date
refreshes each requested profile. The island outline comes from
[Natural Earth](https://www.naturalearthdata.com/).
The district capitals are listed by the [Sri Lanka Army](https://alt.army.lk/sfhqeast/districts-of-srilanka).
Coordinates for the added capitals come from [GeoNames](https://www.geonames.org/),
licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

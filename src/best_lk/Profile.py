import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo

from .DailyWeather import DailyWeather
from .DaytimeComfort import DaytimeComfort
from .ProfileCache import ProfileCache


@dataclass(frozen=True)
class Profile:
    name: str
    latlng: tuple[float, float]
    daily_weather: tuple[DailyWeather, ...]

    daily_variables = (
        "temperature_2m_mean",
        "rain_sum",
        "relative_humidity_2m_mean",
        "dew_point_2m_mean",
        "dew_point_2m_max",
    )

    @property
    def score(self):
        days = [d for d in self.daily_weather if d.comfort_score is not None]
        assessed = sum(d.assessed_shade_hours for d in days)
        if not assessed:
            return None
        return 100 * sum(d.comfortable_shade_hours for d in days) / assessed

    @classmethod
    def from_open_meteo(cls, name: str, latlng: tuple[float, float]):
        timezone = "Asia/Colombo"
        today = datetime.now(ZoneInfo(timezone)).date()
        start = today - timedelta(days=365)
        end = today - timedelta(days=1)
        cache = ProfileCache(latlng, name)
        try:
            weather = cls._parse_daily(cache.read(), start)
        except (FileNotFoundError, ValueError, KeyError, TypeError):
            daily = cls._fetch_daily(latlng, start, end, timezone)
            weather = cls._parse_daily(daily, start)
            cache.write(daily)
        return cls(name, latlng, weather)

    @staticmethod
    def _fetch_daily(latlng, start, end, timezone):
        latitude, longitude = latlng
        params = urlencode(
            {
                "latitude": latitude,
                "longitude": longitude,
                "timezone": timezone,
                "start_date": start.isoformat(),
                "end_date": end.isoformat(),
                "daily": ",".join(Profile.daily_variables),
                "hourly": ",".join(DaytimeComfort.variables),
                "wind_speed_unit": "ms",
                "temperature_unit": "celsius",
                "precipitation_unit": "mm",
            }
        )
        url = "https://archive-api.open-meteo.com/v1/archive"
        with urlopen(f"{url}?{params}", timeout=30) as response:
            payload = json.load(response)
        daily = payload["daily"]
        DaytimeComfort.add_counts(daily, payload["hourly"])
        return daily

    @staticmethod
    def _parse_daily(daily: dict, start: date) -> tuple[DailyWeather, ...]:
        dates = [start + timedelta(days=i) for i in range(365)]
        columns = [
            daily[key]
            for key in Profile.daily_variables + DaytimeComfort.counts
        ]
        if daily["time"] != [day.isoformat() for day in dates]:
            raise ValueError("Expected one weather record per requested day")
        if any(len(column) != len(dates) for column in columns):
            raise ValueError("Weather measurements do not match the dates")
        return tuple(DailyWeather(*row) for row in zip(dates, *columns))

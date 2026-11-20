import numpy as np
from thermofeel import calculate_utci


class DaytimeComfort:
    hours = tuple(range(7, 19))
    variables = ("temperature_2m", "dew_point_2m", "wind_speed_10m", "rain")
    counts = ("comfortable_shade_hours", "assessed_shade_hours")

    @classmethod
    def add_counts(cls, daily, hourly):
        expected = [
            f"{day}T{hour:02}:00"
            for day in daily["time"]
            for hour in range(24)
        ]
        if hourly["time"] != expected:
            raise ValueError("Expected 24 hourly records for each local date")
        temp, dew, wind, rain = [
            np.asarray(hourly[key], dtype=float).reshape(
                len(daily["time"]), 24
            )[:, cls.hours]
            for key in cls.variables
        ]
        valid = (
            (temp >= -50)
            & (temp <= 50)
            & np.isfinite(dew)
            & (wind >= 0)
            & (wind <= 17)
            & np.isfinite(rain)
            & (rain >= 0)
        )
        air_k = temp + 273.15
        utci = (
            calculate_utci(
                air_k, np.maximum(wind, 0.5), air_k, td_k=dew + 273.15
            )
            - 273.15
        )
        valid &= np.isfinite(utci)
        comfortable = valid & (utci > 9) & (utci <= 26) & (rain < 0.1)
        daily[cls.counts[0]] = comfortable.sum(axis=1).tolist()
        daily[cls.counts[1]] = valid.sum(axis=1).tolist()

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class DailyWeather:
    date: date
    mean_temperature_c: Optional[float]
    rainfall_mm: Optional[float]
    mean_relative_humidity_pct: Optional[float] = None
    mean_dew_point_c: Optional[float] = None
    max_dew_point_c: Optional[float] = None

    comfortable_shade_hours: Optional[int] = None
    assessed_shade_hours: Optional[int] = None

    @property
    def comfort_score(self) -> Optional[float]:
        if (
            not self.assessed_shade_hours
            or self.comfortable_shade_hours is None
        ):
            return None
        return 100 * self.comfortable_shade_hours / self.assessed_shade_hours

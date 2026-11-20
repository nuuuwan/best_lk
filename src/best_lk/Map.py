import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as PolygonPath

from .DistrictCapitals import DistrictCapitals
from .GreaterColombo import GreaterColombo
from .PointScores import PointScores
from .Profile import Profile


class Map:
    places = DistrictCapitals.places
    data = Path(__file__).resolve().parents[2] / "data"

    @classmethod
    def draw(cls, profiles, regional=False):
        profiles = sorted(profiles, key=PointScores.rank)
        figure, panels = plt.subplot_mosaic(
            [["map", "key"], ["metric", "metric"]],
            figsize=(9, 9.8),
            gridspec_kw={
                "width_ratios": [1.6, 1],
                "height_ratios": [8, 1.15],
            },
            layout="constrained",
        )
        ax, key = panels["map"], panels["key"]
        PointScores.describe(panels["metric"])
        cls._base(ax, regional)
        key.set(xlim=(0, 1), ylim=(len(profiles) + 0.4, -1.2))
        key.set_title("Locations by comfort score", loc="left", fontsize=11)
        key.set_axis_off()
        scale = PointScores.scale()
        for rank, profile in enumerate(profiles, 1):
            PointScores.mark(ax, key, scale, rank, profile)
        region = "Greater Colombo" if regional else "Sri Lanka"
        figure.suptitle(f"{region}  |  Outdoor comfort in shade", fontsize=17)
        if profiles and profiles[0].daily_weather:
            series = profiles[0].daily_weather
            period = f"{series[0].date:%d %b %Y} – {series[-1].date:%d %b %Y}"
            ax.set_title(period, fontsize=10)
        figure.colorbar(
            scale,
            ax=ax,
            orientation="horizontal",
            shrink=0.82,
            label="Dry daytime hours with no thermal stress (%)",
        )
        return figure

    @classmethod
    def _base(cls, ax, regional):
        boundary = json.loads((cls.data / "sri_lanka.geojson").read_text())
        rings = [
            PolygonPath(ring, closed=True)
            for polygon in boundary["coordinates"]
            for ring in polygon
        ]
        ax.add_patch(
            PathPatch(
                PolygonPath.make_compound_path(*rings),
                facecolor="#f1f0e9",
                edgecolor="#939e97",
                lw=0.8,
            )
        )
        xlim, ylim = (
            ((79.78, 80.15), (6.66, 7.25))
            if regional
            else ((79.40, 82.02), (5.82, 9.94))
        )
        ax.set(xlim=xlim, ylim=ylim, aspect=1.01)
        ax.set_axis_off()

    @classmethod
    def main(cls):
        images = cls.data.parent / "images"
        images.mkdir(parents=True, exist_ok=True)
        for places, filename, regional in (
            (cls.places, "weather-map.png", False),
            (GreaterColombo.places, "greater-colombo.png", True),
        ):
            profiles = [
                Profile.from_open_meteo(name, coords)
                for name, coords in places.items()
            ]
            figure = cls.draw(profiles, regional)
            figure.savefig(images / filename, dpi=180)
            plt.close(figure)
            print(images / filename)


if __name__ == "__main__":
    Map.main()

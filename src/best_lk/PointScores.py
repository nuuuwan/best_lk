from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap, Normalize, to_rgb


class PointScores:
    @staticmethod
    def scale():
        colors = ["#b2182b", "#e45722", "#ffa526", "#a5bb48", "#168047"]
        cmap = LinearSegmentedColormap.from_list("comfort", colors, N=257)
        return ScalarMappable(norm=Normalize(0, 100, clip=True), cmap=cmap)

    @staticmethod
    def label_color(color):
        linear = [
            v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
            for v in to_rgb(color)
        ]
        red, green, blue = linear
        luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
        return "black" if luminance > 0.179 else "white"

    @staticmethod
    def rank(profile):
        score = profile.score
        return (score is None, -(score or 0), profile.name)

    @staticmethod
    def mark(ax, key, scale, rank, profile):
        score = profile.score
        color = "#aaaaaa" if score is None else scale.to_rgba(score)
        label = "—" if score is None else f"{score:.1f}%"
        lng, lat = reversed(profile.latlng)
        ax.scatter(lng, lat, s=155, color=color, edgecolor="white", lw=0.7)
        ink = PointScores.label_color(color)
        ax.text(
            lng,
            lat,
            str(rank),
            ha="center",
            va="center",
            color=ink,
            fontsize=7,
            weight="bold",
        )
        key.text(0, rank - 1, f"{rank:02}", color="#57635c", fontsize=8)
        key.text(0.12, rank - 1, profile.name, fontsize=9)
        key.text(1, rank - 1, label, ha="right", fontsize=9)

    @staticmethod
    def describe(ax):
        ax.set_axis_off()
        ax.text(
            0.02,
            0.96,
            "How to read the score",
            va="top",
            fontsize=12,
            weight="bold",
        )
        ax.text(
            0.02,
            0.66,
            "The score is the percentage of assessed daytime hours "
            "that meet both limits.\n"
            "• In shade, the Universal Thermal Climate Index (UTCI) "
            "is above 9 °C and at or below 26 °C.\n"
            "• Rainfall in the preceding hour is below 0.1 mm.\n"
            "We assess 12 readings per day, 07:00–18:00 Sri Lanka time, "
            "and exclude hours with missing inputs.",
            va="top",
            fontsize=9.4,
            linespacing=1.4,
        )

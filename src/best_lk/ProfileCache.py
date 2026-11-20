import json
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import quote


class ProfileCache:
    directory = Path(__file__).resolve().parents[2] / "data" / "profiles"

    def __init__(self, latlng, name):
        lat, lng = map(float, latlng)
        filename = f"{lat}_{lng}_{quote(name, safe=' ')}.json"
        self.path = self.directory / filename
        self.legacy_path = self.directory / f"{lat}_{lng}.json"

    def read(self):
        if not self.path.exists():
            try:
                self.legacy_path.rename(self.path)
            except FileNotFoundError:
                pass
        return json.loads(self.path.read_text())

    def write(self, daily):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with NamedTemporaryFile(dir=self.path.parent, delete=False) as file:
            temporary = Path(file.name)
            try:
                file.write(json.dumps(daily).encode())
                file.flush()
                temporary.replace(self.path)
            finally:
                temporary.unlink(missing_ok=True)

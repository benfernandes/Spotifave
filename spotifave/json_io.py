import json
import attr
from pathlib import Path


@attr.s
class JsonIO:
    file_path: Path = attr.ib()

    def read_file(self):
        with self.file_path.open() as file:
            data = json.load(file)

        return data

    def write_file(self, data):
        with self.file_path.open('w') as file:
            json.dump(data, file)

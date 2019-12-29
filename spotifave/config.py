from pathlib import Path

import attr

from spotifave.json_io import JsonIO


@attr.s(frozen=True)
class Api:
    client_id: str = attr.ib()
    client_secret: str = attr.ib()


@attr.s(frozen=True)
class Spotify:
    user_uri: str = attr.ib()
    playlist_uri: str = attr.ib()


@attr.s(frozen=True)
class Settings:
    max_artists: int = attr.ib()


class Config:
    def __init__(self, file_path: Path):
        config_json = JsonIO(file_path).read_file()

        self.api = Api(
            config_json['api']['client_id'],
            config_json['api']['client_secret']
        )

        self.spotify = Spotify(
            config_json['spotify']['user_uri'],
            config_json['spotify']['playlist_uri']
        )

        self.settings = Settings(
            config_json['settings']['max_artists']
        )

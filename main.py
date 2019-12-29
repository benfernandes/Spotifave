from pathlib import Path

from spotifave.config import Config
from spotifave.gui import Gui
from spotifave.spotipy_service import SpotipyService
from spotifave.utils import Utils


def main(config_file_path: Path):
    config = Config(config_file_path)
    sp = SpotipyService(config.api.client_id, config.api.client_secret)

    # Get data
    tracks = sp.get_tracks_in_playlist(config.spotify.user_uri, config.spotify.playlist_uri)

    # Manipulate data
    artist_counts = Utils.count_artists_in_tracks(tracks)
    sorted_artist_counts = Utils.sort_artist_counts(artist_counts)

    # Display data
    Gui.display_chart(Utils.trim_dict(sorted_artist_counts, config.settings.max_artists))


if __name__ == '__main__':
    main(
        Path('./appConfig.json')
    )

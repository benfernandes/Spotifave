from collections import OrderedDict
from typing import List, Dict

from spotifave.spotipy_service import Track, Artist


class Utils:
    @staticmethod
    def count_artists_in_tracks(tracks: List[Track]) -> Dict[Artist, int]:
        artists_and_counts: Dict[Artist, int] = {}

        for track in tracks:
            for artist in track.artists:
                if artist in artists_and_counts.keys():
                    artists_and_counts[artist] += 1
                else:
                    artists_and_counts[artist] = 1

        return artists_and_counts

    @staticmethod
    def sort_artist_counts(artist_counts: Dict[Artist, int]) -> Dict[Artist, int]:
        return OrderedDict(sorted(artist_counts.items(), key=lambda x: x[1], reverse=True))

    @staticmethod
    def trim_dict(dictionary: Dict[any, any], max_items: int) -> Dict[any, any]:
        return OrderedDict(list(dictionary.items())[0:max_items])

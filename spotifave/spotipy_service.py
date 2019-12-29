from typing import List
from spotipy import oauth2
import attr
import spotipy


@attr.s(frozen=True)
class Artist:
    id: str = attr.ib()
    name: str = attr.ib()


@attr.s(frozen=True)
class Track:
    name: str = attr.ib()
    artists: List[Artist] = attr.ib()


class SpotipyService:
    def __init__(self, client_id: str, client_secret: str) -> None:
        credentials = oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        token = credentials.get_access_token()
        self.sp = spotipy.Spotify(auth=token)

    def get_tracks_in_playlist(self, user_uri: str, playlist_uri: str) -> List[Track]:
        all_tracks: List[Track] = []

        playlist_data = self.sp.user_playlist(
            user_uri, playlist_uri, fields='tracks,next')
        tracks = playlist_data['tracks']

        all_tracks = self._read_tracks_page(all_tracks, tracks)

        # This is required to hand track pagnation
        while tracks['next']:
            tracks = self.sp.next(tracks)
            all_tracks = self._read_tracks_page(all_tracks, tracks)

        return all_tracks

    def _read_tracks_page(self, all_tracks: List[Track], tracks: any) -> List[Track]:
        for track in tracks['items']:
            all_tracks.append(self._parse_track(track['track']))

        return all_tracks

    @staticmethod
    def _parse_track(raw_track: any) -> Track:
        return Track(
            raw_track['name'],
            [Artist(artist['id'], artist['name']) for artist in raw_track['artists']]
        )

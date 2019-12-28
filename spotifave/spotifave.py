import spotipy
import spotipy.oauth2 as oauth2
import matplotlib.pyplot as plt
import matplotlib.cm as mcm
import squarify

print("Starting")

client_id = ""
client_secret = ""
credentials = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

all_tracks = []


def read_page(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        artist = track['artists'][0]['name']
        title = track['name']
        all_tracks.append([artist, title])


def count_artists():
    print("Counting artists")

    counted_dict = {}

    for track in all_tracks:
        if track[0] in counted_dict:
            counted_dict[track[0]] += 1
        else:
            counted_dict[track[0]] = 1

    counted_list = []
    for artist in counted_dict:
        counted_list.append([artist, counted_dict[artist]])

    return counted_list


def process_artists():
    print("Processing artists")

    counted = count_artists()
    counted.sort(key=lambda x: x[1], reverse=True)

    max_artists = 30
    if len(counted) > max_artists:
        print(len(counted), "artists")
        print("Trimming")
        counted = counted[0:max_artists]
        print(len(counted), "artists")

    artists, counts = map(list, zip(*counted))

    for i in range(len(artists)):
        artists[i] = artists[i] + "\n" + str(counts[i])

    return artists, counts


def display_chart(counts, artists):
    print("Displaying chart")

    cmap = mcm.get_cmap("prism")
    colors = [cmap(i/len(counts)) for i in range(len(counts))]

    squarify.plot(sizes=counts, label=artists, alpha=.7, color=colors)

    fig = plt.gcf()
    fig.canvas.set_window_title("Artist Treemap")

    plt.subplots_adjust(left=0, bottom=0, top=1, right=1)
    plt.axis('off')
    plt.show()


def find_favourites(user_uri, playlist_uri):
    print("Downloading data")

    results = sp.user_playlist(user_uri, playlist_uri, fields="tracks,next")
    tracks = results['tracks']
    read_page(tracks)

    while tracks['next']:
        tracks = sp.next(tracks)
        read_page(tracks)

    artists, counts = process_artists()

    display_chart(counts, artists)
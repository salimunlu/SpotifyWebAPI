from spotify_auth import get_token
from spotify_data import get_artist_albums, get_album_tracks, get_track_audio_features
import pandas as pd   # Veri Analizi

from visual_utils import plot_scatter

artist_id = 'ARTIST_ID'

access_token = get_token()

albums = get_artist_albums(artist_id, access_token)
albums = get_artist_albums(artist_id, access_token)

data = []

for i, album in enumerate(albums["items"], 1):
    album_name = album["name"]
    release_date = album["release_date"]
    # print(i, album_name, release_date)

    # Albümdeki tüm şarkıları al
    tracks_data = get_album_tracks(album["id"], access_token)

    for j, track in enumerate(tracks_data["items"], 1):
        # print("\t", j, track["name"])
        audio_data = get_track_audio_features(track["id"], access_token)
        audio_data.update(
            {
                "track_name": track["name"],
                "album_name": album_name,
                "release_date": release_date,
                "album_id": album["id"]
            }
        )
        data.append(audio_data)

    # print("*********************************************")
    # print()


df = pd.DataFrame(data=data)
# df.to_csv("tarkan.csv")

plot_scatter(df)



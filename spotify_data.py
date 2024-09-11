import requests

BASE_URL = 'https://api.spotify.com/v1/'


def get_artist_albums(artist_id, access_token):
    url = BASE_URL + "artists/" + artist_id + "/albums"

    params = {
        "include_groups": "album",
        "limit": 50
    }

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, params=params, headers=headers)

    return response.json()


def get_album_tracks(album_id, access_token):
    url = BASE_URL + "albums/" + album_id + "/tracks"

    params = {
        "limit": 50
    }

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, params=params, headers=headers)

    return response.json()


def get_track_audio_features(track_id, access_token):
    url = BASE_URL + "audio-features/" + track_id
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

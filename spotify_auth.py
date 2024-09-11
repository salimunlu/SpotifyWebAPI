import requests

# Client ID and Secret
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

AUTH_URL = 'https://accounts.spotify.com/api/token'


def get_token():
    # Spotify Web API'ye kimlik doğrulama isteği gönderiyoruz.
    auth_response = requests.post(
        AUTH_URL,
        {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )

    return auth_response.json()['access_token']


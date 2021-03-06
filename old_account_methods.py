import requests
import auth

def get_playlists(token, spotify_name):
    try:
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
        print(response)
        response = response.json()

        playlists = response['items']
        id_own_playlists = []
        id_follow_playlists = []
        name_my_lists = []

        for item in playlists:
            if item['owner']['display_name'] == spotify_name:
                id_own_playlists.append(item['uri'].split(':')[2])
                name_my_lists.append(item['name'])
            else:
                id_follow_playlists.append([item['uri'].split(':')[2], item['public']])

        return id_own_playlists, id_follow_playlists, name_my_lists

    except Exception as e:
        print(e)

def get_songs_from_playlist(token, id_playlists):
    songs_id = []
    try:
        for list in id_playlists:
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            response = requests.get(f'https://api.spotify.com/v1/playlists/{list}/tracks', headers=headers)
            response = response.json()
            list_songs = []
            for song in response['items']:
                list_songs.append(f"spotify:track:{song['track']['id']}")
            songs_id.append(list_songs)
        return songs_id

    except Exception as e:
        print(e)

def get_liked_songs(token):
    id_liked_songs = []
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept":"application/json"}
    response = requests.get(f'https://api.spotify.com/v1/me/tracks', headers=headers)
    print(response)
    response = response.json()
    for song in response['items']:
        id_liked_songs.append(song['track']['id'])

    return id_liked_songs
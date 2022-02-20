import requests

def create_playlists(token, user_id, name_list, public=True):
    try:
        id_lists = []
        for list in name_list:
            print(list)
            data = {
                "name": list,
                "description": "",
                "public": public
            }
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

            response = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", json=data, headers=headers)
            response = response.json()
            id_lists.append(response['id'])

        return id_lists
    except Exception as e:
        print(e)

def add_songs_to_playlists(token, id_songs):
    for playlist_id in id_songs.keys():
        try:
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            songs = '%2C'.join(id_songs[playlist_id])
            response = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={songs}', headers=headers)
            print(response)
            response = response.json()

        except Exception as e:
            print(e)

def follow_list(token, lists_to_follow):
    for list in lists_to_follow:
        try:
            data = {
                "public": list[1]
            }
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            response = requests.put(f'https://api.spotify.com/v1/playlists/{list[0]}/followers', json=data, headers=headers)
            print(response)
            response = response.json()
        except Exception as e:
            print(e)
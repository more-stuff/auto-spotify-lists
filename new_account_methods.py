import requests

def create_playlists(token, user_id, name_list, public=True):
    try:
        id_lists = []
        for list in name_list:
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

def add_songs_to_playlists(token, id_songs, id_lists):
    #print(len(id_songs))
    #print()
    for i in range(len(id_songs)):
        try:
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}
            songs = ','.join(id_songs[i])
            response = requests.post(f'https://api.spotify.com/v1/playlists/{id_lists[i]}/tracks?uris={songs}', headers=headers)
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
            response = response.json()
            print(response)
        except Exception as e:
            print(e)


def like_songs(token, id_liked_songs):
    for song in id_liked_songs:
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={song}', headers=headers)
        response = response.json()
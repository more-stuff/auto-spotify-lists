import auth
import old_account_methods
import new_account_methods
import urllib

client_id = '591f898374464aedb2c5810a0facb6eb'
client_secret = '502b106fd2f64280a642c7bf2644c6bd'
redirect_uri = 'https://github.com/z3hcnas'
spotify_name = 'lol'
spotify_id_new = 'zj4jfhtfl7h6vqmidwzeixdub'
version = ''

if version == 'cutre':
    token = auth.cutre_version()

else:
        encoded_redirect_url = urllib.parse.quote_plus(redirect_uri)
        # The code starts here
        token = ''
        if token == '':
            code_auth = auth.get_code(client_id, encoded_redirect_url)
            token, refresh_token = auth.get_token(client_id, client_secret, redirect_uri, code_auth)

id_own_playlists, id_followed_playlists, name_my_lists = old_account_methods.get_playlists(token, spotify_name)
songs_id = old_account_methods.get_songs_from_playlist(token, id_own_playlists)

print(songs_id)

if version == 'cutre':
    token = auth.cutre_version()
else:
    # get the token for the second user and
    token = ''
    if token == '':
        code_auth = auth.get_code(client_id, encoded_redirect_url)
        token, refresh_token = auth.get_token(client_id, client_secret, redirect_uri, code_auth)

id_new_lists = new_account_methods.create_playlists(token, spotify_id_new, name_my_lists)
new_account_methods.add_songs_to_playlists(token, songs_id, id_new_lists)
new_account_methods.follow_list(token, id_followed_playlists)

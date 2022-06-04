import auth
import old_account_methods
import new_account_methods
import urllib

client_id = '591f898374464aedb2c5810a0facb6eb'
client_secret = '502b106fd2f64280a642c7bf2644c6bd'
redirect_uri = 'https://github.com/z3hcnas'
spotify_name = 'Izan'
spotify_id_new = '315rbmtzk33gglv56i6z3rqt27wy'
version = 'cutre'

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
#id_liked_songs = old_account_methods.get_liked_songs(token)


if version == 'cutre':
    token = auth.cutre_version()
else:
    # get the token for the second user and
    token = ''
    if token == '':
        code_auth = auth.get_code(client_id, encoded_redirect_url)
        token, refresh_token = auth.get_token(client_id, client_secret, redirect_uri, code_auth)

id_new_lists = new_account_methods.create_playlists(token, spotify_id_new, name_my_lists)
print(id_new_lists)
#new_account_methods.add_songs_to_playlists(token, songs_id, id_new_lists)
#new_account_methods.follow_list(token, id_followed_playlists)
#new_account_methods.like_songs(token, id_liked_songs)


# mscguay+ips2112@gmail.com
# mscguay+ips2204@gmail.com

# mscguay+psm2112@gmail.com
# mscguay+psm2204@gmail.com

# Mus1c4Pr3m1um

# BQApuA1cyZtd7TkGLa8z6kouI8oNpYv7KloLXqN5MKXHukirJbPox5CbMc2hva4Nm4Kks5ntmqtCm-Ee3X95msZsCYana96ISTDO2lGCxUpodgtTv7tzlI4TK8HgDGI_d3MgxpJxzDQb7UZXqYOMNjvtr3Suk50_asY
# BQAMvNrbFt8QMRECdBNzTHyXfeULpwyLjBaiSx-Od4XfkVQIMASiFfU21EmKXQqmk7QJ7oxXNAbQda4CB5ti2jXKhhqq-OQaKrS0lC9IlktXEpRO74CtwSLFWjpnA_lLanjHSwxBo2x3IRhHztf3hb6EuHlLBwkfFzwfmnc
import urllib.parse
import base64
import requests
from selenium import webdriver


def get_code(client_id, encoded_redirect_url):
    scope = 'user-read-private user-read-email playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-modify user-library-read'
    output = requests.get(f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={encoded_redirect_url}&scope={scope}")
    driver = webdriver.Chrome('./chromedriver.exe')
    print("Now go here and accept the terms")
    driver.get(output.url)
    code = input("Introduce the code from the url: ")

    return code

# get the token
def get_token(client_id, client_secret, redirect_uri, code):
    params = {'grant_type':'authorization_code', 'code':code, 'redirect_uri':redirect_uri, "client_id":client_id, "client_secret":client_secret}

    token_output = requests.post('https://accounts.spotify.com/api/token', data=params).json()
    print(token_output)

    token = token_output['access_token']
    refresh_token = token_output['refresh_token']


    return token, refresh_token


def refresh_token(client_id, client_secret, refresh_token):
    credentials_encoded = str(base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8"))).split("'")[1]
    headers = {"Authorization": f"Basic {credentials_encoded}"}
    params = {'grant_type':'authorization_code', 'refresh_token':refresh_token}

    token_output = requests.post('https://accounts.spotify.com/api/token', data=params, headers=headers).json()
    refreshed_token = token_output['access_token']
    return refreshed_token


def cutre_version():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://developer.spotify.com/console/get-playlists/')
    print('Permisions required')
    print('playlist-read-private')
    print('playlist-read-public')
    print('playlist-modify-public')
    print('playlist-modify-private')
    print('playlist-read-collaborative')
    print('user-library-modify')
    print('user-library-read')
    return input('Introduce the token:')

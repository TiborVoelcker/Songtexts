# -*- coding: utf-8 -*-

import requests
import webbrowser
import json
import time

class OAuth():
    def __init__(self, client_id, client_secret, redirect_uri, authorize_url, access_token_url, scope='', cache_path='config/Token.cache'):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret

        self.SCOPE = scope

        self.REDIRECT_URI = redirect_uri
        self.AUTHORIZE_URL = authorize_url
        self.ACCESS_TOKEN_URL = access_token_url
        self.cache_path = cache_path

    def get_access_token(self):
        token = self.get_cached_token()
        if token: return token
        url = self.AUTHORIZE_URL+"client_id="+self.CLIENT_ID+"&response_type=code&redirect_uri="+self.REDIRECT_URI
        if self.SCOPE: url = url + "&scope="+self.SCOPE
        # 1. Ask for an authorization code
        webbrowser.open(url)
        auth_code = input("Copy URL: ").split("?code=")[1]
        # 2. Ask for Access Token
        payload = {'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': self.REDIRECT_URI, 'client_id': self.CLIENT_ID, 'client_secret':self.CLIENT_SECRET, 'scope': self.SCOPE}
        token = requests.post(self.ACCESS_TOKEN_URL, data=payload).json()
        self.save_token(token)
        return token

    def get_cached_token(self):
        try:
            f = open(self.cache_path)
            token = f.read()
            f.close()
            token = json.loads(token)
            if self.is_expired(token):
                print("Token expired.")
                token = self.refresh_token(token['refresh_token'])
            return token
        except FileNotFoundError:
            return False

    def save_token(self, token):
        f = open(self.cache_path, 'w')
        token['expires_at'] = int(time.time()) + int(token['expires_in'])
        f.write(json.dumps(token))
        f.close()

    def is_expired(self, token):
        now = int(time.time())
        return token['expires_at'] < now

    def refresh_token(self, token):
        payload = {'grant_type': 'refresh_token', 'refresh_token': token, 'client_id': self.CLIENT_ID, 'client_secret':self.CLIENT_SECRET, 'scope': self.SCOPE}
        token = requests.post(self.ACCESS_TOKEN_URL, data=payload).json()
        self.save_token(token)
        return token
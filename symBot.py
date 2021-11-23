from mastodon import Mastodon, StreamListener
from dotenv import load_dotenv
import os

#環境変数の追加
load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
API_BASE_URL = os.getenv('API_BASE_URL')


# Botの主な挙動をここに記述します。
class Bot(StreamListener):
    # Botの準備してくれる所。所謂おまじない。
    def __init__(self):
        super(Bot, self).__init__()
    # アカウントのローカルタイムラインに動きがあると新規トゥートの情報を持って中の挙動を読み取る。
    def on_update(self, status):
        content = status['content'].replace('<p>', '').replace('</p>', '')
        if 'お腹すいた' in content or 'おなかすいた'in content:
          mastodon.toot('とてもわかる🐱')


def Login():
    mastodon = Mastodon(
                access_token = ACCESS_TOKEN,           # ここにさっき取得したアクセストークンを入れる。
                api_base_url = API_BASE_URL            # ここにMastodonのインスタンスのURLを記述
                )
    return mastodon

def LTLlisten(mastodon):
    bot = Bot()
    mastodon.stream_local(bot)

# ログインする処理
mastodon = Login()
LTLlisten(mastodon)
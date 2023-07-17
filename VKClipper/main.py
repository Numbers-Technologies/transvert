import json
import requests
import os
from config import *
from pprint import pprint

token = "vk1.a.gAbcGWiuz3LYZCl8Za7tRLat_oUdl0VhANAq6rVQo7V_miaPMT-mCO_dfuiMhrB-8-HuJRybZ1yWa32Y0Bc5PoO35DPgMuUv2bLJ0nU4qDaRV__44V1IqoZDLDFZ0cbnCiGZQWiSnHOLQbECmYMUpEQK1yR1dBBwQ9h967kF1EzgunWDXi9-VtVyv3EjYH_pw0puRvOkIWUOKyIPilODNw"


class Post:
    def __init__(self, text: str, content: list, post_id: int = 0) -> None:
        self.post_id: int = post_id
        self.text: str = text
        self.content: list = content

    def __str__(self):
        return f'Post({self.post_id}, {self.text}, {self.content})'



class VKClipper:
    def __init__(self, group_name: str, vk_token: str, api_version: str = '5.131', count: int = 2):
        self.group_name = group_name
        self.url = f'https://api.vk.com/method/wall.get?domain={group_name}&count={str(count)}&access_token={token}&v={api_version}'

    def get_posts(self) -> None:
        self.response = requests.get(self.url).json()['response']['items']
        #pprint(self.response)

        for i in self.response:
            post = Post(i['id'], i['text'], i['attachments'])
            print(post.text)
        

VKClipper(group_name="slvgoo", vk_token=token).get_posts()










"""
def get_wall_post():
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count={str(count)}&access_token={vk_token}&v={api_version}"
    req = requests.get(url)
    src = req.json()

    if os.path.exists(f"VKClipper/{group_name}"):
        print(f"Директория VKClipper/{group_name} уже существует")
    else:
        os.mkdir(f"VKClipper/{group_name}")

    with open(f"VKClipper/{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, ensure_ascii=False)
    file.close()

    fresh_posts_id = []
    posts = src["response"]["items"]

    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)

    if not os.path.exists(f"VKClipper/{group_name}/exists_posts_{group_name}.txt"):
        print("Создание файла с ID постов")

    with open(f"VKClipper/{group_name}/exists_posts_{group_name}.txt", "w") as file:
        for item in fresh_posts_id:
            file.write(str(item)+ "\n")

    for post in posts:
        post_id = post["id"]
        print(f"ID поста: {post_id}")

        try:
            post_text = post["text"]
            print(f"Текст поста: {post_text}\n")
        except Exception as ex:
            print("Пост без текста")
        try:
            
            if "attachments" in post:
                post = post["attachments"]

                if post[0]["type"] == "photo":
                    if len(post) == 1:
                        post_photo = post[0]["photo"]["sizes"][-1]["url"]
                        print(f"Ссылка на фото: {post_photo}")
                    else:
                        for post_photos in post:
                            post_photo = post_photos["photo"]["sizes"][-1]["url"]
                            print(f"Ссылка на фото: {post_photo}\n")

        except Exception as ex:
            print(ex)


def main():
    get_wall_post()
"""

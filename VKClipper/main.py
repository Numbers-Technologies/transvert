# VKClipper is a object that can get posts from vk.com/group_name url and send it to any of MQ driver (RabbitMQ, MemoreMQ, Celery).
# All variables such as VK_TOKEN, REFRESH_RATE and etc.. must be stored in environment
# 
# Usage example:
# ```
# VKClipper(params...).start_session()
# ```
# Written by Andrey Averin <email@email.root> 17.07.2023 with
# Co-author(s): Daniil Ermolaev <blcklptn@icloud.com> 18.07.2023.

import requests
import pickle
from config import *
from typing import Self
import time
from pprint import pprint

# For serialization via pickle.
# Outut: Posts.{post_id, text, content}
# From Pickle: bytes
class Post:
    def __init__(self, text: str, content: list, post_id: int = 0) -> Self:
        self.post_id: int = post_id
        self.text: str = text
        self.content: list = content

    def __str__(self) -> None:
        return f'Post({self.post_id}, {self.text}, {self.content})'



class VKClipper:
    def __init__(self, group_name: str, vk_token: str, api_version: str = '5.131', count: int = 1) -> Self:
        self.group_name = group_name
        self.url = f'https://api.vk.com/method/wall.get?domain={group_name}&count={str(count)}&access_token={vk_token}&v={api_version}'
        self.old_hashes = []
        self.start_session()

    def get_posts(self) -> list | None :
        self.response = requests.get(self.url).json()['response']['items']
        posts = []
        for i in self.response:
            post = Post(
                    post_id=i['id'],
                    text=i['text'],
                    content=[k['photo']['sizes'][-1]['url'] if 'photo' in k.keys() else k['doc']['url'] for k in i['attachments']]
            )
            if i['hash'] not in self.old_hashes:
                posts.append(post)
                self.old_hashes.append(i['hash'])
        if len(posts) != 0: return pickle.dumps(posts, protocol=pickle.HIGHEST_PROTOCOL)
        return None
    
    def start_session(self):
        while True:
            new_posts = self.get_posts()
            time.sleep(REFRESH_RATE)

VKClipper(group_name=GROUP_NAME, vk_token=VK_TOKEN, count=3)

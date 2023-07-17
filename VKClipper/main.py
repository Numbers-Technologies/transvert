import json
import requests
import os
from config import *



def get_wall_post():
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count={post_count}&access_token={token_vk}&v=5.131"
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

if __name__ == '__main__':
    main()
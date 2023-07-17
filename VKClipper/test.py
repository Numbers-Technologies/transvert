import pickle

class Post:
    def __init__(self, text: str, content: list, post_id: int = 0) -> None:
        self.post_id: int = post_id
        self.text: str = text
        self.content: list = content

    def __str__(self):
        return f'Post({self.post_id}, {self.text}, {self.content})'



some_object = b'\x80\x04\x95,\x02\x00\x00\x00\x00\x00\x00]\x94(\x8c\x08__main__\x94\x8c\x04Post\x94\x93\x94)\x81\x94}\x94(\x8c\x07post_id\x94JTc\t\x00\x8c\x04text\x94\x8c\x16\xd0\x98\xd1\x89\xd0\xb5\xd0\xbc \xd0\xb8\xd1\x85\n\xd0\x90\xd0\xbd\xd0\xbe\xd0\xbd\x94\x8c\x07content\x94]\x94\x8c\xd7https://sun21-2.userapi.com/impg/PKcIkMpYQfpTWhi_1qu8aQsj7SxBoaJKxeW2lQ/WchIvC3GuIc.jpg?size=510x514&quality=95&sign=a62f6ea4749ed093fd21c798707c5ff9&c_uniq_tag=2mdNg7pE6LYxRErB6a3xEJKenyluIKBQzn1sEYIKIuU&type=album\x94aubh\x03)\x81\x94}\x94(h\x06J:c\t\x00h\x07\x8c\x00\x94h\t]\x94\x8c\xd7https://sun21-1.userapi.com/impg/SqzFUw2s-Mfi3tz7Q9uUnPGw67eVREqKrRLEEw/p9mXr_wsJj4.jpg?size=510x430&quality=95&sign=aad03bd617a08f7bb31965828c2b057e&c_uniq_tag=LmsQkqSG0Ggb3jS4N2ba_BGWwGem6E0LRP1vXj-GJBM&type=album\x94aube.'



q = pickle.loads(some_object)
print(q[0].content)

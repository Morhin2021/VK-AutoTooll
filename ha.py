from __future__ import annotations
from config import*
import vk_api
import requests


class worker():


    def __init__(self, token : str) -> worker:
        self.token=token
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()


    def get_byid(self):
        r = requests.get(f"https://api.vk.com/method/gifts.getCatalog?access_token={self.token}&v=5.131").json()["response"][0]["items"]
        for line in r:
            id_gift = line["gift"]["id"]
            price_str = line["price_str"]
            if price_str == "Бесплатно":
                return id_gift


    def add_friends(self):
        self.vk.friends.add(user_id=Profile_id)


    def add_likes(self):
        self.vk.likes.add(type="photo", owner_id=Profile_id, item_id=Photo_id)


    def add_photo(self):
        owner_id=self.vk.users.get()
        self.vk.wall.repost (object=Post_id)


    def add_gift(self):
        for x in range(0,5):
            send_code = "var gift = " + str(self.get_byid()) + "; return API.gifts.send({user_ids:" + str(Profile_id) + ",gift_id:gift,guid:API.apps.getRandomInt({max:99999})});"
            self.vk.execute(code=send_code)
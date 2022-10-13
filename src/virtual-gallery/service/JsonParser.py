import json
import requests

class MediaData:
    def __init__(self, history, anime, games):
        self.history = history
        self.anime = anime
        self.games = games

    @classmethod
    def from_json(cls, json_string):

        json_dict = json.loads(json_string)
        return cls(**json_dict)


if __name__ == "__main__":
    response = requests.get(
        "https://api.myanimelist.net/v2/users/curiossity/animelist?status=completed", headers={"X-MAL-CLIENT-ID": "05238348537b2a8ebe3e1daf070dcce9"})

    data = MediaData.from_json(str(response.content).removeprefix("b'").removesuffix("'"))
    print(data)

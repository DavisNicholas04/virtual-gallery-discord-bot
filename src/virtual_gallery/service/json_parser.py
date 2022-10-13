import json


class MediaData:
    def __init__(self, history, anime, game):
        self.history = history
        self.anime = anime
        self.game = game

    @classmethod
    def from_json(cls, json_string):
        # print(json_string)
        json_dict = json.loads(json_string)
        return cls(**json_dict)

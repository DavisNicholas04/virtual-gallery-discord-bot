import json


class MediaData:
    def __init__(self, history, anime, games):
        self.history = history
        self.anime = anime
        self.games = games

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

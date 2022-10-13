import json


class MediaData:
    def __init__(self, history_link, anime_link, games_link, history, anime, game):
        self.history_link = history_link
        self.anime_link = anime_link
        self.games_link = games_link
        self.history = history
        self.anime = anime
        self.game = game

    @classmethod
    def from_json(cls, json_string):
        # print(json_string)
        json_dict = json.loads(json_string)
        return cls(**json_dict)

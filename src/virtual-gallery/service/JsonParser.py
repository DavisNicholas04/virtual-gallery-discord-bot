import json

class MediaData:
    def __init__(self, history):
        self.node = history.node
        self.title = self.node['title']
        self.description = self.node['description']
        self.date = self.node['node.date']
        self.images = self.node['node.images']

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<title: {self.title}>'

json_string = '''{
    "history": [
        {
            "node": {
                "title":"string",
                "description":"string",
                "date":"dateTime",
                "images":"string <location of file in github>"
            }
        }
    ]
}'''

data = MediaData.from_json(json_string)
print(data)

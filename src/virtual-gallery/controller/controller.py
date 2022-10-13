import requests
import os


def get_json_from_github(api):
    """
    makes a request to an endpoint you specify on github's raw user content api

    :param api: fileName that you wish to access from the json directory
    :return: string representation of a json object
    :rtype: str
    """
    response = requests.get(f"{os.environ['GITHUB_ROOT_URL']}{api}")
    if response.status_code == 200:
        print(response.content)
        return response.content
    else:
        print(f"{response.status_code}: {response.content}")
        return str(response.content).removeprefix("b'").removesuffix("'")

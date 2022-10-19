import requests
import os

from src.utils.utils import gen_two_rand_resources
from src.model.main_data_model import MediaData


def get_resource_from_github(folder, file, return_string=True):
    """
    makes a request to an endpoint you specify on github's raw user content api

    :param return_string: specifies whether or not you want the response as a string or in it's original form
    :param folder: the directory you are trying to reach from tree/main
    :param file: fileName that you wish to access from the json directory
    :return: string representation of a json object
    """
    response = requests.get(f"{os.environ['RAW_GITHUB_ROOT_URL'] + folder + '/' + file}")
    if response.status_code == 200:
        if return_string:
            backslash = "\\"
            val = str(response.content).removeprefix("b'").removesuffix("'").replace("\\n", "").replace("\\t", "").replace(backslash, "")
            return val
        else:
            val2 = response.content
            return val2
    else:
        print(f"{response.status_code}: {response.content}")
        return str(response.content).removeprefix("b'").removesuffix("'")


def get_two_recourses(selection):
    full_json = get_resource_from_github("jsonFiles", "main_data.json")
    mdo = MediaData.from_json(full_json)  # mdo = media data object

    if selection == "history":
        resources = gen_two_rand_resources(mdo.history)
        return resources
    elif selection == "anime":
        resources = gen_two_rand_resources(mdo.anime)
        return resources
    elif selection == "games":
        resources = gen_two_rand_resources(mdo.game)
        return resources
    else:
        return None
import requests
import os


def get_resource_from_github(folder, file, return_string=True):
    """
    makes a request to an endpoint you specify on github's raw user content api

    :param return_string: specifies whether or not you want the response as a string or in it's original form
    :param folder: the directory you are trying to reach from tree/main
    :param file: fileName that you wish to access from the json directory
    :return: string representation of a json object
    """
    response = requests.get(f"{os.environ['GITHUB_ROOT_URL'] + folder + '/' + file}")
    if response.status_code == 200:
        print(response.content)
        return response.content
    else:
        print(f"{response.status_code}: {response.content}")
        if return_string:
            return str(response.content).removeprefix("b'").removesuffix("'")
        else:
            return response.content


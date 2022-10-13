def get_title(genre, index):
    """
    helper function to return the title of a resource

    :param genre: main genre of the json file (i.e. history, anime, games)
    :param index: the index of the resource you want to access (i.e. history[0])
    :return: title of the media you are accessing
    :rtype: str
    """
    return genre[index]['title']


def get_description(genre, index):
    """
    helper function to return the description of a resource

    :param genre: main genre of the json file (i.e. history, anime, games)
    :param index: the index of the resource you want to access (i.e. history[0])
    :return: description of the media you are accessing
    :rtype: str
    """
    return genre[index]['description']


def get_date(genre, index):
    """
    helper function to return the date of a resource

    :param genre: main genre of the json file (i.e. history, anime, games)
    :param index: the index of the resource you want to access (i.e. history[0])
    :return: date of the media you are accessing
    :rtype: str
    """
    return genre[index]['date']


def get_images(genre, index):
    """
    helper function to return the image(s) of a resource

    :param genre: main genre of the json file (i.e. history, anime, games)
    :param index: the index of the resource you want to access (i.e. history[0])
    :return: date of the media you are accessing
    :rtype: str
    """
    return genre[index]['images']


def get_genre(genre, index):
    """
    :param genre: main genre of the json file (i.e. history, anime, games)
    :param index: the index of the genre you want to access (i.e. history[0])
    :return: the name of title of the entity
    :rtype: str
    """
    return genre[index]['genre']


def remove_body_tag_from_requests(response):
    """
    removes body tag caused by using the requests package (i.e. b'{JSON OBJ}' -> {JSON OBJ}).

    Also converts byte response to a string.

    :param response: api request response
    :return: the json object with body tage from requests package removed. Also converted to a string
    :rtype: str
    """
    return str(response.content).removeprefix("b'").removesuffix("'")

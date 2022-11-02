import asyncio
import random

import interactions
from typing import Optional


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


def gen_two_rand_resources(genre):
    mdo_len = len(genre)
    index1 = random.randrange(0, mdo_len)
    index2 = random.choice([i for i in range(0, mdo_len) if i not in [index1]])
    resources: [] = genre[index1], genre[index2]
    return resources


async def delete(msg: interactions.Message, delay: Optional[float] = None) -> None:
    if delay is not None:
        async def delete_msg(delay_by: float):
            await asyncio.sleep(delay_by)
            await msg.delete()

        asyncio.create_task(delete_msg(delay))
    else:
        await msg.delete()


async def edit(ctx: interactions.ComponentContext, msg: str = None, components=None,
               delay: Optional[float] = None) -> None:
    if delay is not None:
        async def edit_msg(delay_by: float):
            await asyncio.sleep(delay_by)
            await ctx.edit(msg, components=components)

        asyncio.create_task(edit_msg(delay))
    else:
        await ctx.edit(msg, components=components)

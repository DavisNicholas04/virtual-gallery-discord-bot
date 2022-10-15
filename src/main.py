import os
import time

import interactions
from dotenv import load_dotenv
from src.service.helper_service import get_two_recourses
from src.controller.controller import get_resource_from_github
# from src.service.helper_service import multi_component

button_ids_dict = {}

if __name__ == "__main__":
    load_dotenv()
    intent = interactions.Intents.DEFAULT
    client = interactions.Client(token=os.environ['DISCORD_TOKEN'], intents=intent)

    @client.command(
        name="start",
        description="start the interaction, which will tell the bot to message the user privately",
    )
    async def start(msg: interactions.ComponentContext):
        await msg.send("Welcome to the interactive virtual gallery experience. "
                       "For a list of commands use the ``/help`` command")
        time.sleep(1)
        options = interactions.SelectMenu(
            custom_id="genre_select",
            options=[
                interactions.SelectOption(custom_id="custom_id_history", label="History",
                                          value="history", decription="description_history"),

                interactions.SelectOption(custom_id="custom_id_anime", label="Anime",
                                          value="anime", decription="description_anime"),

                interactions.SelectOption(custom_id="custom_id_games", label="Games",
                                          value="games", decription="description_games")],

            placeholder="Choose your experience",
        )
        await msg.send(content="choose your genre", components=options)


    @client.component("genre_select")
    async def select_menu_response(ctx: interactions.ComponentContext, selection):

        await ctx.send(f"You selected {selection[0]}. Great choice!")
        await ctx.send("**you have a few options. select the one that interests you __or__**")
        if selection[0] == "history":
            second_button_label = "Official Webpage"
        else:
            second_button_label = "Buy now!"
        resources = get_two_recourses(selection[0])
        i = 0
        msgs: [interactions.Message]
        for entity in resources:
            i = i + 1
            # custom_id_interested = f"{ctx.author.id}.{entity['title']}.interested"
            # custom_id_buy_now = f"{ctx.author.id}.{entity['title']}.buyNow"
            button = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=f"I'm interested in {' '.join(entity['title'].split()[:15])}",
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )
            button2 = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=second_button_label,
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )
            # button_ids_dict.update({ctx.author: custom_id_interested})
            await ctx.channel.send(
                    f"Title: {entity['title']}\n"
                    f"Date:  {entity['date']}\n"
                    f"Description:  {' '.join(str(entity['description']).split()[:20])}. . .",
                    files=interactions.File(
                        entity['cv_image'],
                        fp=get_resource_from_github(f"images/{selection[0]}", entity["cv_image"], False)
                    ),
                    components=[button, button2]
                )


    # @multi_component(button_ids_dict, client)
    # async def resource_selection_response(ctx: interactions.ComponentContext, selection):
    #     pass
    #
    @client.component("interested")
    @client.component("buyOrGoto")
    async def resource_selection_response(ctx: interactions.ComponentContext):
        sq = "'"
        if ctx.data.custom_id.startswith("I'm interested in"):
            prefix = "I'm interested in'"
            await ctx.send(f"oh wow, you're interested knowing more about {ctx.data.custom_id.removeprefix(prefix)}! that's a really good choice.")
        else:
            await ctx.send(f"oh wow, you're interested in <buying or going> to <selection>! that's a really good choice.")
        time.sleep(.5)
        await ctx.send(f"redirecting you to **<website name>**")


    client.start()

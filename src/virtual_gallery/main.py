import os
import time

import interactions
from dotenv import load_dotenv
from src.virtual_gallery.service.helper_service import get_two_recourses
from src.virtual_gallery.controller.controller import get_resource_from_github
from src.virtual_gallery.service.helper_service import multi_component

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
        await msg.send("Welcome to the interactive virtual reality experience. "
                       "For a list of commands use the ``/help`` command")
        time.sleep(2)
        options = interactions.SelectMenu(
            custom_id="genre_select",
            options=[
                interactions.SelectOption(custom_id="custom_id_history", label="History",
                                          value="value_History", decription="description_history"),

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

        await ctx.send("**you have a few options. select the one that interests you?**")
        resources = get_two_recourses(selection[0])
        i = 0
        for entity in resources:
            i = i + 1
            custom_id = f"{ctx.author.id}.{entity['title']}"
            button = interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id=custom_id,
                label=f"I'm interested in {entity['title']}"
            )
            button_ids_dict.update({ctx.author:custom_id})
            await ctx.channel.send(
                f"Title: {entity['title']}\n"
                f"Date:  {entity['date']}\n"
                f"Description:  {' '.join(str(entity['description']).split()[:20])}. . .",
                files=interactions.File(
                    entity['cv_image'],
                    fp=get_resource_from_github(f"images/{selection[0]}", entity["cv_image"], False)
                ),
                components=button
            )

    # @multi_component(button_ids_dict, client)
    # async def resource_selection_response(ctx: interactions.ComponentContext, selection):
    #     await ctx.send(f"oh wow, you're interested in {selection}, that's a really good choice")
    #     for value in button_ids_dict.values():
    #         if str(value).startswith(ctx.author.id.)
    #
    # client.start()

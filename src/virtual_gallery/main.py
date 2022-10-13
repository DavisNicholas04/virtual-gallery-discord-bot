import os
import time

import interactions
from dotenv import load_dotenv
from src.virtual_gallery.service.helper_service import get_two_recourses
from src.virtual_gallery.controller.controller import get_resource_from_github

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

        await ctx.send("**you have a few options. Do any of these interest you?**")
        resources = get_two_recourses(selection[0])
        for entity in resources:
            await ctx.channel.send(
                f"Title: {entity['title']}\n"
                f"Date:  {entity['date']}\n"
                f"Description:  {' '.join(str(entity['description']).split()[:20])}. . .",
                files=interactions.File(
                    entity['cv_image'],
                    fp=get_resource_from_github(f"images/{selection[0]}", entity["cv_image"], False)
                )
            )


    client.start()

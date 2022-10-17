import os
import time

import interactions
from dotenv import load_dotenv
from src.service.helper_service import get_two_recourses
from src.controller.controller import get_resource_from_github

# from src.service.helper_service import multi_component

reroll_button_ids_dict = {}

if __name__ == "__main__":
    load_dotenv()
    intent = interactions.Intents.DEFAULT
    client = interactions.Client(token=os.environ['DISCORD_TOKEN'], intents=intent)


    @client.command(
        name="start",
        description="start the interaction, which will tell the bot to message the user privately",
    )
    async def start(msg: interactions.ComponentContext):
        website_button = interactions.Button(
            style=interactions.ButtonStyle.LINK,
            label="go to website",
            url="https://cs.oswego.edu/~acascen/coursework/Virtual%20Gallery.HTML"
        )
        await msg.send("Welcome to the interactive virtual gallery experience. "
                       "For a list of commands use the ``/help`` command.\n"
                       "You can also go straight to our website here.", components=website_button)
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
        await msg.send(content="select on of the following options", components=options)


    @client.component("genre_select")
    async def select_menu_response(ctx: interactions.ComponentContext, selection):
        reroll_button = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="reroll",
            custom_id="reroll"
        )
        d = await ctx.send(f"You selected {selection[0]}. Great choice!")
        await ctx.send("**you have a few options. select the one that interests you __or__**", components=reroll_button)
        await roll(ctx, selection)


    async def roll(ctx: interactions.ComponentContext, selection):
        if selection[0] == "history":
            second_button_label = "Official Webpage"
        else:
            second_button_label = "Buy now!"
        resources = get_two_recourses(selection[0])
        reroll_button_ids_dict[f"{ctx.user}-selection"] = selection
        i = 0
        msgs: [interactions.Message]
        for entity in resources:
            i = i + 1
            button = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=f"I'm interested in {entity['title'].split()[:15]}",
                url=' '.join(entity['title'].split()[:15])
            )
            button2 = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=second_button_label,
                url=entity["official_link"]
            )
            reroll_button_ids_dict[f"{ctx.user}-{i}"] = \
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


    @client.component("reroll")
    async def reroll(ctx: interactions.ComponentContext):
        reroll_button_ids_dict.get(f"{ctx.user}-{1}").delete()
        reroll_button_ids_dict.get(f"{ctx.user}-{2}").delete()
        selection = reroll_button_ids_dict.get(f"{ctx.user}-selection")
        await roll(ctx, selection)

        reroll_button_ids_dict.pop(f"{ctx.user}-selection")


    client.start()

import os
import time

import interactions
from dotenv import load_dotenv
from src.controller.controller import get_resource_from_github, get_two_recourses

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
    async def start(ctx: interactions.ComponentContext):
        await ctx.defer()
        website_button = interactions.Button(
            style=interactions.ButtonStyle.LINK,
            label="go to website",
            url="https://cs.oswego.edu/~acascen/coursework/Virtual%20Gallery.HTML"
        )
        await   ctx.author.send("Welcome to the interactive virtual gallery experience. "
                       "For a list of commands use the ``/help`` command.\n"
                       "You can also go straight to our website here.", components=website_button)
        await selection_menu(ctx)


    async def selection_menu(ctx: interactions.ComponentContext):
        options = interactions.SelectMenu(
            custom_id="genre_select",
            options=[
                interactions.SelectOption(custom_id="custom_id_history", label="History",
                                          value="history", decription="description_history"),

                interactions.SelectOption(custom_id="custom_id_anime", label="Anime",
                                          value="anime", decription="description_anime"),

                interactions.SelectOption(custom_id="custom_id_games", label="Games",
                                          value="games", decription="description_games")],

            placeholder="select",
        )
        await   ctx.author.send(content="select on of the following options", components=options)

    @client.component("genre_select")
    async def select_menu_response(ctx: interactions.ComponentContext, selection):
        new_options_buttons = [
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="reroll",
                custom_id="reroll"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="change genre",
                custom_id="change_genre"
            )
        ]
        await ctx.author.message.edit(f"You selected {selection[0]}. Great choice!")
        # await   ctx.author.send(f"You selected {selection[0]}. Great choice!")
        await   ctx.author.send("**you have a few options. select the one that interests you.**", components=new_options_buttons)
        await roll(ctx, selection)

    async def roll(ctx: interactions.ComponentContext, selection):
        if selection[0] == "history":
            second_button_label = "Official Webpage"
        else:
            second_button_label = "Buy now!"
        resources = get_two_recourses(selection[0])
        reroll_button_ids_dict[f"{ctx.user}-selection"] = selection
        i = 0
        # msgs: [interactions.Message]
        for entity in resources:
            i = i + 1
            button = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=f"I'm interested in {entity['title'].split()[:15]}",
                url="https://www.cs.oswego.edu/~acascen/coursework/Virtual%20Gallery.HTML"
            )
            button2 = interactions.Button(
                style=interactions.ButtonStyle.LINK,
                label=second_button_label,
                url=entity["official_link"]
            )
            reroll_button_ids_dict[f"{ctx.user}-{i}"] = \
                await ctx.author.send(
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
        new_options_buttons = [
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="reroll",
                custom_id="reroll"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="change genre",
                custom_id="change_genre"
            )
        ]
        new_options_buttons2 = [
            interactions.Button(
                style=interactions.ButtonStyle.SUCCESS,
                label="reroll",
                custom_id="reroll"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="change genre",
                custom_id="change_genre"
            )
        ]
        await ctx.message.edit(components=new_options_buttons)
        await ctx.defer(edit_origin=True)
        msg = await ctx.channel.get_message(reroll_button_ids_dict.get(f"{ctx.user}-{1}").id)
        await msg.delete()
        msg = await ctx.channel.get_message(reroll_button_ids_dict.get(f"{ctx.user}-{2}").id)
        await msg.delete()
        selection = reroll_button_ids_dict.get(f"{ctx.user}-selection")
        reroll_button_ids_dict.pop(f"{ctx.user}-selection")
        reroll_button_ids_dict.pop(f"{ctx.user}-{1}")
        reroll_button_ids_dict.pop(f"{ctx.user}-{2}")
        await roll(ctx, selection)
        await ctx.message.edit(components=new_options_buttons2)

    @client.component("change_genre")
    async def change_genre(ctx: interactions.ComponentContext):
        msg = await ctx.channel.get_message(reroll_button_ids_dict.get(f"{ctx.user}-{1}").id)
        await msg.delete()
        msg = await ctx.channel.get_message(reroll_button_ids_dict.get(f"{ctx.user}-{2}").id)
        await msg.delete()
        await ctx.message.delete()
        await selection_menu(ctx)

    @client.command(
        name="end",
        description="ends the interaction, opens an optional survey",
    )
    async def end(ctx: interactions.CommandContext):
        survey = interactions.Modal(
            title="Survey",
            custom_id="survey",
            components=[
                interactions.TextInput(
                    label="username (if you would like a follow-up)",
                    style=interactions.TextStyleType.SHORT,
                    placeholder="username",
                    default="anonymous",
                    max_length=32,
                    custom_id="input1"
                ),
                interactions.TextInput(
                    label="Did you enjoy your experience with us today?",
                    style=interactions.TextStyleType.SHORT,
                    placeholder="yes or no",
                    max_length=3,
                    custom_id="input1"
                ),
                interactions.TextInput(
                    label="If no, why not?",
                    style=interactions.TextStyleType.PARAGRAPH,
                    custom_id="input2",
                    required=False

                ),
                interactions.TextInput(
                    label="How could we improve your experience?",
                    style=interactions.TextStyleType.PARAGRAPH,
                    custom_id="input3",

                ),
                interactions.TextInput(
                    label="Bugs? report them here.",
                    style=interactions.TextStyleType.PARAGRAPH,
                    custom_id="input4",
                    required=False
                ),
            ]
        )
        await ctx.popup(survey)

    @client.modal("survey")
    async def change_genre(ctx: interactions.CommandContext, input1, input2, input3, input4):
        logs = await interactions.get(client, interactions.Channel, object_id=int(os.environ["LOGS_CHANNEL"]))
        await logs.send(f"""            
            Did you enjoy your experience with us today?
            **{input1}**
            If no, why not?
            **{input2}**
            How could we improve your experience?
            **{input3}**
            Bugs? report them here.
            **{input4}**
            """)
        await ctx.send("Thank you for filling out the survey. Join us again!")

    client.start()

import os
import interactions
from dotenv import load_dotenv

load_dotenv()
intent = interactions.Intents.DEFAULT
client = interactions.Client(token=os.environ['DISCORD_TOKEN'], intents=intent)

@client.command(
    name="start",
    description="start the interaction, which will tell the bot to message the user privately",
)
async def start(msg: interactions.ComponentContext):
    await msg.send(f"starting virtual gallery with {msg.author.name} in private messages.")
    await msg.author.send("If you're reading this it's already too late for you. "
                          "I'm behind you and won't wait for you to turn around before I swing my axe")
    await msg.author.send("Also, welcome to the interactive virtual reality experience. For a list of commands use the ``/help`` command")
    options = interactions.SelectMenu(
        custom_id="genre_select",
        options=[
            interactions.SelectOption(custom_id="custom_id_history", label="History", value="value_History", decription="description_history"),
            interactions.SelectOption(custom_id="custom_id_anime", label="Anime", value="anime", decription="description_anime"),
            interactions.SelectOption(custom_id="custom_id_games", label="Games", value="games", decription="description_games")],
        placeholder="Choose your experience",
    )
    await msg.author.send(content="choose your genre", components=options)


@client.component("genre_select")
async def select_menu_response(ctx: interactions.ComponentContext, selection):
    await ctx.send(f"You selected {selection[0]}. Great choice. {client.me.guild_id}")

client.start()

import os
import interactions
from dotenv import load_dotenv
# reroll_button_ids_dict = {}


if __name__ == "__main__":
    load_dotenv()
    intent = interactions.Intents.DEFAULT
    client = interactions.Client(token=os.environ['DISCORD_TOKEN'], intents=intent)
    client.load("src.extensions.command_extensions")
    client.load("src.extensions.component_extensions")
    client.load("src.extensions.modal_extensions")
    client.start()

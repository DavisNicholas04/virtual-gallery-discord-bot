import os
import interactions
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    intent = interactions.Intents.DEFAULT
    client = interactions.Client(token=os.environ['DISCORD_TOKEN'], intents=intent)

    # Load extension files to load in appropriate listeners and their corresponding logic.

    # Load listener for slash commands.
    client.load("extensions.command_extensions")

    # load lister for interactive components (buttons & menus)
    client.load("extensions.component_extensions")

    # load modal listener
    client.load("extensions.modal_extensions")
    client.start()

import interactions
import src.service.component_service as cs
import src.components.components as cpnts


class Commands(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="start",
        description="start the interaction, which will tell the bot to message the user privately",
    )
    async def start(self, ctx: interactions.ComponentContext):
        await ctx.send("Thanks! I sent you a private message so lets get started!")
        await ctx.user.send("Welcome to the interactive virtual gallery experience.\n"
                            "You can go straight to our website here.",
                            components=cpnts.website_button)
        await cs.selection_menu(ctx)


def setup(client):
    Commands(client)

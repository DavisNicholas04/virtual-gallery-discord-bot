import interactions
import os


class Modals(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client

        @interactions.extension_modal("survey")
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


def setup(client):
    Modals(client)

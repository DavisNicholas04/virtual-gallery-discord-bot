import interactions
import src.components.components as cpnts
import src.service.component_service as component_service
from src.utils.utils import edit, delete


class Components(interactions.Extension):
    def __init__(self, client):
        self.client: interactions.Client = client
        cs = component_service.ComponentService(self.client, {})

        @self.client.component("genre_select")
        async def select_menu_response(ctx: interactions.ComponentContext, selection):
            new_options_buttons = cpnts.enabled_button_group
            await ctx.message.delete()
            await delete(
                await ctx.send(f"You selected {selection[0]}. Great choice!"),
                delay=5400
            )
            await delete(
                await ctx.send("**you have a few options. select the one that interests you.**",
                               components=new_options_buttons),
                delay=5400
            )
            await cs.roll(ctx, selection)

        @self.client.component("reroll")
        async def reroll(ctx: interactions.ComponentContext):
            await ctx.message.edit(components=cpnts.disabled_button_group)
            await ctx.defer(edit_origin=True)
            await cs.delete_rolls(ctx)
            selection = cs.reroll_button_ids_dict.get(f"{ctx.user}-selection")
            cs.reroll_button_ids_dict.pop(f"{ctx.user}-selection")
            cs.reroll_button_ids_dict.pop(f"{ctx.user}-{0}")
            cs.reroll_button_ids_dict.pop(f"{ctx.user}-{1}")
            await cs.roll(ctx, selection)
            await edit(
                ctx,
                components=cpnts.success_button_group,
                delay=4
            )

        @self.client.component("change_genre")
        async def change_genre(ctx: interactions.ComponentContext):
            await cs.delete_rolls(ctx)
            await ctx.message.delete()
            await component_service.selection_menu(ctx)

        @self.client.component("end")
        async def end_interaction(ctx: interactions.ComponentContext):
            # sends a modal
            await cs.delete_rolls(ctx)
            await ctx.message.delete()
            await ctx.popup(cpnts.survey)


def setup(client):
    Components(client)

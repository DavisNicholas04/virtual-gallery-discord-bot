import time

import interactions
from src.service.github_service import get_resource_from_github, get_two_recourses
import src.components.components as cpnts


class ComponentService(interactions.Extension):
    def __init__(self, client, reroll_button_ids_dict: {}):
        self.client: interactions.Client = client
        self.reroll_button_ids_dict = reroll_button_ids_dict

    async def roll(self, ctx: interactions.ComponentContext, selection):
        # choose second button label base on user selection
        if selection[0] == "history":
            second_button_label = "Official Webpage"
        else:
            second_button_label = "Buy now!"

        resources = get_two_recourses(selection[0])
        self.reroll_button_ids_dict[f"{ctx.user}-selection"] = selection

        for i, entity in enumerate(resources):
            rolls = cpnts.create_roll_buttons(entity, second_button_label)
            self.reroll_button_ids_dict[f"{ctx.user}-{i}"] = \
                await ctx.user.send(
                    f"Title:  {entity['title']}\n"
                    f"Date:  {entity['date']}\n"
                    f"Description:  {' '.join(str(entity['description']).split()[:20])}. . .",
                    files=get_image(entity, selection),
                    components=rolls,
                )

    async def delete_rolls(self, ctx: interactions.ComponentContext):
        """
        find saved roll messages by user_id key saved in dict and delete

        :param ctx: component context sent in the previous interactions.Client.component function
        :return: null
        """
        msg = await ctx.message.get_from_url(
            self.reroll_button_ids_dict.get(f"{ctx.user}-{0}").url,
            client=self.client._http
        )
        await msg.delete()

        msg = await ctx.message.get_from_url(
            self.reroll_button_ids_dict.get(f"{ctx.user}-{1}").url,
            client=self.client._http
        )
        await msg.delete()


def get_image(entity, selection):
    return interactions.File(
        entity['cv_image'],
        fp=get_resource_from_github(f"images/{selection[0]}", entity["cv_image"], False)
    )


async def selection_menu(ctx: interactions.ComponentContext):
    await ctx.user.send(content="select one of the following options", components=cpnts.genre_select)


async def send_edited_button(ctx, new_options_buttons2):
    time.sleep(4)
    await ctx.message.edit(components=new_options_buttons2)

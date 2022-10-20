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
    # @client.command(
    #     name="start",
    #     description="start the interaction, which will tell the bot to message the user privately",
    # )
    # async def start(ctx: interactions.ComponentContext):
    #     await ctx.send("Thanks! I sent you a private message so lets get started!")
    #     await ctx.user.send("Welcome to the interactive virtual gallery experience. "
    #                         "For a list of commands use the ``/help`` command.\n"
    #                         "You can also go straight to our website here.",
    #                         components=cpnts.website_button)
    #     await selection_menu(ctx)


    # async def selection_menu(ctx: interactions.ComponentContext):
    #     await ctx.user.send(content="select one of the following options", components=cpnts.genre_select)


    # @client.component("genre_select")
    # async def select_menu_response(ctx: interactions.ComponentContext, selection):
    #     new_options_buttons = cpnts.enabled_button_group
    #     await ctx.message.delete()
    #     await ctx.send(f"You selected {selection[0]}. Great choice!")
    #     await ctx.send("**you have a few options. select the one that interests you.**", components=new_options_buttons)
    #     await roll(ctx, selection)


    # async def roll(ctx: interactions.ComponentContext, selection):
    #     # choose second button label base on user selection
    #     if selection[0] == "history":
    #         second_button_label = "Official Webpage"
    #     else:
    #         second_button_label = "Buy now!"
    #
    #     resources = get_two_recourses(selection[0])
    #     reroll_button_ids_dict[f"{ctx.user}-selection"] = selection
    #
    #     for i, entity in enumerate(resources):
    #         rolls = cpnts.create_roll_buttons(entity, second_button_label)
    #         reroll_button_ids_dict[f"{ctx.user}-{i}"] = \
    #             await ctx.user.send(
    #                 f"Title:  {entity['title']}\n"
    #                 f"Date:  {entity['date']}\n"
    #                 f"Description:  {' '.join(str(entity['description']).split()[:20])}. . .",
    #                 files=get_image(entity, selection),
    #                 components=rolls,
    #             )


    # def get_image(entity, selection):
    #     return interactions.File(
    #         entity['cv_image'],
    #         fp=get_resource_from_github(f"images/{selection[0]}", entity["cv_image"], False)
    #     )


    # @client.component("reroll")
    # async def reroll(ctx: interactions.ComponentContext):
    #     await ctx.message.edit(components=cpnts.disabled_button_group)
    #     await ctx.defer(edit_origin=True)
    #     await delete_rolls(ctx)
    #     selection = reroll_button_ids_dict.get(f"{ctx.user}-selection")
    #     reroll_button_ids_dict.pop(f"{ctx.user}-selection")
    #     reroll_button_ids_dict.pop(f"{ctx.user}-{0}")
    #     reroll_button_ids_dict.pop(f"{ctx.user}-{1}")
    #     await roll(ctx, selection)
    #     threading.Thread(
    #         target=await send_edited_button(ctx, cpnts.success_button_group)
    #     )


    # async def send_edited_button(ctx, new_options_buttons2):
    #     time.sleep(4)
    #     await ctx.message.edit(components=new_options_buttons2)


    # @client.component("change_genre")
    # async def change_genre(ctx: interactions.ComponentContext):
    #     await delete_rolls(ctx)
    #     await ctx.message.delete()
    #     await selection_menu(ctx)


    # async def delete_rolls(ctx: interactions.ComponentContext):
    #     """
    #     find saved roll messages by user_id key saved in dict and delete
    #
    #     :param ctx: component context sent in the previous interactions.Client.component function
    #     :return: null
    #     """
    #     msg = await ctx.message.get_from_url(
    #         reroll_button_ids_dict.get(f"{ctx.user}-{0}").url,
    #         client=client._http
    #     )
    #     await msg.delete()
    #
    #     msg = await ctx.message.get_from_url(
    #         reroll_button_ids_dict.get(f"{ctx.user}-{1}").url,
    #         client=client._http
    #     )
    #     await msg.delete()

    # @client.modal("survey")
    # async def change_genre(ctx: interactions.CommandContext, input1, input2, input3, input4):
    #     logs = await interactions.get(client, interactions.Channel, object_id=int(os.environ["LOGS_CHANNEL"]))
    #     await logs.send(f"""
    #         Did you enjoy your experience with us today?
    #         **{input1}**
    #         If no, why not?
    #         **{input2}**
    #         How could we improve your experience?
    #         **{input3}**
    #         Bugs? report them here.
    #         **{input4}**
    #         """)
    #     await ctx.send("Thank you for filling out the survey. Join us again!")

    # @client.component("end")
    # async def end_interaction(ctx: interactions.ComponentContext):
    #     await delete_rolls(ctx)
    #     await ctx.message.delete()
    #     await ctx.popup(cpnts.survey)


    client.start()

import os

import interactions

# BUTTONS

website_button = interactions.Button(
    style=interactions.ButtonStyle.LINK,
    label="go to website",
    url=os.environ['WEBSITE_HOME']
)


def create_roll_buttons(entity, second_button_label, selection):
    url = os.environ["WEBSITE_ERROR"]
    if selection == "game":
        url = os.environ['WEBSITE_GAME']
    if selection == "history":
        url = os.environ['WEBSITE_HISTORY']
    if selection == "anime":
        url = os.environ['WEBSITE_ANIME']

    button = interactions.Button(
        style=interactions.ButtonStyle.LINK,
        label=f"I'm interested in {entity['title'].split()[:15]}",
        url=url+entity
    )
    button2 = interactions.Button(
        style=interactions.ButtonStyle.LINK,
        label=second_button_label,
        url=entity["official_link"]
    )
    return [button, button2]
# /-S-T-A-R-T--------------------\
# | re-roll buttons              |
# \------------------------------/


original_rr_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,  # Original re-roll button
    label="reroll",
    custom_id="reroll"
)

disabled_rr_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,  # re-roll button - disabled
    label="reroll",
    custom_id="reroll",
    disabled=True
)

success_rr_button = interactions.Button(
    style=interactions.ButtonStyle.SUCCESS,  # re-roll button - success
    label="reroll",
    custom_id="reroll"
)

original_cg_button = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,  # change genre button
    label="change genre",
    custom_id="change_genre"
)

disabled_cg_button = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,  # disabled change genre button
    label="change genre",
    custom_id="change_genre",
    disabled=True
)

original_ei_button = interactions.Button(  # end interaction button
    style=interactions.ButtonStyle.DANGER,
    label=f"END SESSION",
    custom_id="end"
)

disabled_ei_button = interactions.Button(
    style=interactions.ButtonStyle.DANGER,  # disabled end interaction button
    label=f"END SESSION",
    custom_id="end",
    disabled=True
)

enabled_button_group = [original_rr_button, original_cg_button, original_ei_button]
disabled_button_group = [disabled_rr_button, disabled_cg_button, disabled_ei_button]
success_button_group = [success_rr_button, original_cg_button, original_ei_button]
# /------------------------E-N-D-\
# | re-roll buttons              |
# \------------------------------/

# SELECT MENU
# /-S-T-A-R-T--------------------\
# | genre select select menu     |
# \------------------------------/
history_select = interactions.SelectOption(
    custom_id="custom_id_history",
    label="History",
    value="history",
    decription="description_history"
)

anime_select = interactions.SelectOption(
    custom_id="custom_id_anime",
    label="Anime",
    value="anime",
    decription="description_anime"
)

games_select = interactions.SelectOption(
    custom_id="custom_id_games",
    label="Games",
    value="games",
    decription="description_games"
)

genre_select = interactions.SelectMenu(
    custom_id="genre_select",
    placeholder="select",
    options=[
        history_select,
        anime_select,
        games_select,
    ]
)
# /------------------------E-N-D-\
# | genre select select menu     |
# \------------------------------/

# MODAL
# /-S-T-A-R-T--------------------\
# | survey modal                 |
# \------------------------------/
username_prompt = interactions.TextInput(
    label="username (if you would like a follow-up)",
    style=interactions.TextStyleType.SHORT,
    placeholder="username",
    max_length=32,
    custom_id="input0",
    required=False

)

experience_prompt = interactions.TextInput(
    label="Did you enjoy your experience with us today?",
    style=interactions.TextStyleType.SHORT,
    placeholder="yes or no",
    max_length=3,
    custom_id="input1"
)

experience_exp_prompt = interactions.TextInput(
    label="If no, why not?",
    style=interactions.TextStyleType.PARAGRAPH,
    custom_id="input2",
    max_length=400,
    required=False
)

improve_us_prompt = interactions.TextInput(
    label="could we improve your experience? How?",
    style=interactions.TextStyleType.PARAGRAPH,
    max_length=400,
    custom_id="input3",
)

report_bugs_prompt = interactions.TextInput(
    label="Bugs? report them here.",
    style=interactions.TextStyleType.PARAGRAPH,
    custom_id="input4",
    max_length=700,
    required=False
)

survey = interactions.Modal(
    title="Survey",
    custom_id="survey",
    components=[
        username_prompt,
        experience_prompt,
        experience_exp_prompt,
        improve_us_prompt,
        report_bugs_prompt,
    ]
)
# /------------------------E-N-D-\
# | survey modal                 |
# \------------------------------/

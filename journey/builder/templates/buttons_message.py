from linebot.models import (
    TemplateSendMessage, ButtonsTemplate,
    CarouselColumn, MessageTemplateAction,
    PostbackTemplateAction, URITemplateAction
)

"""
    This template message contains LINE Template message, such as:

        1. Buttons message
        2. Confirm message

    This template just handle one bubble message,
    if you want send more than one bubble message call each function
    as many as bubbles you want to send
"""


def message_buttons(tup_attr, lists_actions):
    alt_text, image_url, title, text = tup_attr
    return TemplateSendMessage(
        alt_text=alt_text,
        template=ButtonsTemplate(
            thumbnail_image_url=image_url,
            title=title,
            text=text,
            actions=buttons_action(lists_actions)
        )
    )


def message_buttons_no_img(tup_attr, lists_actions):
    alt_text, text = tup_attr

    return TemplateSendMessage(
        alt_text=alt_text,
        template=ButtonsTemplate(
            text=text,
            actions=buttons_action(lists_actions)
        )
    )


def buttons_action(lists_actions):
    lists_template_action = []

    for action in lists_actions:
        if action['type'] == "message":
            template_action = MessageTemplateAction(
                label=action['label'],
                text=action['text']
            )
        elif action['type'] == "uri":
            template_action = URITemplateAction(
                label=action['label'],
                uri=action['uri']
            )
        elif action['type'] == "postback":
            template_action = PostbackTemplateAction(
                label=action['label'],
                text=action['text'],
                data=action['data']
            )

        lists_template_action.append(template_action)

    return lists_template_action

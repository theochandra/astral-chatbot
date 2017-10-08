from linebot.models import (
    TemplateSendMessage, CarouselTemplate,
    CarouselColumn, MessageTemplateAction,
    PostbackTemplateAction, URITemplateAction
)


"""
    This template message contains LINE Template message, such as:

        1. Carousel message

    This template just handle one bubble message, 
    if you want send more than one bubble message call each function 
    as many as bubbles you want to send
"""


def message_carousel(alt_text, lists_columns):
    return TemplateSendMessage(
        alt_text=alt_text,
        template=CarouselTemplate(
            columns=lists_columns
        )
    )


def carousel_column_no_img(lists_column):
    lists_template_column = []

    for column in lists_column:
        template_column = CarouselColumn(
            text=column['text'],
            actions=carousel_action(column['actions'])
        )
        lists_template_column.append(template_column)

    return lists_template_column


def carousel_column(lists_column):
    lists_template_column = []

    for column in lists_column:
        template_column = CarouselColumn(
            thumbnail_image_url=column['url'],
            title=column['title'],
            text=column['text'],
            actions=carousel_action(column['actions'])
        )
        lists_template_column.append(template_column)

    return lists_template_column


def carousel_action(lists_actions):
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

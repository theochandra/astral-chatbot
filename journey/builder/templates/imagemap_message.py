from linebot.models import (
    ImagemapSendMessage, BaseSize,
    URIImagemapAction, MessageImagemapAction,
    ImagemapArea
)


"""
    This template message contains LINE Message object, such as:

        1. Imagemap message

    This template just handle one bubble message, 
    if you want send more than one bubble message call each function 
    as many as bubbles you want to send
"""


def message_imagemap(base_url, alt_text, lists_actions):
    return ImagemapSendMessage(
        base_url=base_url,
        alt_text=alt_text,
        base_size=BaseSize(height=1040, width=1040),
        actions=lists_actions
    )


def imagemap_action_uri():
    pass


def imagemap_action_msg(action):
    text = action['text']
    tup_area = (
        action['x'],
        action['y'],
        action['width'],
        action['height']
    )

    return MessageImagemapAction(
        text=text,
        area=imagemap_area(tup_area)
    )


def imagemap_area(tup_area):
    x, y, width, height = tup_area

    return ImagemapArea(
        x=x,
        y=y,
        width=width,
        height=height
    )

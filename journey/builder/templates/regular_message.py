from linebot.models import (
    TextSendMessage, ImageSendMessage,
    VideoSendMessage, LocationSendMessage,
    StickerSendMessage
)


"""
    This template message contains LINE Message object, such as:
    
        1. Text message
        2. Image message
        3. Video message
        4. Audio message
        5. File message
        6. Location message
        7. Sticker message
        
    For now we will focus in develop for number 1, 2, 3, 6 and 7.
    
    This template just handle one bubble message, 
    if you want send more than one bubble message call each function 
    as many as bubbles you want to send
"""


def message_text(message):
    return TextSendMessage(
        text=message
    )


def message_image(tup_url):
    content_url, preview_url = tup_url

    return ImageSendMessage(
        original_content_url=content_url,
        preview_image_url=preview_url
    )


def message_video(tup_url):
    content_url, preview_url = tup_url

    return VideoSendMessage(
        original_content_url=content_url,
        preview_image_url=preview_url
    )


def message_location(tup_location):
    title, address, lat, lon = tup_location

    return LocationSendMessage(
        title=title,
        address=address,
        latitude=lat,
        longitude=lon
    )


def message_sticker(tup_sticker):
    package_id, sticker_id = tup_sticker

    return StickerSendMessage(
        package_id=package_id,
        sticker_id=sticker_id
    )

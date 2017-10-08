import os
import json
from utils.logger import Logger
from journey.builder import build
from journey.controller.request.travel import service


logger = Logger('VIEW BY LOCATION')
logger.get()
logger = logger._logger

filepath = os.path.join('./journey/controller/static', 'string_message.json')
LIST_OF_MESSAGE = []
with open(filepath) as message_file:
    LIST_OF_MESSAGE = json.load(message_file)


def choose_place_by_city(profile, messages, parameters):
    """user choose place filtered by location and category"""
    lists = []
    user_id = profile.user_id
    display_name = profile.display_name

    logger.info("%s - %s choose %s" % (display_name, user_id, parameters['travel-tipe']))

    switcher = {
        'Adventure': show_adventure_place_by_loc,
        'Sweet Escape': show_sweetescape_place_by_loc,
        'Culinary': show_culinary_place_by_loc
    }

    fx = switcher.get(parameters['travel-tipe'], "")(profile, messages, parameters)

    if fx is None:
        logger.error("%s - %s | Data : %s" % (display_name, user_id, fx))
        bubble_text = build.show_text(LIST_OF_MESSAGE['message_error_general'])
        lists.append(bubble_text)
    else:
        lists = fx

    return lists


def show_adventure_place_by_loc(profile, messages, parameters):
    user_id = profile.user_id
    display_name = profile.display_name

    logger.info("%s - %s choose %s" % (display_name, user_id, parameters['tipe-adventure']))
    logger.info("%s - %s choose %s" % (display_name, user_id, parameters['kota']))

    place_type = parameters['tipe-adventure'].lower()
    kota = parameters['kota']
    req_attr = (kota, 'chat', place_type, "", "", "", "", "", user_id)

    lists_data_carousel = service.get_adventure(req_attr)

    lists = build_message(user_id, display_name, messages, lists_data_carousel)

    return lists


def build_message(user_id, display_name, messages,  lists_data_carousel):
    lists = []

    key = 'errorCode'
    if key in lists_data_carousel:
        logger.error("%s - %s | Data : %s" % (display_name, user_id, lists_data_carousel))
        bubble_text = build.show_text(LIST_OF_MESSAGE['message_error_datanotfound_city'])
        lists.append(bubble_text)
    else:
        attr_action = ('message', 'View Detail', 'place_name')
        attr_column = ('url_image', 'place_name', 'short_desc')
        lists_columns = build.populate_carousel_img(lists_data_carousel, attr_action, attr_column, None)

        alt_text = LIST_OF_MESSAGE['alt_recommended']
        bubble_carousel = build.show_carousel_with_img(alt_text, lists_columns)

        if len(messages) > 0:
            bubble_text = build.show_text(messages[0]['speech'])

        lists.append(bubble_text)
        lists.append(bubble_carousel)

    return lists


def show_sweetescape_place_by_loc(profile, messages, parameters):
    pass


def show_culinary_place_by_loc(profile, messages, parameters):
    pass

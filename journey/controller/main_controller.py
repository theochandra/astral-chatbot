import json
import os.path
import sys

from journey.builder import build
from journey.controller.request.travel import service
from journey.controller.static import static_data as data
from utils.switcher import Switch
from utils.logger import Logger
import recommended
import view_by_location


logger = Logger('MAIN CONTROLLER')
logger.get()
logger = logger._logger

filepath = os.path.join('./journey/controller/static', 'string_message.json')
MESSAGE = []
with open(filepath) as message_file:
    MESSAGE = json.load(message_file)

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


# switch = Switch
CLIENT_ACCESS_TOKEN = data.apiai_client_access_token


def call_api_ai(query, session):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()
    request.lang = data.apiai_lang
    request.session_id = session
    request.query = query

    return request.getresponse()


def select_journey_process(message_from_user, profile, user_timestamp):
    user_id = profile.user_id
    display_name = profile.display_name
    status_message = profile.status_message
    
    logger.info("%s - %s | chat content : %s | with status : %s"
                % (display_name, user_id, message_from_user, status_message))

    response = call_api_ai(message_from_user, user_id)
    data_json = json.loads(response.read())

    intent = data_json['result']['metadata']['intentName']
    messages = data_json['result']['fulfillment']['messages']
    parameters = data_json['result']['parameters']

    logger.info("%s - %s | Intent: %s" % (display_name, user_id, intent))
    logger.info("%s - %s | Parameters: %s" % (display_name, user_id, parameters))

    switcher = {
        "main-menu"                 : show_main_menu,
        "travel"                    : choose_travel,
        "travel-tipe"               : choose_tipe_travel,
        "travel-tipe-adventure"     : choose_tipe_adventure,
        "travel-tipe-sweetescape"   : choose_tipe_sweetescape,
        "travel-tipe-culinary"      : choose_tipe_culinary,
        "travel-location"           : choose_location,
        "travel-location-province"  : choose_province,
        "travel-city"               : view_by_location.choose_place_by_city,
        "travel-recommended"        : recommended.choose_recommended,
        "travel-hiking"             : view_detail_hiking,
        "Cute"                      : "",
        "discover"                  : discover,
        "Default Fallback Intent"   : fallback_intent,
    }

    fx = switcher.get(intent, "")(profile, messages, parameters)

    return fx


def show_main_menu(profile, messages, parameters):
    actions = data.menu_action_button
    attr = (MESSAGE['alt_choose_menu'], MESSAGE['message_choose_menu'])
    lists = buttons_response(actions, messages, attr)

    return lists


def choose_travel(profile, messages, parameters):
    """show carousel of travel type when user hit travel with astral"""
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE MENU TRAVEL'

    lists = []

    lists_data_carousel = data.lists_tipe_travel
    attr_action = ('message', 'Pilih', 'title')
    attr_column = ('url', 'title', 'text')
    lists_columns = build.populate_carousel_img(lists_data_carousel, attr_action, attr_column, None)

    bubble_text_1 = build.show_text(messages[0]['speech'])
    lists.append(bubble_text_1)

    alt_text = MESSAGE['alt_choose_travel_tipe']
    bubble_carousel = build.show_carousel_with_img(alt_text, lists_columns)
    lists.append(bubble_carousel)

    bubble_text_2 = build.show_text(messages[1]['speech'])
    lists.append(bubble_text_2)

    return lists


def choose_tipe_travel(profile, messages, parameters):
    """show button or imagemap when user choose travel type"""
    lists = []
    for case in Switch(parameters['travel-tipe']):
        print 'ASTRAL - CLASS CONTROL - USER CHOOSE %s' % parameters['travel-tipe'].upper()

        if case('Adventure'):
            base_url = data.url_imagemap_adventure
            alt_text = MESSAGE['alt_choose_adventure_tipe']
            attr = (base_url, alt_text)

            actions = data.lists_imagemap_adventure

            bubble_imagemap = build.show_imagemap(attr, actions)
            bubble_text = build.show_text(messages[0]['speech'])

            lists.append(bubble_text)
            lists.append(bubble_imagemap)

            return lists
            break
        if case('Sweet Escape'):
            base_url = data.url_imagemap_sweetescape
            alt_text = MESSAGE['alt_choose_sweetescape_tipe']
            attr = (base_url, alt_text)

            actions = data.lists_imagemap_sweetescape

            bubble_imagemap = build.show_imagemap(attr, actions)
            bubble_text = build.show_text(messages[0]['speech'])

            lists.append(bubble_text)
            lists.append(bubble_imagemap)

            return lists
            break
        if case('Leisure'):
            print 'Leisure'
            break
        if case('Culinary'):
            base_url = data.url_imagemap_culinary
            alt_text = MESSAGE['alt_choose_culinary_tipe']
            attr = (base_url, alt_text)

            actions = data.lists_imagemap_culinary

            bubble_imagemap = build.show_imagemap(attr, actions)
            bubble_text = build.show_text(messages[0]['speech'])

            lists.append(bubble_text)
            lists.append(bubble_imagemap)

            return lists
            break
        if case():
            print "This is default"
    
    return lists


def choose_tipe_adventure(profile, messages, parameters):
    """show button when user choose adventure type or main menu button"""
    # lists = []
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE %s' % parameters['tipe-adventure'].upper()

    actions = data.three_action_button
    attr = ("Pilih salah satu dari button di bawah ini", "Silahkan pilih")

    lists = buttons_response(actions, messages, attr)

    return lists


def choose_tipe_sweetescape(profile, messages, parameters):
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE %s' % parameters['tipe-sweetescape'].upper()

    actions = data.three_action_button
    attr = ("Pilih salah satu dari button di bawah ini", "Silahkan pilih")

    lists = buttons_response(actions, messages, attr)

    return lists


def choose_tipe_culinary(profile, messages, parameters):
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE %s' % parameters['tipe-culinary'].upper()

    actions = data.three_action_button
    attr = ("Pilih salah satu dari button di bawah ini", "Silahkan pilih")

    lists = buttons_response(actions, messages, attr)

    return lists


def buttons_response(data_actions, messages, attr):
    lists = []

    bubble_text = build.show_text(messages[0]['speech'])
    lists.append(bubble_text)

    bubble_buttons = build.show_buttons_no_img(attr, data_actions)
    lists.append(bubble_buttons)

    return lists


def choose_location(profile, messages, parameters):
    """user choose view by location, Astral will provide province"""
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE VIEW BY LOCATION'

    lists = []
    user_id = profile.user_id
    key = 'province'
    type = 'chat'
    attr_action = ('province', 'province')
    attr_column = [
        {
            'url': ' ',
            'title': ' ',
            'text': 'Silahkan pilih salah satu provinsi di bawah ini ya'
        }
    ]
    dict_province = service.get_province(key, type, user_id)

    lists_columns = build.populate_carousel(dict_province, attr_column, attr_action)

    alt_text = 'Silahkan pilih provinsi terlebih dahulu'
    bubble_carousel = build.show_carousel_no_img(alt_text, lists_columns)
    lists.append(bubble_carousel)

    return lists


def choose_province(profile, messages, parameters):
    """user chose province, Astral will provide cities from that province"""
    print 'ASTRAL - CLASS CONTROL - USER CHOOSE %s' % parameters['provinsi'].upper()

    lists = []
    user_id = profile.user_id
    display_name = profile.display_name
    type = 'chat'
    provinsi = parameters['provinsi']
    place_sub_type = parameters['travel-tipe']
    place_type = ''

    if parameters['travel-tipe'] == 'Adventure':
        place_type = parameters['tipe-adventure']
    elif parameters['travel-tipe'] == 'Sweet Escape':
        place_type = parameters['tipe-sweetescape']
    elif parameters['travel-tipe'] == 'Culinary':
        place_type = parameters['tipe-culinary']
    else:
        pass

    dict_city = service.get_city(provinsi, type, user_id, place_type, place_sub_type)

    if dict_city is None:
        logger.error("%s - %s | Data : %s" % (display_name, user_id, dict_city))
        bubble_text = build.show_text(MESSAGE['message_error_general'])
        lists.append(bubble_text)
    else:
        key = 'errorCode'
        if key in dict_city:
            logger.error("%s - %s | Data : %s" % (display_name, user_id, dict_city))
            bubble_text = build.show_text(MESSAGE['message_error_datanotfound_city'])
            lists.append(bubble_text)
        else:
            attr_action = ('city', 'city')
            attr_column = [
                {
                    'url': ' ',
                    'title': ' ',
                    'text': 'Silahkan pilih lokasi yang ingin kamu kunjungi'
                }
            ]

            lists_columns = build.populate_carousel(dict_city['cities'], attr_column, attr_action)
            alt_text = 'Silahkan pilih lokasi terlebih dahulu'
            bubble_carousel = build.show_carousel_no_img(alt_text, lists_columns)

            bubble_text = build.show_text(dict_city['text'])

            lists.append(bubble_text)
            lists.append(bubble_carousel)

    return lists


def view_detail_hiking(user_id, messages, parameters):
    pass


def discover(profile, messages, parameters):
    lists = []
    data_actions = [
        {
            "type" : "uri",
            "label": "tes",
            "uri" : "https://preview.c9users.io/theochandra27/astral/templates/story/index.html"
        }
    ]
    attr = ("Pilih salah satu dari button di bawah ini", "Silahkan pilih")
        
    bubble_buttons = build.show_buttons_no_img(attr, data_actions)
    lists.append(bubble_buttons)

    return lists
        

def fallback_intent(profile, messages, parameters):
    lists = []
    bubble_text = build.show_text(messages[0]['speech'])
    lists.append(bubble_text)
    return lists
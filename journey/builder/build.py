import json
from journey.builder.templates import buttons_message as buttons, carousel_message as carousel, \
    imagemap_message as imagemap, regular_message as regular


def show_text(message):
    bubble_text = regular.message_text(message)

    return bubble_text


# TODO need to fix show_imagemap
def show_imagemap(attr, lists_actions):
    list_of_action = []
    base_url, alt_text = attr

    for action in lists_actions:
        list_of_action.append(imagemap.imagemap_action_msg(action))

    bubble_imagemap = imagemap.message_imagemap(base_url, alt_text, list_of_action)

    return bubble_imagemap


def show_carousel_with_img(alt_text, lists_columns):
    carousel_column = carousel.carousel_column(lists_columns)
    bubble_carousel = carousel.message_carousel(alt_text, carousel_column)
    return bubble_carousel


def show_carousel_no_img(alt_text, lists_columns):
    carousel_column = carousel.carousel_column_no_img(lists_columns)
    bubble_carousel = carousel.message_carousel(alt_text, carousel_column)
    return bubble_carousel


def show_buttons(tup_attr, lists_actions):
    bubble_buttons = buttons.message_buttons(tup_attr, lists_actions)
    return bubble_buttons


def show_buttons_no_img(tup_attr, lists_actions):
    bubble_buttons = buttons.message_buttons_no_img(tup_attr, lists_actions)
    return bubble_buttons


def populate_carousel_img(lists_data_carousel, attr_action, attr_column, lists_postback):
    lists_columns = []
    action_type, action_label, action_text = attr_action
    column_url, column_title, column_text = attr_column

    j = 0
    for data_carousel in lists_data_carousel:
        lists_actions = []

        for i in range(0, 3):
            dict_actions = {}
            if i == 1:
                if action_type == 'postback':
                    json_postpack = json.dumps(lists_postback[j])
                    dict_actions['type'] = action_type
                    dict_actions['label'] = action_label
                    dict_actions['text'] = data_carousel[action_text]
                    dict_actions['data'] = json_postpack
                else:
                    dict_actions['type'] = action_type
                    dict_actions['label'] = action_label
                    dict_actions['text'] = data_carousel[action_text]
            else:
                dict_actions['type'] = 'message'
                dict_actions['label'] = ' '
                dict_actions['text'] = ' '

            lists_actions.append(dict_actions)
        j += 1
        dict_column = {
            'url': data_carousel[column_url],
            'title': data_carousel[column_title],
            'text': data_carousel[column_text],
            'actions': lists_actions
        }
        lists_columns.append(dict_column)

    return lists_columns


# data carousel should be dictionary
def populate_carousel(object_carousel, attr_column, attr_action):
    print "PANJANG DATA ::: ", len(object_carousel)
    label, text_action = attr_action

    dict_of_format = format_of_carousel(len(object_carousel))
    sum_of_carousel = dict_of_format['sum_of_carousel']
    sum_of_button = dict_of_format['sum_of_button']

    lists_columns = []
    k = 0
    for i in range(0, sum_of_carousel):
        lists_actions = []
        # build action buttons first
        for j in range(0, 3):
            dict_actions = {}
            if j < sum_of_button:
                if k >= len(object_carousel):
                    dict_actions['type'] = 'message'
                    dict_actions['label'] = ' '
                    dict_actions['text'] = ' '
                else:
                    data = object_carousel[k]
                    dict_actions['type'] = 'message'
                    # has_attr = getattr(data, label, None)
                    # if has_attr is not None:
                    #     dict_actions['label'] = data[label]
                    # else:
                    #     dict_actions['label'] = label
                    dict_actions['label'] = data[label]
                    dict_actions['text'] = data[text_action]

                k += 1
            else:
                dict_actions['type'] = 'message'
                dict_actions['label'] = ' '
                dict_actions['text'] = ' '

            lists_actions.append(dict_actions)

        # build column
        if len(attr_column) < sum_of_carousel:
            dict_column = {
                'url': attr_column[0]['url'],
                'title': attr_column[0]['title'],
                'text': attr_column[0]['text'],
                'actions': lists_actions
            }
        else:
            dict_column = {
                'url': attr_column[i]['url'],
                'title': attr_column[i]['title'],
                'text': attr_column[i]['text'],
                'actions': lists_actions
            }
        lists_columns.append(dict_column)

    return lists_columns


def format_of_carousel(len_data_carousel):
    switch = {
        1: {
            "sum_of_carousel": 1,
            "sum_of_button": 1
        },
        2: {
            "sum_of_carousel": 2,
            "sum_of_button": 1
        },
        3: {
            "sum_of_carousel": 3,
            "sum_of_button": 1
        },
        4: {
            "sum_of_carousel": 4,
            "sum_of_button": 1
        },
        5: {
            "sum_of_carousel": 5,
            "sum_of_button": 1
        },
        6: {
            "sum_of_carousel": 3,
            "sum_of_button": 2
        },
        7: {
            "sum_of_carousel": 4,
            "sum_of_button": 2
        },
        8: {
            "sum_of_carousel": 4,
            "sum_of_button": 2
        },
        9: {
            "sum_of_carousel": 3,
            "sum_of_button": 3
        },
        10: {
            "sum_of_carousel": 5,
            "sum_of_button": 2
        },
        11: {
            "sum_of_carousel": 4,
            "sum_of_button": 3
        },
        12: {
            "sum_of_carousel": 4,
            "sum_of_button": 3
        },
        13: {
            "sum_of_carousel": 5,
            "sum_of_button": 3
        },
        14: {
            "sum_of_carousel": 5,
            "sum_of_button": 3
        },
        15: {
            "sum_of_carousel": 5,
            "sum_of_button": 3
        },
    }

    format = switch.get(len_data_carousel, lambda: "nothing")

    return format
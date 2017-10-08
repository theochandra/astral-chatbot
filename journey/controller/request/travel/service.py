import requests
import json
import init_end_point as init
from utils.logger import Logger


logger = Logger('SERVICE')
logger.get()
logger = logger._logger

init.initialize_end_point()

END_POINT = init.END_POINT


def get_province(key, type, user_id):
    path = END_POINT['path_inq_province']
    # path = "/province/inquiry"
    req_body = {
        "key": key,
        "typeDevice": type,
        "userIDLine": user_id
    }
    data = get_data_request(req_body, path)
    if data is not None:
        dict_data = json.loads(data)
        if dict_data['output']['header']['errorCode'] == '00':
            return dict_data['output']['body']
        else:
            return dict_data['output']['header']
    else:
        return None


def get_city(provinsi, type, user_id, place_type, place_sub_type):
    path = END_POINT['path_inq_city']
    # path = "/city/inquiry"
    req_body = {
        "province": provinsi,
        "typeDevice": type,
        "userIDLine": user_id,
        "placeType": place_type.lower(),
        "placeSubType": place_sub_type.lower()
    }
    data = get_data_request(req_body, path)
    print data
    if data is not None:
        dict_data = json.loads(data)
        if dict_data['output']['header']['errorCode'] == '00':
            return dict_data['output']['body'][0]
        else:
            return dict_data['output']['header']
    else:
        return None


def get_adventure(req_attr):
    city, type, place_type, place_id, place_sub_type,\
        recommended_flag, nearby_flag, detail_flag, user_id = req_attr
    path = END_POINT['path_inq_adventure']
    # path = "/adventure/inquiry"
    req_body = {
        "city": city,
        "typeDevice": type,
        "placeType": place_type,
        "placeID": place_id,
        "placeSubType": place_sub_type,
        "recommendedFlag": recommended_flag,
        "nearByFlag": nearby_flag,
        "detailFlag": detail_flag,
        "userIDLine": user_id
    }
    data = get_data_request(req_body, path)
    if data is not None:
        dict_data = json.loads(data)
        if dict_data['output']['header']['errorCode'] == '00':
            return dict_data['output']['body']
        else:
            return dict_data['output']['header']
    else:
        return None


def get_data_request(req_body, path):
    end_point = END_POINT['url_service'] + path
    logger.info("Request to end point: %s" % end_point)
    logger.info("Request body : %s" % req_body)
    try:
        req = requests.post(
            end_point,
            # "https://rest-astral-hannyptr.c9users.io"+path,
            json=req_body,
            timeout=10
        ).content
        logger.info("Response from %s ::: %s" % (end_point, json.dumps(req)))
        return req
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        logger.error("Timeout ::: %s" % e)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        logger.error("Error ::: %s" % e)

# print get_city("Jakarta", "chat", "Uddd7b74d41b77a2b968c8e0d6810cdb7", "hiking", "adventure")
# print get_province("province", "chat", "Uddd7b74d41b77a2b968c8e0d6810cdb7")
# req_attr = ('Garut', 'chat', 'hiking',
#                 "", "", "", "", "", 'Uddd7b74d41b77a2b968c8e0d6810cdb7')
# print get_adventure(req_attr)
import os
import json

END_POINT = []
filepath_end_point = os.path.join('./journey/controller/request/travel', 'end_point.json')


def initialize_end_point():
    global END_POINT
    
    with open(filepath_end_point) as end_point_json:
        END_POINT = json.load(end_point_json) 
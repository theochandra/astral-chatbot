import os
import json

LINE_KEY = []
LIST_OF_MESSAGE = []

# use ../config when run this file only
# use ./config when run from astral.py
filepath_line_key = os.path.join('./config', 'line_key.json')
filepath_template_message = os.path.join('./config', 'pre_defined_messages.json')

def initialize_line_key():
    
    global LINE_KEY
    
    with open(filepath_line_key) as line_key_file:
        LINE_KEY = json.load(line_key_file)
        
def initialize_messages():
    
    global LIST_OF_MESSAGE
    
    with open(filepath_template_message) as message_file:
        LIST_OF_MESSAGE = json.load(message_file)
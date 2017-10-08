import os
import json

LINE_KEY = []

filepath = os.path.join('../config', 'line_key.json')

if not os.path.exists('../config'):
    print "folder not exist"
else:
    print "folder exist"

def initialize_line_key():
    
    global LINE_KEY
    
    with open(filepath) as line_key_file:
        LINE_KEY = json.load(line_key_file)
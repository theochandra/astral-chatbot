import json
import os
from init import init_config
from journey.controller import main_controller
from flask import Flask, request, abort, jsonify
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, PostbackEvent
)


astral = Flask(__name__)

init_config.initialize_line_key()
line_key = init_config.LINE_KEY


line_bot_api = LineBotApi(line_key['channel_access_token'])
handler = WebhookHandler(line_key['channel_secret']) 


@astral.route('/')
def hello_from_astral():
    print "Hello this is Astral"


@astral.route('/chat', methods=['POST'])
def chat():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        
    return 'OK'
    
    
# when the event is an instance of MessageEvent and event.message 
# is an instance of TextMessage, this handler method is called 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    
    lists = main_controller.select_journey_process(event.message.text, profile, event.timestamp)
    
    if lists is not None:
        line_bot_api.reply_message(
            event.reply_token,
            lists
        )
    else:
        pass


@handler.add(PostbackEvent)
def handle_postback(event):
    print "POSTBACK EVENT ::: ", event
    

# default handler
# If there is no handler for an event, this default handler method is called
@handler.default()
def default(event):
    print "EVENT : ", event
    

if __name__ == '__main__':
    astral.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
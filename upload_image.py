import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/upload_image')
def hello_world():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8081)))
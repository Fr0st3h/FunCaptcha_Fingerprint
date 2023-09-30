
from flask import Flask, render_template, request
import base64
import random
import string
import json

app = Flask(__name__)

#By Fr0st3h

@app.route('/memes', methods=['POST'])
def get_names():
    fileName = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
    with open(f'bdas/{fileName}.json', 'w') as f:
        f.write(json.dumps(json.loads(base64.b64decode(request.get_data()).decode()), indent = 4))
    print("Got Fingerprint")
    return '', 200

@app.route('/')
def hello_world():
    return render_template('funcapmeme.html')

if __name__ == '__main__':

    app.run('0.0.0.0', debug=True)
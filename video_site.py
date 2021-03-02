from flask import Flask, render_template, request
from random import randint
import json


app = Flask(__name__, static_folder='data')


def some():
    print('sdffds')


@app.route('/')
def base(file_num):
    f = f'video/{file_num}.mp4'
    return render_template('index.html', file=str(f))

'''
РОМА ЧТО-ТО НАПИСАЛ
@app.route('/update', methods=['GET'])
def update(f='2.mp4'):
    some()
    f = f'{randint(1, 2)}.mp4'
    return render_template('index.html', file=str(f))


@app.route('/something', methods=['POST'])
def something_post():
    # Get JSON object passed with Ajax request
    elems = request.json
    # Do stuff
    # If everithing is OK, return success message
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
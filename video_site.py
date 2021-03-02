from flask import Flask, render_template, request, redirect
from main import get_lenght, make_pause, count
from random import randint
import json


app = Flask(__name__, static_folder='data')


def some():
    print('sdffds')


@app.route('/')
def index():
    print('идёт фильм')
    print('выбор')

    # id = count()
    id = 2
    if id == 1:
        duration = get_lenght(1)
        make_pause(duration)
        print('бежим на право')
        return redirect('/update/1')
    elif id == 2:
        return redirect('/update/2')
        duration = get_lenght(2)
        make_pause(duration)
        print('бежим на лево')
    else:
        print('АААААААА')


@app.route('/update/<int:file_num>')
def update(file_num):
    f = f'{file_num}.mp4'
    return render_template('index.html', file=str(f))

'''
РОМА ЧТО-ТО НАПИСАЛ


@app.route('/something', methods=['POST'])
def something_post():
    # Get JSON object passed with Ajax request
    elems = request.json
    # Do stuff
    # If everithing is OK, return success message
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

print('идёт фильм')
print('выбор')

# id = count()
id = 2
if id == 1:
    duration = get_lenght(1)
    make_pause(duration)
    print('бежим на право')
elif id == 2:
    duration = get_lenght(2)
    make_pause(duration)
    print('бежим на лево')
else:
    print('АААААААА')
'''
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
from flask import Flask, render_template


app = Flask(__name__, static_folder='data')


def some():
    print('sdffds')


@app.route('/')
def index(f='1.mp4'):
    some()
    return render_template('index.html', file=str(f))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
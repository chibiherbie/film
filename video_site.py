from flask import Flask, render_template


app = Flask(__name__, static_folder='data')


@app.route('/')
def index(f='1.mp4'):
    return render_template('index.html', file=str(f))
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return None

@app.route('/user')
def user():
    return None

@app.route('/config')
def config():
    return None


if __name__ =='__main__':
    app.run(debug=True)

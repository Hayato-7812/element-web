from flask import Flask,render_template, redirect, request
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

    
# 画像の表示

@app.route('/show_pic')
def game():
    return render_template('game.html')

app.run(port=8000, debug=True)


from flask import Flask, render_template, request, redirect
from strategy import start_algo
import os

app = Flask(__name__)
algo_running = False

@app.route('/')
def index():
    return render_template('index.html', status=algo_running)

@app.route('/start', methods=['POST'])
def start():
    global algo_running
    if not algo_running:
        algo_running = True
        start_algo()
    return redirect('/')

@app.route('/stop', methods=['POST'])
def stop():
    global algo_running
    algo_running = False
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from strategy import start_algo
import threading

app = Flask(__name__)
algo_running = False

def run_algo():
    start_algo()

@app.route('/')
def index():
    return render_template('index.html', status=algo_running)

@app.route('/start', methods=['POST'])
def start():
    global algo_running
    if not algo_running:
        algo_running = True
        threading.Thread(target=run_algo).start()
    return redirect('/')

@app.route('/stop', methods=['POST'])
def stop():
    global algo_running
    algo_running = False
    return redirect('/')
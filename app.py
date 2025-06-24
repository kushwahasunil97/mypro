from flask import Flask, render_template, request, redirect
from strategy import start_algo
import threading
import os

app = Flask(__name__)

algo_running = False
TRADING_MODE = os.getenv("TRADING_MODE", "SIMULATED")  # Default mode from env

def run_algo():
    # Pass the mode to strategy
    start_algo(TRADING_MODE)

@app.route('/')
def index():
    return render_template('index.html', status=algo_running, trading_mode=TRADING_MODE)

@app.route('/set_mode', methods=['POST'])
def set_mode():
    global TRADING_MODE
    mode = request.form.get("mode")
    TRADING_MODE = mode
    return redirect('/')

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
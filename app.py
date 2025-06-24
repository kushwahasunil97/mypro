from flask import Flask, render_template, request, redirect
from strategy import start_algo
from login import login  # Angel SmartAPI से login
import threading
import os

app = Flask(__name__)

algo_running = False
TRADING_MODE = os.getenv("TRADING_MODE", "SIMULATED")  # Default mode from env

# 🔹 Get live balance from Angel One SmartAPI
def get_live_balance():
    try:
        smartapi = login()
        if smartapi is None:
            return None
        funds = smartapi.rms_funds()
        return float(funds['data']['availablecash'])
    except Exception as e:
        print("❌ Error fetching balance:", e)
        return None

# 🔹 Algo thread starter
def run_algo():
    start_algo(TRADING_MODE)

# 🔹 Home route (Dashboard)
@app.route('/')
def index():
    balance = get_live_balance()
    return render_template('index.html',
        status=algo_running,
        trading_mode=TRADING_MODE,
        balance=balance
    )

# 🔹 Mode change
@app.route('/set_mode', methods=['POST'])
def set_mode():
    global TRADING_MODE
    TRADING_MODE = request.form.get("mode")
    return redirect('/')

# 🔹 Start algo
@app.route('/start', methods=['POST'])
def start():
    global algo_running
    if not algo_running:
        algo_running = True
        threading.Thread(target=run_algo).start()
    return redirect('/')

# 🔹 Stop algo
@app.route('/stop', methods=['POST'])
def stop():
    global algo_running
    algo_running = False
    return redirect('/')
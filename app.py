from flask import Flask, render_template, request, redirect
from strategy import start_algo
from login import login  # Angel SmartAPI से login (new SDK compatible)
import threading
import os

app = Flask(__name__)
algo_running = False

# 🔹 Load trading mode from environment (default SIMULATED)
TRADING_MODE = os.getenv("TRADING_MODE", "SIMULATED").upper()


# 🔹 Get live balance from Angel One
def get_live_balance():
    try:
        smartapi = login()
        if smartapi is None:
            return None
        funds = smartapi.rms()
        return float(funds['data']['availablecash'])
    except Exception as e:
        print("❌ Error fetching balance:", e)
        return None


# 🔹 Algo Thread Function
def run_algo():
    start_algo(TRADING_MODE)


# 🔹 Home Dashboard
@app.route('/')
def index():
    balance = get_live_balance()
    return render_template(
        'index.html',
        status=algo_running,
        trading_mode=TRADING_MODE,
        balance=balance
    )


# 🔹 Change Trading Mode (REAL / SIMULATED)
@app.route('/set_mode', methods=['POST'])
def set_mode():
    global TRADING_MODE
    mode = request.form.get("mode", "SIMULATED").upper()
    if mode in ["REAL", "SIMULATED"]:
        TRADING_MODE = mode
    return redirect('/')


# 🔹 Start Algo Button
@app.route('/start', methods=['POST'])
def start():
    global algo_running
    if not algo_running:
        algo_running = True
        threading.Thread(target=run_algo, daemon=True).start()
    return redirect('/')


# 🔹 Stop Algo Button
@app.route('/stop', methods=['POST'])
def stop():
    global algo_running
    algo_running = False
    return redirect('/')


# 🔹 Only run locally
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
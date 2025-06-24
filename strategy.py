import time
from order_manager import place_order
from risk_control import check_loss_limit

def start_algo(mode):
    loss_count = 0

    print(f"🚀 Algo Started in {mode} Mode")

    while True:
        if check_loss_limit():
            print("🔴 Loss limit reached. Stopping Algo.")
            break

        signal = "BUY_CALL"  # यहाँ VWAP logic आएगा

        if signal:
            if mode == "REAL":
                result = place_order(signal)
            else:
                result = simulate_order(signal)

            if result == "LOSS":
                loss_count += 1
                print(f"❌ Loss {loss_count}/2")

            if loss_count >= 2:
                print("🔴 2 Loss हो चुके हैं। Algo बंद किया जा रहा है।")
                break

        time.sleep(60)

def simulate_order(signal):
    print(f"📘 SIMULATED ORDER: {signal}")
    # Optional: Here you can randomly return "LOSS" or "PROFIT" for testing
    return "LOSS"  # या "PROFIT"
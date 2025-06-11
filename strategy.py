import time
from order_manager import place_order
from risk_control import check_loss_limit

def start_algo():
    loss_count = 0
    while True:
        if check_loss_limit():
            print("🔴 Loss limit reached. Stopping Algo.")
            break

        signal = "BUY_CALL"  # यहां पर VWAP logic जोड़ना है

        if signal:
            result = place_order(signal)
            if result == "LOSS":
                loss_count += 1
                print(f"❌ Loss {loss_count}/2")
            if loss_count >= 2:
                print("🔴 2 Loss हो चुके हैं। Algo बंद किया जा रहा है।")
                break
        time.sleep(60)

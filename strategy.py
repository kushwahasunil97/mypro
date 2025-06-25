import time
from order_manager import place_order
from risk_control import check_loss_limit

def start_algo(mode):
    loss_count = 0
    print(f"\n🚀 Algo Started in {mode.upper()} Mode")

    while True:
        # 🔴 Loss limit checker
        if check_loss_limit():
            print("🛑 Global loss limit hit. Algo exiting...")
            break

        # 🔍 Signal generation (VWAP logic to be added here)
        signal = get_trade_signal()

        if signal:
            print(f"📡 Signal detected: {signal}")

            # ✅ Order Execution
            result = (
                place_order(signal) if mode == "REAL" else simulate_order(signal)
            )

            if result == "LOSS":
                loss_count += 1
                print(f"❌ Trade Loss Count: {loss_count}/2")

            if loss_count >= 2:
                print("🛑 2 continuous losses. Algo stopped.")
                break

        else:
            print("⏳ No signal, waiting...")

        time.sleep(60)

# 🧠 Placeholder for VWAP or strategy logic
def get_trade_signal():
    # TODO: Add real VWAP logic here
    return "BUY_CALL"  # Or None

# 🎮 Simulated trade for testing without real execution
def simulate_order(signal):
    print(f"📘 SIMULATED ORDER EXECUTED: {signal}")
    # Return "LOSS" or "PROFIT" (Can be randomized if needed)
    return "LOSS"
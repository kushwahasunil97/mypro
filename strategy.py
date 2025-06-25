import time
from order_manager import place_order
from risk_control import check_loss_limit

# 🔄 Algo Entry Point
def start_algo(mode):
    loss_count = 0
    max_losses = 2
    print(f"\n🚀 Algo Started in {mode.upper()} Mode")

    while True:
        # 🔴 Check overall daily loss limit
        if check_loss_limit():
            print("🛑 Global loss limit hit. Algo exiting...")
            break

        # 🔍 Signal detection (placeholder for VWAP logic)
        signal = get_trade_signal()

        if signal:
            print(f"📡 Signal detected: {signal}")

            # 🎯 Execute real or simulated order
            if mode.upper() == "REAL":
                result = place_order(signal)
            else:
                result = simulate_order(signal)

            if result == "LOSS":
                loss_count += 1
                print(f"❌ Trade Loss Count: {loss_count}/{max_losses}")

            # 🛑 Stop after N losses in a session
            if loss_count >= max_losses:
                print("🛑 Reached max allowed losses. Stopping Algo.")
                break

        else:
            print("⏳ No valid signal, sleeping for 60s...")

        time.sleep(60)


# 📈 Strategy logic placeholder
def get_trade_signal():
    """
    TODO: Replace with real VWAP breakout / trap logic.
    Return one of: 'BUY_CALL', 'BUY_PUT', or None.
    """
    # Example dummy logic
    return "BUY_CALL"  # Replace with real strategy conditions


# 🧪 Simulated trade execution
def simulate_order(signal):
    print(f"📘 SIMULATED ORDER EXECUTED: {signal}")
    # You can use random.choice(["LOSS", "PROFIT"]) here if needed
    return "LOSS"
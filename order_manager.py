def place_order(signal):
    print(f"📈 Order Placed: {signal}")
    import random
    result = random.choice(["PROFIT", "LOSS"])
    return result

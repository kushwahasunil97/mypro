loss_counter = 0

def check_loss_limit():
    global loss_counter
    return loss_counter >= 2

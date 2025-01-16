import loss
import numpy as np

def get_min_max_loss(w_centre, b_centre, radius):
    max_loss = 0
    min_loss = np.inf
    for w in range(w_centre-radius, w_centre+radius):
        for b in range (b_centre-radius, b_centre+radius):
            max_loss = max(max_loss, loss.L(w, b))
            min_loss = min(min_loss, loss.L(w, b))
    return min_loss, max_loss

def loss_landscape(w_centre=0, b_centre=0, radius=10, block="minecraft:light_gray_concrete"): # incircle radius
    output_file = open("loss_landscape_commands.txt", "w")
    min_loss, max_loss = get_min_max_loss(w_centre, b_centre, radius)
    for w in range(w_centre-radius, w_centre+radius):
        for b in range (b_centre-radius, b_centre+radius):
            output_file.write(f"setblock {int(w)} {int(((loss.L(w, b)-min_loss)*60)/(max_loss-min_loss))-60} {int(b)} {block}\n") # O(n)
        print(f"creating loss landscape commands, {((w+1-(w_centre-radius))*100)//(2*radius)}% completed", end="\r")
    print()
    output_file.close()

def optimiser(lr=0.001, iters=10000, w_init=0, b_init=0, w_centre=0, b_centre=0, radius=10, block="minecraft:torch"):
    output_file = open("optimiser_commands.txt", "w")
    w = w_init
    b = b_init
    min_loss, max_loss = get_min_max_loss(w_centre, b_centre, radius)
    for i in range(iters):
        output_file.write(f"setblock {int(w)} {int(((loss.L(w, b)-min_loss)*60)/(max_loss-min_loss))-59} {int(b)} {block}\n")
        print(f"creating optimiser commands, {((i+1)*100)//iters}% completed, loss={int(loss.L(w, b))} at ({int(w)}, {int(b)})", end="\r")
        gradient = loss.grad_L(w, b)
        w = w - lr*gradient[0]
        b = b - lr*gradient[1]
    print()
    output_file.close()

    seen = set()
    with open("optimiser_commands.txt", "r") as input_file, open("optimiser_commands_minimal.txt", "w") as output_file:
        for line in input_file:
            if line not in seen:
                output_file.write(line)
                seen.add(line)
        input_file.close()
        output_file.close()
import make_commands
from input_commands import enter_commands
import playsound
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--centre", type=int, nargs=2, default=(0, 0), help="x z coordinates of the centre of the loss landscape plot; defaults to 0 0")
    parser.add_argument("--radius", type=int, default=10, help="radius of the incircle of the loss landscape plot; defaults to 10")
    parser.add_argument("--lr", type=float, default=0.001, help="learning rate for optimiser; defaults to 1e-3")
    parser.add_argument("--iters", type=int, default=10000, help="number of train loop iterations; defaults to 10000")
    parser.add_argument("--wandb_init", type=int, nargs=2, default=(0, 0), help="initial w and b; defaults to 0 0")
    parser.add_argument("--min_typing_speed", type=float, default=0.001, help="minimum time (in seconds) between successive keystrokes in a command; defaults to 1e-3")
    parser.add_argument("--delay", type=float, default=0.2, help="minimum delay (in seconds) between successive commands; defaults to 0.2")
    parser.add_argument("--countdown", type=int, default=10, help="countdown (in seconds) before command entry begins; defaults to 10")
    parser.add_argument("--landscape_block", type=str, default="minecraft:light_gray_concrete", help="block to construct loss landscape with; defaults to minecraft:light_gray_concrete")
    parser.add_argument("--optimiser_block", type=str, default="minecraft:torch", help="block to highlight optimiser path with; defaults to minecraft:torch")

    args = parser.parse_args()

    centre = tuple(args.centre)
    radius = args.radius
    lr = args.lr
    iters = args.iters
    min_typing_speed = args.min_typing_speed
    delay = args.delay
    counter_max = args.countdown
    wandb_init = tuple(args.wandb_init)
    landscape_block = args.landscape_block
    optimiser_block = args.optimiser_block

    make_commands.loss_landscape(w_centre=centre[0], b_centre=centre[1], radius=radius, block=landscape_block)
    enter_commands("loss_landscape_commands.txt", min_typing_speed=min_typing_speed, delay=delay, counter_max=counter_max)

    print("Landscape complete")
    for i in range(3):
        playsound.playsound("data/buzzer.mp3")

    make_commands.optimiser(lr=lr, iters=iters, w_init=wandb_init[0], b_init=wandb_init[1], w_centre=centre[0], b_centre=centre[1], radius=radius, block=optimiser_block)
    enter_commands("optimiser_commands_minimal.txt", min_typing_speed=min_typing_speed, delay=delay, counter_max=counter_max)

    print("End")
    for i in range(3):
        playsound.playsound("data/buzzer.mp3")

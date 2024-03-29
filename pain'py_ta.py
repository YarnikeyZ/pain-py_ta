from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd
from sys import argv
from pypixpile.pixpile import *
from keyboard import is_pressed

def render(fps: int) -> None:
    """Renders an "image" to the screen."""
    try:
        canvas = list(gts())
        canvas[1] += -2
        ## brush = [sym[0], color[1], posX[2], posY[3], sizeX[4], sizeY[5], speedX[6], speedY[7], bool[8]]
        brush = [",", 0, 1, 1, 4, 3, 2, 1, False]
        while True:

            ## etc
            if is_pressed('q'):
                print(CLR)
            
            ## brush movement v2
            if is_pressed('a'):
                if brush[2] - brush[6] >= 1:
                    brush[2] -= brush[6]
                elif brush[2] - brush[6]//2 >= 1:
                    brush[2] -= brush[6]//2
            if is_pressed('d'):
                if brush[2] + brush[4] + brush[6] <= canvas[0]-1:
                    brush[2] += brush[6]
                elif brush[2] + brush[4] + brush[6]//2 <= canvas[0]-2:
                    brush[2] += brush[6]//2
            if is_pressed('w'):
                if brush[3] - brush[7] >= 1:
                    brush[3] -= brush[7]
            if is_pressed('s'):
                if brush[3] + brush[5] + brush[7] <= canvas[1]-2:
                    brush[3] += brush[7]

            ## brush coloring
            colors = [("0", 0), ("1", 1), ("2", 202), ("3", 11), ("4", 46), ("5", 39), ("6", 21), ("7", 93)]
            for color in colors:
                if is_pressed(f"{color[0]}"):
                    brush[1] = color[1]
            
            ## brush size
            sizes = [("z", 1), ("x", 2), ("c", 3), ("v", 4), ("b", 5), ("n", 6), ("m", 7)]
            for size in sizes:
                if is_pressed(f"{size[0]}"):
                    brush[4], brush[5] = size[1]*2, size[1]

            ## canvas
            print(drawRectangle(brush[0], 0, 0, brush[2], brush[3], brush[4], brush[5]))
            sl(0.01)
            print(drawRectangle(brush[0], brush[1], 0, brush[2], brush[3], brush[4], brush[5]))
            print(drawLine("=", 245, 245, 0, 0, canvas[0], 0))
            print(drawLine("|", 245, 245, canvas[0], 0, canvas[0], canvas[1]-2))
            print(drawLine("|", 245, 245, 0, 0, 0, canvas[1]-2))
            print(drawLine("=", 245, 245, 1, canvas[1]-2, canvas[0]-2, canvas[1]-2))

            sl(1/fps)
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(CLR, end="")
    try:
        render(int(argv[1]))
    except IndexError:
        render(int(input("FPS:")))
    print(CLR, end="")

if __name__ == "__main__":
    main()

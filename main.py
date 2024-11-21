import neopixel
import board
import time
import random
import math
import sys
ledcount = 100
leds = neopixel.NeoPixel(board.D18, ledcount, pixel_order=neopixel.RGB, auto_write=False)
#Note to self -> add which pin you are using on board. EX: board.D18 for pin 18
ORDER = neopixel.RGB






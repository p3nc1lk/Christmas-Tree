import neopixel
import board
import time
import random
import math
import sys
ledcount = 100
leds = neopixel.NeoPixel(board., ledCount, pixel_order=neopixel.RGB, auto_write=False)
#Note to self -> add which pin you are using after board. EX: board.D18 for pin 18

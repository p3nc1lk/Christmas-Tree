import neopixel
import board
import time
import random
import math
import sys

ledcount = 100
leds = neopixel.NeoPixel(board.D18, ledcount, pixel_order=neopixel.RGB, auto_write=False)
# Note to self -> add which pin you are using on board. EX: board.D18 for pin 18 on raspberry pi3+
Light_green = (144, 238, 128)
Tea_green = (195, 250, 204)
Picton_blue = (63, 217, 255)
Button_blue = (31, 151, 231)
Plump_purple = (88, 69, 177)

def mix_colors(color1, color2, mix_factor):
    """Interpolate between two colors."""
    return tuple(
        round(color1[i] * (1 - mix_factor) + color2[i] * mix_factor)
        for i in range(3)
    )

if len(sys.argv) == 2 and sys.argv[1] == 'off':
    leds.fill((0, 0, 0))
    leds.show()

elif len(sys.argv) == 2 and sys.argv[1] == 'northern':
    # Northern lights themed lightshow
    colors = [
        Light_green,
        Tea_green,
        Picton_blue,
        Button_blue,
        Plump_purple
    ]

    offset = 0
    color_distance = ledcount / len(colors)
    delay = 0.05

    while True:
        for i in range(ledcount):
            n = (i + offset) % ledcount

            
            color_index = math.floor(n / color_distance)
            color1 = colors[color_index]
            color2 = colors[(color_index + 1) % len(colors)]

           
            mix_factor = (n % color_distance) / color_distance
            color = mix_colors(color1, color2, mix_factor)

            leds[i] = color

        leds.show()
        offset = (offset + 1) % ledcount  
        time.sleep(delay)  
else:
    print("Usage: ./sudopython main.py off|northern")

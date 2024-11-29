import neopixel
import board
import time
import random
import math
import sys
ledcount = 100
leds = neopixel.NeoPixel(board.D18, ledcount, pixel_order=neopixel.RGB, auto_write=False)
#Note to self -> add which pin you are using on board. EX: board.D18 for pin 18 on raspberry pi3+
Light_green = (144, 238, 128)
Tea_green = (195, 250,	204)
Picton_blue = (63, 217,	255)
Button_blue = (31, 151, 231)
Plump_purple = (88, 69, 177)

if len(sys.argv) == 2 and sys.argv[1] == 'off':
    leds.fill((0, 0, 0))
    leds.show()

elif len(sys.argv) == 2 and sys.argv[1] == 'northern':
  #Northern lights themed lightshow
  Colors = [
    Light_green,
    Tea_green,
    Picton_blue,
    Button_blue,
    Plump_purple
  ]

  offset = 0;

  colorDistance = leds.n / len(colors)

  while True:
        for i in range(leds.n):
            n = (i + offset) % leds.n

            colorIndex = math.floor(n / colorDistance)
            color1 = colors[colorIndex]
            color2 = colors[(colorIndex + 1) % len(colors)]

            mixFactor = (n % colorDistance) / colorDistance;

            color = mix_colors(color1, color2, mixFactor);

            leds[i] = color

        leds.show()
        offset = (offset + 1) % leds.n
    
  else:
    print("./sudopython main.py off|northern")
    


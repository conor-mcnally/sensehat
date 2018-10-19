from sense_hat import SenseHat
import time
import random

sense = SenseHat()

sense.clear()

b = [0, 0, 0]
g = [255, 0, 0]

heart = [
b,b,g,b,g,b,b,b,
b,g,g,g,g,g,b,b,
b,b,g,g,g,b,b,b,
b,b,b,g,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

diamond = [
b,b,b,b,g,b,b,b,
b,b,b,g,g,g,b,b,
b,b,b,b,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

sense.set_pixels(heart)
time.sleep(0.5)
sense.set_pixels(diamond)

blank = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

# three = [
# g,g,b,b,b,b,b,b,
# g,g,b,b,b,b,b,b,
# b,b,b,b,b,b,b,b,
# b,b,b,g,g,b,b,b,
# b,b,b,g,g,b,b,b,
# b,b,b,b,b,b,b,b,
# b,b,b,b,b,b,g,g,
# b,b,b,b,b,b,g,g,
# ]

# four = [
# b,b,b,b,b,b,b,b,
# b,g,g,b,b,g,g,b,
# b,g,g,b,b,g,g,b,
# b,b,b,b,b,b,b,b,
# b,b,b,b,b,b,b,b,
# b,g,g,b,b,g,g,b,
# b,g,g,b,b,g,g,b,
# b,b,b,b,b,b,b,b,
# ]

# five = [
# g,g,b,b,b,b,g,g,
# g,g,b,b,b,b,g,g,
# b,b,b,b,b,b,b,b,
# b,b,b,g,g,b,b,b,
# b,b,b,g,g,b,b,b,
# b,b,b,b,b,b,b,b,
# g,g,b,b,b,b,g,g,
# g,g,b,b,b,b,g,g,
# ]

# six = [
# r,r,b,b,b,b,r,r,
# r,r,b,b,b,b,r,r,
# b,b,b,b,b,b,b,b,
# r,r,b,b,b,b,r,r,
# r,r,b,b,b,b,r,r,
# b,b,b,b,b,b,b,b,
# r,r,b,b,b,b,r,r,
# r,r,b,b,b,b,r,r,
# ]
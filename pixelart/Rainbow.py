from sense_hat import SenseHat
import time

sense = SenseHat()

w = [255, 255, 255] #White
r = [255, 0, 0]#Rew
o = [255, 128, 0]#Orange
y = [255, 255, 0]#Yellow
g = [0, 255, 0]
lb = [0, 255, 255]
b =  [0, 0, 255]
p = [127, 0, 255]
w = [255, 255, 255]
image = [
r,r,r,r,r,r,r,r,    
o,o,o,o,o,o,o,o,
y,y,y,y,y,y,y,y,
g,g,g,g,g,g,g,g,
lb,lb,lb,lb,lb,lb,lb,lb,
b,b,b,b,b,b,b,b,
p,p,p,p,p,p,p,p,
w,w,w,w,w,w,w,w,
]

sense.set_pixels(image)
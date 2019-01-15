from sense_hat import SenseHat
import time

sense = SenseHat()

p = [178, 102, 255]
wp = [153, 204, 255]
db = [102, 178, 255]
b = [0, 0, 255]
lb = [0, 255, 255]
wlb = [153, 255, 255]
g = [0, 255, 0]
lg = [128, 255, 0]
wy = [255, 255, 153]
y = [255, 255, 0]
o = [255, 128, 0]
r = [255, 0, 0]
wr = [255, 204, 204]
dr = [153, 0, 0]
br = [51, 25, 0]




image = [
wp,p,db,b,lb,wlb,g,lg,
p,wp,b,db,wlb,lb,lg,g,
wy,y,o,y,r,wr,dr,br,
y,wy,y,o,wr,r,br,dr,
dr,br,r,wr,o,y,y,wy,
br,dr,wr,r,y,o,wy,y,
lg,g,lb,wlb,b,db,wp,p,
g,lg,wlb,lb,db,b,p,wp
]

sense.set_pixels(image)
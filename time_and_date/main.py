from sense_hat import SenseHat
from datetime import datetime
import time

hat = SenseHat()
temp = hat.get_temperature()

time_color = (0, 255, 0)
date_color = (200, 200, 0)
back_color = (155, 155, 155)

print("Temperature: %s C" % temp)

while True:
	now = datetime.now()
	date_message = '{:%d %B %Y}'.format(now)
	time_message = '{:%H:%M:%S}'.format(now)
	
	print("Temperature: %s C" % temp)
	hat.show_message(date_message, text_colour = date_color, back_colour = back_color, scroll_speed = 0.05)
	hat.show_message(time_message, text_colour = time_color, back_colour = back_color, scroll_speed = 0.05)

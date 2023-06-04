
from sense_hat import SenseHat
import time

def value():
    sense = SenseHat()
    sense.clear()
    humidity = sense.get_humidity()
    return humidity
    time.sleep(30)



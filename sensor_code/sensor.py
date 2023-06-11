
from sense_hat import SenseHat

def value():
    sense = SenseHat()
    sense.clear()
    humidity = sense.humidity
    humidity = "%.2f" % humidity
    return humidity
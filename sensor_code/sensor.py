
from sense_hat import SenseHat

def value():
    sense = SenseHat()
    sense.clear()
    humidity = sense.get_humidity()
    return humidity


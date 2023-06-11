
from sense_hat import SenseHat

def value():
    sense = SenseHat()
    sense.clear()
    humidity = sense.humidity
    return humidity

sense = SenseHat()

sense.show_message("hoola")
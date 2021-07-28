from Adafruit_IO import Client
from time import sleep
username = 'zaky0817'
key = 'aio_zoHj33z4yuCPNym9gpkFlTGYjjri'
io = Client(username, key)

with open('data.txt') as data:
    d = data.readline().rstrip()
    i = 1
    while d:
        humidity, fahrenheit, celcius = d.split()
        print(humidity, fahrenheit, celcius)
        d = data.readline().rstrip()
        io.send_data('humidity', humidity)
        io.send_data('temprature', celcius)
        io.send_data('fahrenheit', fahrenheit)
        print('data ke ', i)
        sleep(6)
        i += 1


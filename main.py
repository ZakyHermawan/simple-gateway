from Adafruit_IO import Client
from paho.mqtt import client as paho

from threading import Thread

broker = "broker.mqtt-dashboard.com"
from time import sleep

# sesuaikan dengan kebutuhan
sleep_variable = 4 # in seconds
topic = 'tesaja'
username = 'zaky0817'
key = 'aio_zoHj33z4yuCPNym9gpkFlTGYjjri'
io = Client(username, key)

# cara kirim
# mosquitto_pub.exe -h broker.mqtt-dashboard.com -t <topic> -m "<temprature> <humidity>"
temperature_arr, humidity_arr = [], []

# untuk multi threading
def pooling():
    while True:
        sleep(sleep_variable)
        print(temperature_arr, humidity_arr)
        if (temperature_arr != [] and humidity_arr != []):
            temprature, humidity = temperature_arr[0], humidity_arr[0]
            io.send_data('temprature', temprature)
            io.send_data('humidity', humidity)
            print(f"data berhasil dikirim: {temprature} {humidity}")
            temperature_arr.clear(); humidity_arr.clear()


def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))
    temperature, humidity = str(message.payload.decode("utf-8")).split()
    temperature_arr.append(temperature); humidity_arr.append(humidity)

thread = Thread(target=pooling)
thread.start()

client = paho.Client("c1")
client.on_message=on_message
client.connect(broker)

client.subscribe(topic)
client.loop_forever()


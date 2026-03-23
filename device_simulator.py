import time
import random
import json
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "home/energy"

def connect_mqtt():
    client = mqtt.Client()
    client.connect(broker, 1883, 60)
    return client

client = connect_mqtt()

devices = ["AC", "Fan", "Heater"]

print("🚀 Device Simulator Started...")

while True:
    device = random.choice(devices)

    if device == "AC":
        power = random.randint(1000, 1500)
    elif device == "Heater":
        power = random.randint(800, 1200)
    else:
        power = random.randint(50, 150)

    data = {
        "device": device,
        "power": power
    }

    client.publish(topic, json.dumps(data))
    print(f"✅ Sent: {data}")

    time.sleep(2)
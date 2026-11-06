import time
import board
import adafruit_dht
import requests
dht_device = adafruit_dht.DHT11(board.D20, use_pulseio=False)

API_KEY = "FJJFIQOFFI3BIE8Z"

URL = "https://api.thingspeak.com/update"

print("DHT11 Temperature Monitoring")
print("----------------------------")

while True:
    try:
        # Read temperature
        temperature = dht_device.temperature

        print("Temperature:", temperature, "°C")

        # Upload temperature to ThingSpeak
        data = {
            "api_key": API_KEY,
            "field1": temperature
        }

        response = requests.get(URL, params=data)

        if response.text != "0":
            print("Temperature uploaded successfully!")
        else:
            print("Upload failed!")

    except RuntimeError as error:
        print("Reading error:", error)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    time.sleep(20)

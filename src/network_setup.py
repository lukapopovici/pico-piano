import network
import time  # Added import

def connect_to_wifi(ssid='', password=''):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected! IP:", wlan.ifconfig()[0])
    return wlan

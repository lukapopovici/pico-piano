from network_setup import connect_to_wifi
from piano_controller import PianoController
from web_server import WebServer
import time

def main():
    wlan = connect_to_wifi()
    piano = PianoController()
    server = WebServer(piano, wlan.ifconfig()[0]) 
    
    print("Starting main loop...")
    while True:
        piano.check_keypad()
        server.handle_requests()
        time.sleep(0.01)  

if __name__ == "__main__":
    main()

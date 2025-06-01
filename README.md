#  Pico Piano 

A fun and interactive way to get a piano interface using a Raspberry Pi Pico W! Play notes manually using a keypad or remotely through a web interface. It also features octave switching via an IR sensor and a lightweight embedded web server.

---

##  Features

-  **Manual control** with a 3x3 keypad
- **Wi-Fi web interface** to play notes remotely
-  **IR sensor** toggles between normal and lower octaves
- **Piezo buzzer** to produce musical notes
-  **Simple HTTP server** for interactive control and state queries
-  **Dark/Light theme** toggles in real-time via the IR sensor on the web UI

---

##  What You Need

- Raspberry Pi Pico W
- Passive Buzzer
- IR Sensor (digital output)
- 3x3 Keypad
- Breadboard & jumper wires
- Micro-USB cable
- Wi-Fi access point
- Will to live
---

##  File Structure

```
pico_piano/
│── main.py
│── network_setup.py
│── piano_controller.py
│── web_server.py
│── static/
│   └── index.html
```

---
## Picture
![image](https://github.com/user-attachments/assets/f4db2ce2-6443-49ff-9082-093c1b8f15c3)



## Schematic

![image](https://github.com/user-attachments/assets/e59613c2-884b-4cb6-badc-9ba0fcf73263)



##  Setup Instructions

1. **Connect the components:**
   - Buzzer → GPIO15
   - IR Sensor → GPIO14
   - Keypad rows → GPIO2, GPIO3, GPIO4
   - Keypad cols → GPIO5, GPIO6, GPIO7

2. **Clone the repository and upload files to the Pico W:**
   Use [Thonny](https://thonny.org/) or `rshell` to upload the entire project to your Pico W.

3. **Update your Wi-Fi credentials:**
   In `network_setup.py`, replace:

   ```python
   connect_to_wifi(ssid='networkname', password='your guess')
   ```

   with your actual SSID and password.

4. **Run `main.py`:**
   This will connect the Pico to Wi-Fi, start the keypad listener, and launch the web server.

---

##  Web Interface

- Access the piano remotely by entering your Pico’s IP address (displayed in the serial console).
- Play notes via links like:  
  `http://<ip_address>/play?note=C`
- Monitor IR sensor state:  
  `http://<ip_address>/state`
- Detect last input method (manual/remote):  
  `http://<ip_address>/manual`

![image](https://github.com/user-attachments/assets/98375cd3-14b8-4505-89f7-96ce0b15b687)


> The web UI (in `static/index.html`) will automatically switch themes based on IR sensor state.

---

##  Example Output

```bash
Connecting to Wi-Fi...
Connected! IP: 192.168.1.42
Server running at http://192.168.1.42
Manual input: Note C
IR sensor toggled: HIGH (object detected)
```


##  How It Works

- **Keypad scanning** runs in a loop using GPIO pin reads.
- **IR sensor** dynamically switches between two frequency maps (`notes_normal` and `notes_lower`).
- The **web server** is a lightweight HTTP handler using `socket` and `ure`.
- The **buzzer** plays tones using PWM with a brief duration and pause.



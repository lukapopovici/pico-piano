import socket
import ure
import time  # Added import

class WebServer:
    def __init__(self, piano_controller, ip_address):
        self.piano = piano_controller
        self.ip_address = ip_address
        self.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen(5)
        print(f"Server running at http://{self.ip_address}")
        
    def handle_requests(self):
        try:
            cl, addr = self.s.accept()
            cl.settimeout(0.1)
            try:
                request = cl.recv(1024).decode()
            except:
                cl.close()
                return

            path = ure.search(r'GET\s(\/[^\s]*)\s', request)
            if path:
                route = path.group(1)

                if route.startswith('/play'):
                    note_match = ure.search(r'note=([A-G])', route)
                    if note_match:
                        note = note_match.group(1)
                        self.piano.play_note(note)
                        self.piano.manual_input_flag = False
                    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\nOK')

                elif route == "/state":
                    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n' + 
                          str(self.piano.last_ir_state))

                elif route == "/manual":
                    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n' + 
                          ("1" if self.piano.manual_input_flag else "0"))

                else:
                    with open('static/index.html', 'r') as f:
                        html = f.read()
                    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n' + html)

            cl.close()
        except Exception as e:
            print("Server error:", e)
            time.sleep(0.1) 
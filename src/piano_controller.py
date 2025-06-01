from machine import Pin, PWM
import time

class PianoController:
    def __init__(self):
        # Buzzer and IR sensor setup
        self.buzzer = PWM(Pin(15))
        self.buzzer.duty_u16(0)
        self.ir_sensor = Pin(14, Pin.IN)
        
        # Notes
        self.notes_normal = {'C': 262, 'D': 294, 'E': 330, 
                           'F': 349, 'G': 392, 'A': 440, 'B': 494}
        self.notes_lower = {'C': 131, 'D': 147, 'E': 165,
                           'F': 175, 'G': 196, 'A': 220, 'B': 247}
        
        # Keypad setup
        self.rows = [Pin(pin, Pin.OUT) for pin in [2, 3, 4]]
        self.cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in [5, 6, 7]]
        self.key_map = {
            (0, 0): 'C', (0, 1): 'D', (0, 2): 'E',
            (1, 0): 'F', (1, 1): 'G', (1, 2): 'A',
            (2, 0): 'B'
        }
        self.manual_input_flag = False
        self.last_ir_state = self.ir_sensor.value()

    def play_note(self, note):
        current_notes = self.notes_lower if self.ir_sensor.value() == 1 else self.notes_normal
        freq = current_notes.get(note, 0)
        if freq:
            self.buzzer.freq(freq)
            self.buzzer.duty_u16(30000)
            time.sleep_ms(300)
            self.buzzer.duty_u16(0)

    def check_keypad(self):
        for i, row in enumerate(self.rows):
            row.high()
            for j, col in enumerate(self.cols):
                if col.value() == 1:
                    key = self.key_map.get((i, j))
                    if key:
                        self.play_note(key)
                        self.manual_input_flag = True
                        print("Manual input: Note", key)
                        time.sleep(0.3)  # debounce
            row.low()
        
        # Check IR sensor state
        current_ir_state = self.ir_sensor.value()
        if current_ir_state != self.last_ir_state:
            print("IR sensor toggled:", "HIGH (object detected)" if current_ir_state else "LOW (clear)")
            self.last_ir_state = current_ir_state

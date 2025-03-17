import os
import time
import random
import threading
import signal
import sys
from evdev import UInput, ecodes as e

class ActivitySimulator:
    def __init__(self):
        self.running = False
        self.ui = UInput()

    def move_mouse(self):
        """Randomly move the mouse to simulate activity."""
        x = random.randint(100, 1000)
        y = random.randint(100, 800)
        os.system(f"xdotool mousemove {x} {y}")
        print(f"Mouse moved to: ({x}, {y})")

    def press_key(self):
        """Simulates a real key press and release."""
        key = random.choice([
            e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E, e.KEY_F, e.KEY_G, e.KEY_H, e.KEY_I, e.KEY_J,
            e.KEY_K, e.KEY_L, e.KEY_M, e.KEY_N, e.KEY_O, e.KEY_P, e.KEY_Q, e.KEY_R, e.KEY_S, e.KEY_T,
            e.KEY_U, e.KEY_V, e.KEY_W, e.KEY_X, e.KEY_Y, e.KEY_Z,  # Alphabets
            e.KEY_1, e.KEY_2, e.KEY_3, e.KEY_4, e.KEY_5, e.KEY_6, e.KEY_7, e.KEY_8, e.KEY_9, e.KEY_0,  # Numbers
            e.KEY_TAB, e.KEY_SPACE  # Tab & Space
        ])
        self.ui.write(e.EV_KEY, key, 1)  # Press key
        self.ui.syn()
        time.sleep(0.1)
        self.ui.write(e.EV_KEY, key, 0)  # Release key
        self.ui.syn()
        print(f"Key pressed: {key}")

    def run(self):
        """Main loop to simulate activity."""
        self.running = True
        while self.running:
            self.move_mouse()
            self.press_key()
            time.sleep(random.randint(5, 10))

    def stop(self):
        """Stops the activity simulation."""
        self.running = False
        print("Stopping simulator...")

simulator = ActivitySimulator()

def signal_handler(sig, frame):
    simulator.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def start():
    """Starts the activity simulator in a new thread."""
    t = threading.Thread(target=simulator.run)
    t.start()

def stop():
    """Stops the activity simulator."""
    simulator.stop()

if __name__ == "__main__":
    start()

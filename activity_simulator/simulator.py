import os
import time
import random
import threading
import signal
import sys
from evdev import UInput, ecodes as e
import subprocess

class ActivitySimulator:
    def __init__(self):
        self.running = False
        self.ui = UInput()

    def move_mouse(self):
        """Move the mouse to a random location smoothly."""
        x = random.randint(100, 1000)
        y = random.randint(100, 800)
        subprocess.run(["xdotool", "mousemove", "--sync", "--smooth", "10", str(x), str(y)])
        print(f"[Mouse] Moved smoothly to: ({x}, {y})")

    def scroll_mouse(self):
        """Randomly scroll up or down."""
        direction = random.choice(['up', 'down'])
        clicks = random.randint(1, 3)
        button = 4 if direction == 'up' else 5
        for _ in range(clicks):
            subprocess.run(["xdotool", "click", str(button)])
            time.sleep(0.1)
        print(f"[Scroll] Scrolled {direction} {clicks} times")

    def press_key(self):
        """Simulates a real key press and release."""
        key = random.choice([
            e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E, e.KEY_F, e.KEY_G, e.KEY_H, e.KEY_I, e.KEY_J,
            e.KEY_K, e.KEY_L, e.KEY_M, e.KEY_N, e.KEY_O, e.KEY_P, e.KEY_Q, e.KEY_R, e.KEY_S, e.KEY_T,
            e.KEY_U, e.KEY_V, e.KEY_W, e.KEY_X, e.KEY_Y, e.KEY_Z,
            e.KEY_1, e.KEY_2, e.KEY_3, e.KEY_4, e.KEY_5, e.KEY_6, e.KEY_7, e.KEY_8, e.KEY_9, e.KEY_0,
            e.KEY_TAB, e.KEY_SPACE
        ])
        self.ui.write(e.EV_KEY, key, 1)
        self.ui.syn()
        time.sleep(0.1)
        self.ui.write(e.EV_KEY, key, 0)
        self.ui.syn()
        print(f"[Key] Pressed key code: {key}")

    def type_text(self):
        """Simulate typing full words."""
        words = ['crm ', 'wave picking ', 'delivery slip ', 'inventory ', 'invoice ', 'quotation ', 'sales order ', 'purchase order ', 'partner ',
                 'lead ', 'opportunity ', 'picking ', 'manufacturing ', 'bom ', 'mrp ', 'stock move ', 'replenishment ', 'uom ', 'accounting ',
                 'journal ', 'journal entry ', 'reconciliation ', 'fiscal year ', 'chart of accounts ', 'analytic account ', 'project ', 'task ',
                 'timesheet ', 'attendance ', 'payroll ', 'employee ', 'recruitment ', 'applicant ', 'expenses ', 'fleet ', 'leave request ',
                 'calendar ', 'helpdesk ', 'ticket ', 'sla ', 'subscription ', 'contract ', 'membership ', 'e-commerce ', 'website ', 'blog ',
                 'forum ', 'live chat ', 'point of sale ', 'pos session ', 'product ', 'product variant ', 'product category ', 'barcode ',
                 'serial number ', 'lot ', 'procurement ', 'route ', 'warehouse ', 'location ', 'transfer ', 'scrap ', 'return ', 'backorder ',
                 'vendor ', 'customer ', 'pricelist ', 'discount ', 'tax ', 'multi-currency ', 'bank statement ', 'payment ', 'payment term ',
                 'revenue recognition ', 'asset ', 'depreciation ', 'subscription ', 'timesheet ', 'approval ', 'studio ', 'custom module ', 'api ',
                 'odoo.sh ', 'saas ', 'enterprise ', 'community ', 'theme ', 'kanban ', 'gantt ', 'pivot ', 'dashboard ', 'report ', 'pdf report ',
                 'qweb ', 'xml ', 'view ', 'model ', 'field ', 'record ', 'workflow ', 'automation ']

        text = random.choice(words)
        subprocess.run(['xdotool', 'type', text])
        print(f"[Typing] Typed: '{text}'")

    def switch_window(self):
        """Simulate holding Alt and pressing Tab multiple times."""
        tabs = random.randint(1, 5)
        subprocess.run(["xdotool", "keydown", "Alt"])
        time.sleep(0.1)
        for _ in range(tabs):
            subprocess.run(["xdotool", "key", "Tab"])
            time.sleep(0.2)
        subprocess.run(["xdotool", "keyup", "Alt"])
        print(f"[Window] Switched window using Alt+Tab {tabs} times")

    def run(self):
        """Main loop to simulate activity."""
        self.running = True
        actions = [
            self.move_mouse,
            self.scroll_mouse,
            self.press_key,
            self.type_text,
            self.switch_window
        ]
        print("[Simulator] Started activity simulation.")

        while self.running:
            action = random.choice(actions)
            action()
            sleep_time = random.uniform(4, 12)
            print(f"[Simulator] Sleeping for {sleep_time:.2f} seconds...\n")
            time.sleep(sleep_time)

    def stop(self):
        """Stops the activity simulation."""
        self.running = False
        print("[Simulator] Stopping activity simulation...")


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


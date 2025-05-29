# Activity Simulator - Prevent Idle Detection on Ubuntu

🚀 **Activity Simulator** is a Python-based tool that simulates **keyboard and mouse movements** to prevent idle tracking systems from detecting inactivity. It ensures that your system remains "active" even when you are away.

## 🔹 Features
✔️ Random **mouse movements** (smooth)  
✔️ Simulated **keyboard inputs** (A-Z, numbers, space, tab + typed words)  
✔️ **Random window switching (Alt+Tab)** to make activity look realistic  
✔️ **Occasional scrolling**
✔️ Smart action rotation with random intervals  
✔️ Lightweight & runs **silently in the background**  
✔️ Simple **start/stop** commands

---

## 🔧 Installation
### 1️⃣ Install Dependencies
Ensure you have `pip` and `xdotool` installed:
```bash
sudo apt install xdotool
pip install evdev
```

### 2️⃣ Clone the Repository & Install
```bash
git clone https://github.com/sagarpise5/activity_simulator.git
cd activity_simulator
pip install .
```

---

## 🚀 How to Use
### **Start the Activity Simulator**  
```bash
activity-sim-start
```
> The script will begin moving the mouse and pressing keys automatically.

### **Stop the Activity Simulator**  
```bash
activity-sim-stop
```
> This will gracefully stop the simulation.

---

## 🛠️ How It Works
- Moves the mouse to random locations periodically  
- Simulates keyboard presses (A-Z, numbers, space, tab)  
- Randomly scrolls pages and switches applications  
- Runs in the background while consuming minimal resources  

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

**🛠 Maintained by:** [Your Name]  
🔗 GitHub: [Sagar Pise](https://github.com/sagarpise5)

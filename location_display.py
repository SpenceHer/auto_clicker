import pyautogui
import time

# This will display mouse coordinates in the console
try:
    while True:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        print(f"Mouse position: X={x} Y={y}", end="\r")  # The end='\r' keeps updating on the same line
        time.sleep(0.1)  # Update every 100ms
except KeyboardInterrupt:
    print("\nProgram stopped.")
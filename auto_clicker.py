import pyautogui
import time
import keyboard  # For detecting the stop key

# Delay to switch to the webpage you want to click
time.sleep(5)

# Coordinates of the area you want to click (example: x=500, y=300)
x, y = 3800, 925

# Number of clicks and extremely low delay between clicks
clicks = 2000
delay = 0.000001  # Fast clicks with minimal delay

print("Press 'ESC' to stop the auto-clicker at any time.")

# Auto-clicker loop with a keyboard interrupt to stop it
for i in range(clicks):
    if keyboard.is_pressed("esc"):  # Stop if ESC is pressed
        print("Auto-clicker stopped by the user.")
        break
    pyautogui.click(x, y)
    # time.sleep(delay)  # You can also remove this to maximize speed

print("Auto-clicker finished.")

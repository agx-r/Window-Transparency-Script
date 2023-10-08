import win32gui
import win32con
import time

# Constants for transparency values
TRANSPARENCY_ALPHA = 0.86
TRANSPARENCY_INTERVAL = 1  # Adjust the interval as needed

# Function to set the transparency of a window
def set_window_transparency(hwnd, alpha):
    try:
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, int(255 * alpha), win32con.LWA_ALPHA)
    except Exception as e:
        print(f"An error occurred while setting transparency: {str(e)}")

# Function to apply transparency to all top-level windows
def make_all_windows_transparent():
    try:
        def callback(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                set_window_transparency(hwnd, TRANSPARENCY_ALPHA)

        win32gui.EnumWindows(callback, None)
    except Exception as e:
        print(f"An error occurred while enumerating windows: {str(e)}")

# Function to continuously monitor and apply transparency to new windows
def monitor_new_windows():
    while True:
        make_all_windows_transparent()
        time.sleep(TRANSPARENCY_INTERVAL)

if __name__ == "__main__":
    monitor_new_windows()
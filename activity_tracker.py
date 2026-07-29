import win32gui

def get_active_window_():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)
    
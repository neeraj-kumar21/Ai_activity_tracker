import win32gui

def get_active_window_():

    window = win32gui.GetForegroundWindow()

    window_title =  win32gui.GetWindowText(window)

    return window_title



    
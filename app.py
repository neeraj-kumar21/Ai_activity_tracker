from activity_tracker import get_active_window_
import time

print("AI Activity Tracker is running...")
print("-" * 40)

while True:
    active_window = get_active_window_()

    print("Current active window:", active_window)

    time.sleep(2)  # Check every 2 secondscl
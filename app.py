from activity_tracker import get_active_window_, get_active_window_
from database import create_database, save_activity

from datetime import datetime
import time

create_database()

last_window = ""

print("AI Activity Tracker is running...")


while True:

    current_window = get_active_window_()

    if current_window != last_window:

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(current_time , current_window)

    # Save the activity log 
    save_activity(current_time, current_window)
    
    save_activity(current_time, current_window)

    last_window = current_window

    time.sleep(2)  # Check every 2 seconds

def get_active_window():
    ...
from activity_tracker import get_active_window_
from session_manager import SessionManager
from database import create_database,save_activity

import time 

# Create database if it doesn't exist
create_database()

# Creat Session Manager 
manager = SessionManager()

# Get the current active window 
current_window = get_active_window_()

# Start first session 
manager.start_session(current_window)

print("AI Activity Tracker Started")


while True:
    # check current active window
    new_window = get_active_window_()

    # if user switched to another application
    if new_window != current_window:

        # End previous session 
        session = manager.end_session()

        # Print session details
        print(session)

        # Save session details to database  
        save_activity(
            session['start_time'],
            session['end_time'],
            session['duration'],
            session['window_title'],
        )

        # Update current window 
        current_window = new_window

        # Start new session
        manager.start_session(current_window)


    # Check every 2 secounds
    time.sleep(2)
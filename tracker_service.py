from activity_tracker import get_active_window_
from session_manager import  SessionManager
from database import create_database, save_activity

import  time

def start_tracker():

    create_database()

    manager = SessionManager()

    current_window = get_active_window_

    manager.start_session(current_window)

    print("AI Activity Tracker Started")

    while True:
        new_window = get_active_window_()
        if new_window != current_window:
            session = manager.end_session()
            print(session)

            save_activity(
                session["start_time"],
                session["end_time"],
                session["duration"],
                session["window_title"],
            )

            current_window = new_window

            manager.start_session(current_window)

        time.sleep(2)    


# =================  This is now our tracking engine ==========================

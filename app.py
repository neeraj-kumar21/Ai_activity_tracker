import threading
import time

from activity_tracker import get_active_window_
from session_manager import SessionManager
from database import create_database, save_activity
from datetime import datetime, timedelta
from report_generator import generate_report

import dashboard


# ==========================================
# ACTIVITY TRACKER
# ==========================================

def start_tracker():

    manager = SessionManager()

    current_window = get_active_window_()

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
                session["window_title"]
            )

            current_window = new_window

            manager.start_session(current_window)

        time.sleep(2)


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    # Create database
    create_database()

    # Start tracker in background
    tracker_thread = threading.Thread(
        target=start_tracker,
        daemon=True
    )

    tracker_thread.start()

    print("Tracker started successfully")

    # Start Dashboard
    dashboard.start_dashboard()
from activity_tracker import get_active_window_
from session_manager import SessionManager
from database import create_database, save_activity


import time
from datetime import datetime, timedelta

from report_generator import generate_report


# =========================================
# CREATE DATABASE
# =========================================

create_database()


# =========================================
# CREATE SESSION MANAGER
# =========================================

manager = SessionManager()


# =========================================
# GET CURRENT ACTIVE WINDOW
# =========================================

current_window = get_active_window_()


# =========================================
# START FIRST SESSION
# =========================================

manager.start_session(current_window)


# =========================================
# 8 HOUR REPORT TIMER
# =========================================

report_start_time = datetime.now()

# ---- TESTING MODE: 2 minutes ----
next_report_time = report_start_time + timedelta(hours=8)
# ---- PRODUCTION MODE (use this after testing) ----
# next_report_time = report_start_time + timedelta(hours=8)

print("AI Activity Tracker Started")
print("Next report:", next_report_time)


# =========================================
# MAIN TRACKING LOOP
# =========================================

while True:

    # Check current active window
    new_window = get_active_window_()

    # =====================================
    # WINDOW CHANGED
    # =====================================
    if new_window != current_window:

        # End previous session
        session = manager.end_session()
        print(session)

        # Save activity
        save_activity(
            session['start_time'],
            session['end_time'],
            session['duration'],
            session['window_title'],
        )

        # Update current window and start new session
        current_window = new_window
        manager.start_session(current_window)


    if datetime.now() >= next_report_time:

        print("Generating report NOW...")

        report_end_time = datetime.now()

        generate_report(
            report_start_time,
            report_end_time
        )

        report_start_time = report_end_time

        # TESTING
        next_report_time = report_start_time + timedelta(hours=8)
        print("Next report scheduled:", next_report_time)

        time.sleep(2)

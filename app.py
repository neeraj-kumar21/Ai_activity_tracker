from activity_tracker import get_active_window_
from session_manager import SessionManager
from database import create_database, save_activity

import time
import threading

from datetime import datetime, timedelta

from report_generator import generate_report
from config import get_setting

import customtkinter as ctk
from splash import SplashScreen
from dashboard import start_dashboard


# =========================================
# CREATE DATABASE
# =========================================

create_database()


def run_tracker():
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

    report_interval = get_setting("report_interval_hours")

    next_report_time = report_start_time + timedelta(hours=report_interval)

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

            generate_report(report_start_time, report_end_time)

            report_start_time = report_end_time

            report_interval = get_setting("report_interval_hours")

            next_report_time = report_start_time + timedelta(hours=report_interval)

            print("Next report scheduled:", next_report_time)

        time.sleep(2)


# =========================================
# MAIN
# =========================================

if __name__ == "__main__":

    # Tracker background mein chalega
    tracker_thread = threading.Thread(
        target=run_tracker,
        daemon=True
    )
    tracker_thread.start()

    # ---- SINGLE Tk root for the whole app lifecycle ----
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    def open_dashboard():
        start_dashboard(app)

    # Splash builds itself inside `app`, then hands off to dashboard
    SplashScreen(app, on_complete=open_dashboard)

    # Only ONE mainloop for the entire app
    app.mainloop()
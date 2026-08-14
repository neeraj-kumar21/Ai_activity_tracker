
#  advance ke liye h   

# import threading


# from activity_tracker import get_active_window_
# from session_manager import SessionManager
# from database import create_database, save_activity

# import time
# from datetime import datetime, timedelta
# from report_generator import generate_report

# import dashboard


# # ==========================================
# # ACTIVITY TRACKER
# # ==========================================

# def start_tracker():

#     manager = SessionManager()

#     report_start_time = datetime.now()
#     next_report_time = report_start_time + timedelta(hours=8)

#     current_window = get_active_window_()

#     manager.start_session(current_window)

#     print("AI Activity Tracker Started")
#     print("Next report:" , next_report_time)


# # ==========================================
# # MAIN
# # ==========================================

# if __name__ == "__main__":

#     # Create database
#     create_database()

#     # ==== Report timing ==============
#     report_start_time = datetime.now()
#     next_report_time = report_start_time + timedelta(hours=8)


#     manager = SessionManager()

#     # Start tracker in background
#     tracker_thread = threading.Thread(
#         target=start_tracker,
#         daemon=True
#     )

#     tracker_thread.start()

#     print("Tracker started successfully")

#     # Start Dashboard
#     dashboard.start_dashboard()


# while True:

#     new_window = get_active_window_()

#     if new_window != current_window:

#         session = manager.end_session()

#         print(session)

#         save_activity(
#             session["start_time"],
#             session["end_time"],
#             session["duration"],
#             session["window_title"],
#         )

#         current_window = new_window

#         manager.start_session(current_window)

#     # ==============================
#     # 8 HOUR REPORT CHECK
#     # ==============================

#     if datetime.now() >= next_report_time:

#         report_end_time = datetime.now()

#         generate_report(
#             report_start_time,
#             report_end_time
#         )

#         report_start_time = report_end_time

#         next_report_time = (
#             report_start_time +
#             timedelta(minutes=2)
#         )

#     time.sleep(2)
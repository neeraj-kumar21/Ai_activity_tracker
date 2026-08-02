from datetime import datetime

class SessionManager:
    def __init__(self):
        self.current_window = None
        self.start_time = None

    def start_session(self, window_title):
        print(f"Started: {window_title}")
        self.current_window = window_title
        self.start_time = datetime.now()

    def end_session(self):
        end_time = datetime.now()

        return {
            "window_title": self.current_window,
            "start_time": self.start_time,
            "end_time": end_time,
            "duration": end_time - self.start_time
        }
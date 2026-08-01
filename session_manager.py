from datatime import datetime

class SessionManager:
    def __init__(self):
        self.sessions = []
        self.current_session = None


def start_session(self, window_title):
        self.current_session = window_title
        self.start_time = datetime.now()


def end_session(self):
     end_time = datetime.now()

     duration = end_time - self.start_time

     session = {
          "window_title": self.current_session,
          "start_time": self.start_time,
            "end_time": end_time,
            "duration": duration
     }  

     return session    

  
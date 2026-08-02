from session_manager import SessionManager
import time

manager = SessionManager()

manager.start_session("VS ode")

time.sleep(5)  # Simulate activity for 5 seconds

session = manager.end_session()

print(session)

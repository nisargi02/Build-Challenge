# assignment1/logging_utils.py
import threading
from datetime import datetime

def log(msg: str) -> None:
    print(f"[{threading.current_thread().name}] "
          f"{datetime.now().strftime('%H:%M:%S')} - {msg}")

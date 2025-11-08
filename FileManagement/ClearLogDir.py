import os
import time

log_dir = "logs"
days_to_keep = 7
now = time.time()

for filename in os.listdir(log_dir):
    filepath = os.path.join(log_dir, filename)
    if os.path.isfile(filepath):
        # Υπολογίζει ηλικία αρχείου
        age_days = (now - os.path.getmtime(filepath)) / 86400
        if age_days > days_to_keep:
            os.remove(filepath)
            print(f"Deleted {filename} (older than {days_to_keep} days)")

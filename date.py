import datetime

# Create a log file with timestamp
log_content = f"Workflow executed on {datetime.datetime.now()}\nAdditional log details..."
with open("log.txt", "w") as log_file:
    log_file.write(log_content)

# Optionally, print the log content
print(log_content)

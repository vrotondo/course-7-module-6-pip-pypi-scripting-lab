from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list of log entries")
    
    # STEP 2: Generate a filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # STEP 3: Write the log entries to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    # STEP 4: Print a confirmation message
    print(f"Log file '{filename}' created successfully with {len(data)} entries.")
    
    return filename

if __name__ == "__main__":
    # Sample data when run directly
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
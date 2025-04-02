import os

def send_notification(message):
    # Questo esempio usa il comando 'osascript' per macOS
    os.system(f'osascript -e \'display notification "{message}"\'')

if __name__ == "__main__":
    send_notification("This is a test notification!")
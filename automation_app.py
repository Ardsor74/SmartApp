import os
from twilio.rest import Client

def send_notification(message):
    # Questo esempio usa il comando 'osascript' per macOS
    os.system(f'osascript -e \'display notification "{message}"\'')

def send_sms(message, to, from_):
    # Le credenziali di Twilio (devi configurarle)
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message,
        from_=from_,
        to=to
    )
    print(f"Message sent: {message.sid}")

if __name__ == "__main__":
    send_notification("This is a test notification!")
    # Esempio di invio SMS
    send_sms("This is a test SMS!", "+1234567890", "+0987654321")
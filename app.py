from twilio.rest import Client
from keys import accSID, authTok, trial_number, to_number
import requests
def main():
    client = Client(accSID, authTok)
    input_url = input("Enter the full URL of the website to monitor: ")
    print("pinging website ...")
    while True:
        try:
            r = requests.head(input_url)
            if r.status_code >= 400:
                message = client.messages.create(
                body = "Website is down",
                from_=trial_number,
                to=to_number
                )
                print(message.sid)
                break
        except requests.ConnectionError:
            print("Failed to connect to website")
            break

if __name__ == "__main__":
    main()

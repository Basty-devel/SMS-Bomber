import requests
import time

def banner():
    """Clear the screen and display a banner."""
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                                                                     
                                   By : N3S3                                                                                               
    Note : We are NOT responsible for any damage caused by this script. Use at your own risk.
""")

def validate_mobile_number(mobile_number):
    """Validate if the mobile number is numeric and has the correct length (10 digits in this case)."""
    if len(mobile_number) > 20 or not mobile_number.isdigit():
        raise ValueError("Invalid mobile number. Please enter a 10-digit numeric mobile number.")
    return mobile_number

def validate_positive_integer(value, name):
    """Validate if the input is a positive integer."""
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
    except ValueError:
        raise ValueError(f"Invalid {name}. Please enter a positive integer for {name}.")
    return value

def send_sms(api_key, mobile_number, message, count, delay):
    """Send SMS messages using the provided API key and parameters."""
    url = "https://jyothidinesh-sms-sending-v1.p.rapidapi.com/site2sms.com/send"

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "jyothidinesh-sms-sending-v1.p.rapidapi.com"
    }

    params = {
        "mobile": mobile_number,
        "message": message
    }

    for i in range(count):
        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                print(f"SMS {i + 1} sent successfully.")
                print("Response:", response.json())
            else:
                print(f"Failed to send SMS {i + 1}. Status code: {response.status_code}")
                print("Response:", response.text)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        if i < count - 1:
            print(f"Waiting for {delay} seconds before sending the next SMS...")
            time.sleep(delay)

def main():
    """Main function to get user inputs and trigger SMS sending."""
    banner()

    api_key = ""  # Replace with your actual API key

    try:
        mobile_number = input("Enter the mobile number: ")
        mobile_number = validate_mobile_number(mobile_number)

        message = input("Enter the message you want to send: ")

        count = input("Enter the number of messages to send: ")
        count = validate_positive_integer(count, "number of messages")

        delay = input("Enter the delay in seconds between messages: ")
        delay = validate_positive_integer(delay, "delay")

        send_sms(api_key, mobile_number, message, count, delay)

    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()

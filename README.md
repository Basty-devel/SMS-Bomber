SMS Bomber
A new working SMS Bomber that allows you to send multiple SMS messages to a given phone number, with customizable message content, a specified count of messages, and a delay between each message.

This tool is strictly for educational purposes or authorized testing (e.g., checking message delivery for testing purposes). Please do not misuse it for spamming or malicious activities. The authors take no responsibility for any damage caused by the misuse of this tool.

Features
Customizable: You can set a phone number, message, number of SMS to send, and delay between each message.
Easy to Use: Just sign up for a free API key, add it to the script, and you're ready to go!
Free Usage: Uses a free SMS API with a generous limit of 1000 SMS per hour.
Setup and Usage
Step 1: Install Dependencies
Ensure you have Python 3.x and pip installed. Then, install the necessary dependencies:

bash
Copy code
pip install requests
Step 2: Get an API Key
Visit RapidAPI - SMS Sending.
Sign up for a free account if you don’t already have one.
Navigate to Data --> SMS and find the "SMS-Sending" API (not the fusion).
Subscribe to the free tier (allows up to 1000 SMS/hour).
Copy the provided API Key.
Step 3: Add API Key
Open the script and find the following line:

python
Copy code
api_key = "bce73d2db2mshc49f908da13p1ff7e5jsnf4327f6f4ac1"  # Replace with your actual API key
Replace the placeholder key with your own API key from RapidAPI.

Step 4: Run the Script
Run the Python script:

bash
Copy code
python sms_bomber.py
The script will prompt you to enter the following details:

Phone Number: The target phone number (make sure it's valid and formatted correctly).
Message: The message content you want to send.
Count: The number of SMS messages to send.
Delay: The delay between each message (in seconds).
Example Usage
bash
Copy code
Enter the mobile number: 1234567890
Enter the message you want to send: Hello, this is a test message!
Enter the number of messages to send: 5
Enter the delay in seconds between messages: 2
This will send 5 SMS messages to the provided phone number with a 2-second delay between each message.

Important Notes
This tool is for educational purposes only. Do not use it for spamming or any form of harassment.
SMS limits: You are limited to 1000 SMS per hour using the free plan of the API.
Be aware of the laws and regulations regarding SMS usage in your country, and use this tool responsibly.
Troubleshooting
If you're getting an error message or if the SMS isn’t sent, check the following:
Ensure the phone number format is correct (20 digits, numeric).
Make sure your API key is properly pasted and you haven't exceeded your usage limits.
Confirm that the delay between messages is a reasonable amount of time to avoid rate-limiting.
License
This project is open-source under the MIT License. Feel free to use and modify the code.

Disclaimer
We are NOT responsible for any misuse of this script. Use it at your own risk and ensure you have proper authorization to send SMS messages to the target phone number.

Have fun and use it responsibly!

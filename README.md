# Rotator-email-bomber
Email Bomber v2.1 with Temp Mail API
Overview

This script is an email bomber tool that allows you to send bulk emails to a target email address. It provides both custom and predefined bombing modes, and also allows you to use temporary email addresses through the Temp Mail API or your personal email address. The script is intended for educational purposes only and should not be used for any unethical or illegal activities.

Important: Unauthorized use of this script is prohibited and could result in legal consequences. Ensure you have explicit permission from the target before using this tool.
Features

    Customizable Email Bombing: Choose from predefined bombing modes (1000, 500, 250) or input a custom number of emails to send.
    Temporary Email: Use the Temp Mail API to generate a temporary email address for sending emails, ensuring anonymity.
    Attachments: Option to attach files to the emails.
    Rate Limiting: Sends emails with a 1-second delay between them to avoid overwhelming the target’s inbox too quickly.
    SMTP Support: Uses Gmail's SMTP server for sending emails.

Prerequisites

    Python 3.x
    Required Python Libraries:
        smtplib
        getpass
        requests
        time
        csv
        email

You can install the necessary libraries with the following command:

pip install requests

Setup
1. Clone the Repository or Download the Script

You can clone the repository or download the script file.
2. API Key Setup (For Temp Mail API Usage)

If you want to use the Temp Mail API to generate a temporary email, you’ll need to obtain an API key.

    Go to Temp Mail API and register for an API key.
    When running the script, you will be prompted to enter your Temp Mail API key.

Usage

    Run the script:

python email_bomber.py

    Follow the prompts to:
        Enter the target email address.
        Select the bombing mode or input a custom number of emails to send.
        Choose whether to use the Temp Mail API or your personal email address.
        If you choose to use your personal email, provide your email address and password.
        Optionally, add an attachment to the email.

    Once setup is complete, the script will begin sending the emails to the target.
<br>
Example
<br>
<br>
+[+[+[ Email-Bomber v2.1 with Temp Mail API ]+]+]+<br>
+[+[+[ Ethical Use Only ]+]+]+<br>
...<br>
Enter target email <: victim@example.com   <br>
Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: 1<br>
You have selected BOMB mode: 1 and 1000 emails<br>
Do you want to use a temporary email via API? (yes/no): yes<br>
Enter your Temp Mail API Key: **********<br>
Temporary email generated: example1234@temp-mail.org<br>
Enter subject <: Test Email Bomb<br>
Enter message <: This is a test message.<br>
Do you want to add an attachment? (yes/no): no<br>
<br>
Starting Attack...<br>
BOMB: 1<br>
BOMB: 2<br>
...<br><br>
Attack finished<br>
<br>
<br>
<br>
Disclaimer
<br>
This script is for educational purposes only. Unauthorized use is prohibited. Do not use this tool to spam or harm others. Always get explicit permission before testing this script on any target.<br>
<br>
License
<br>
This script is open-source and free to use for educational purposes. However, it comes with no warranty or guarantee. Use it responsibly and ethically

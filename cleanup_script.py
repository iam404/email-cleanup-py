import imaplib
from pprint import pprint

def open_connection():
    connection = imaplib.IMAP4_SSL("imap.gmail.com") # Hostname here
    username = "" # Username here
    password = "" #password here
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection()
    try:
        print(c)
        typ, data = c.list()
        print('Response code:', typ)
        print('Response:')
        pprint(data)
        msg = c.select('INBOX')
        #emails = c.search(None, 'FROM', '"mail-noreply@google.com"') #for seletected senders
        emails = c.search(None, 'ALL')
        emails = emails[0].split()

        if len(emails) == 0:
            print("No emails found, finishing...")
        else:
            c.store('1:*', '+X-GM-LABELS', '\\Trash')
            c.expunge()
    finally:
        c.logout()




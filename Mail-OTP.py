import smtplib
import random

MAIL = 'smartboympro@gmail.com'
PASSWD = 'vuqxvwfxryyrrnoh'
PORT = 587
SERVER = 'smtp.gmail.com'
REC = input("enter receiver's email : ")
code = random.randint(100000, 999999)
MSG = f"""\
Subject: OTP
\n\n
Your OTP code: {code}
"""

with smtplib.SMTP(SERVER, PORT) as server:
    server.starttls()
    server.login(MAIL, PASSWD)
    server.sendmail(MAIL, REC, MSG)
    print('\nyour verify code sent to your email\n')

verify_code = int(input('enter your received verify code : '))
if verify_code == code:
    print('\nyour verification was successful!!!\n')
else:
    print('\nyour verification was unsuccessful!!!\n')

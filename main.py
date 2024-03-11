from flask import Flask, render_template, request, redirect
import smtplib
import random

MAIL = 'smartboympro@gmail.com'
PASSWD = 'vuqxvwfxryyrrnoh'
PORT = 587
SERVER = 'smtp.gmail.com'
code = random.randint(100000, 999999)
MSG = f"""\
Subject: OTP
\n\n
Your OTP code: {code}
"""


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def _():
    if request.method == 'POST':
        REC = request.form['email']
        if REC:
            with smtplib.SMTP(SERVER, PORT) as server:
                server.starttls()
                server.login(MAIL, PASSWD)
                server.sendmail(MAIL, REC, MSG)

                return redirect('verify')

    return render_template('index.html')

@app.route("/verify", methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        verify_code = request.form['code']
        if verify_code:
            if int(verify_code) == code:
                return 'your verification was successful!!!'
            else:
                return 'your verification was unsuccessful!!!'
    return render_template('verify.html')


if __name__ == '__main__':
    app.run(debug=True)
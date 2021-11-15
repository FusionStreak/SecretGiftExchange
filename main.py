from email import message
import smtplib
import ssl
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
srcEmail = input("Type in source email: ")
password = input("Type your password and press enter: ")

srcFile = input("Type in path to partcipant info file: ")

particpants = dict()
with open(srcFile) as file:
    for line in file:
        l = line.split(", ")
        particpants[l[0]] = l[1][:-1]

matchup = dict()
selected = []
for part in particpants:
    matchup[part] = random.sample(sorted(particpants), 1)[0]
    while (matchup[part] == part) or (matchup[part] in selected):
        matchup[part] = random.sample(sorted(particpants), 1)[0]
    selected.append(matchup[part])

print(matchup)

# Create a secure SSL context
context = ssl.create_default_context()

msgTxt = """\
    Hello {person},

    You are part of a gift exchange.

    Your randomaly selected recipient is: {match}
    """

msgHTML = """\
    <html>
        <body>
            <p>Hello {person}, <br>
                You are part of a gift exchange.<br>
                Your randomaly selected recipient is: {match}
            </p>
        </body>
    </html>
    """


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(srcEmail, password)
    for part in particpants:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Secret Gift Exchange!"
        message["From"] = srcEmail
        message["To"] = particpants[part]
        message.attach(MIMEText(msgTxt.format(
            person=part, match=matchup[part]), "plain"))
        message.attach(MIMEText(msgHTML.format(
            person=part, match=matchup[part]), "html"))
        server.sendmail(srcEmail, particpants[part], message.as_string())

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
# Define your email parameters
sender_email = 'YOUR_EMAIL'
sender_password = 'YOUR_PASSWORD'
receiver_email = 'jonjones@gmail.com'
subject = 'UFC invitation'

# Set up the message headers
email['from'] = 'Name'
email['to'] = receiver_email
email['subject'] = subject

# Add the body of the message
email.set_content(html.substitute({'name': 'Name'}), 'html')

# Connect to the SMTP server and send the message
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.send_message(email)


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ted##uro'
email['to'] = 't8s######o@##il.com'
email['subject'] = 'You won 1,000,000 USD'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('t8sh#####l.com', '##E3####C')
    smtp.send_message(email)
    print('all good boss!')

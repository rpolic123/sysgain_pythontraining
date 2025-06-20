import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Automation Test'
msg['From'] = 'you@example.com'
msg['To'] = 'recipient@example.com'
msg.set_content('This is an automated email.')

with open('report.pdf', 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='report.pdf')

with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login('you@example.com', 'your_password')
    server.send_message(msg)
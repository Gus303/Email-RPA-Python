import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('EMAIL_PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL')
subject = "Automated Email from Python RPA"
body = """
    <h1>Hello!</h1>
    <p>This is an automated email sent using Python.</p>
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'html'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    server.send_message(msg)
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {e}")

finally:
    server.quit()

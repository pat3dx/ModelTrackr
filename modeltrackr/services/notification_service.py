```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NotificationService:
    def __init__(self, smtp_server, smtp_port, email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_notification(self, recipient_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, recipient_email, text)
        server.quit()
```
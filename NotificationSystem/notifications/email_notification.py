from notifications.notification import Notification
import re
class EmailNotification(Notification):
    def __init__(self,recipient_email:str,subject:str,body:str):
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body
        self.validate_notification()
    
    def validate_notification(self):
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, self.recipient_email):
            raise ValueError("Invalid Email Address")
        if not self.subject.strip():
            raise ValueError("subject must not be empty")

    def send_notification(self):
        message = f"""
            Hi {self.recipient_email},
            Subject:{self.subject}
            {self.body}
        """    
        print(message)


import re
import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from notifications.notification import Notification

class EmailNotification(Notification):
    def __init__(self,recipient_email:str,subject:str,body:str):
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body
        self.validate_notification()

    def validate_notification(self):
        pattern = r"^[a-zA-z0-9,_%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, self.recipient_email): 
            raise ValueError("Invalid Email Address")
        if not self.subject.strip():
            raise ValueError("Subject should not be empty")
    
    def send_notification(self):
        message = f"""
            Hi, 
            Subject:{self.subject},
            {self.body}
        """
        print(message);


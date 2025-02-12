import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(),'..')))

from notifications.notification import Notification
import re


class SmsNotification(Notification):
    def __init__(self,phone_no:str,message:str):
        self.phone_no = phone_no
        self.message = message
        self.validate_notification()

    def validate_notification(self):
        if not self.phone_no.isdigit() or len(self.phone_no) not in [10]:
            raise ValueError("must be a valid 10 digit number")
        if not self.message.strip():
            raise ValueError("Message should not be empty")
        if len(self.message)>160: 
            raise ValueError("Must not exceed 160 characters")
    def send_notification(self):
        print(f"Notificaiton Message:{self.message}")




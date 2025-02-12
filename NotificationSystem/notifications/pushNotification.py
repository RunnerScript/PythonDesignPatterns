import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(),'..')))

from notifications.notification import Notification

class PushNotification(Notification):
    def __init__(self,device_id:int,message:str,app_id:int):
        self.device_id = device_id
        self.message = message
        self.app_id = app_id

    def validate_notification(self):
        if not self.device_id.strip():
            raise ValueError("Devide id not found")
        if not self.app_id.strip():
            raise ValueError("App id not found")
        if not self.message.strip():
            raise ValueError("Message should not be empty")
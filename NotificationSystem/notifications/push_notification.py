from notifications.notification import Notification

class PushNotification(Notification):
    def __init__(self,device_id:str,message:str,app_id:str):
        self.device_id = device_id
        self.message = message
        self.app_id = app_id
        self.validate_notification()

    def validate_notification(self):
        if not self.device_id.strip():
            raise ValueError("Missing device id")
        if not self.app_id.strip():
            raise ValueError("Missing app id")
        if not self.message.strip():
            raise ValueError("message must not be empty")

    def send_notification(self):
        print({self.device_id},{self.app_id},{self.message},end=' ')

    
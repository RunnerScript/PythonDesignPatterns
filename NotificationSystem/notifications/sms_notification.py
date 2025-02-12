from notifications.notification import Notification
class SmsNotification(Notification):
    def __init__(self,phone_no:str,message:str):
        self.phone_no = phone_no
        self.message = message
        self.validate_notification()
    
    def validate_notification(self):
        if not self.phone_no.isdigit() or len(self.phone_no) not in [10]:
            raise ValueError("Invalid Phone No")
        if not self.message.strip():
            raise ValueError("message must not be empty")
        if len(self.message)>160:
            raise ValueError("message must not exceed 160 characters")
            
    def send_notification(self):
        print(f"Hello {self.phone_no},{self.message}")

    

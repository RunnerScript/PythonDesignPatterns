import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(),'..')))
from notifications.emailNotification import EmailNotification
from notifications.smsNotification import SmsNotification
from notifications.pushNotification import PushNotification
from notifications.notification_type import NotificationType
class NotificationFactory:

    @staticmethod
    def create_notification(notification_type:NotificationType,**kwargs):
        if notification_type == NotificationType.EMAIL:
            return  EmailNotification(**kwargs)
        elif notification_type == NotificationType.SMS:
            return SmsNotification(**kwargs)
        elif notification_type == NotificationType.PUSH:
            return PushNotification(**kwargs)
        else:
            raise ValueError("Invalid Notification Type")
 
    
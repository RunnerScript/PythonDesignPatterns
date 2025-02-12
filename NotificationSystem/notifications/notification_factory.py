from notifications.notification_type import NotificationType
from notifications.email_notification import EmailNotification
from notifications.sms_notification import SmsNotification
from notifications.push_notification import PushNotification

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type:NotificationType,**kwargs):
        if notification_type == NotificationType.EMAIL:
            return EmailNotification(**kwargs)
        elif notification_type == NotificationType.SMS:
            return SmsNotification(**kwargs)
        elif notification_type == NotificationType.PUSH:
            return PushNotification(**kwargs)
    
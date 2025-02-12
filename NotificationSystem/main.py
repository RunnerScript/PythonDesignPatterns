from notifications.notificationFactory import NotificationFactory
from notifications.notification_type import NotificationType
if __name__ == "__main__":
    email = NotificationFactory.create_notification(
        NotificationType.EMAIL,
        recipient_email="user@example.com",
        subject="Hello!",
        body="This is a test email."
    )
    email.send_notification()
    email = NotificationFactory.create_notification(
        NotificationType.SMS,
        phone_no='9174373248',
        message="Hello I am pradeep Yadav"
    )
    email.send_notification()
    
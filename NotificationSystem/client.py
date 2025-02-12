from notifications.notification_factory import NotificationFactory
from notifications.notification_type import NotificationType

if __name__ == '__main__':
    # Email Notification
    emailNotification = NotificationFactory.create_notification(
        NotificationType.EMAIL,
        recipient_email = "pradeepy1121@gmail.com",
        subject = "Test Notification",
        body="This is just a demo notifiation to check notification"
    )
    emailNotification.send_notification()

    # SMS Notificaiton
    smsNotification = NotificationFactory.create_notification(
        NotificationType.SMS,
        phone_no = '9174373248',
        message = 'This is a demo SMS Notification'
    )
    smsNotification.send_notification()

    #Push Notification 
    pushNotification = NotificationFactory.create_notification(
        NotificationType.PUSH,
        device_id = '1234',
        message = "This is a demo Message",
        app_id = '1'
    )
    pushNotification.send_notification()

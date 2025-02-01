class Notification:
    def __init__(self,notification):
        self.notification=notification
    def send():
        pass
class EmailNotification(Notification):
    def send(self):
        print(f"Email Notification: {self.notification}")
class SMSNotification(Notification):
    def send(self):
        print(f"SMS Notification: {self.notification}")        
e=EmailNotification("This is email")
s=SMSNotification("This is SMS")
e.send()
s.send()
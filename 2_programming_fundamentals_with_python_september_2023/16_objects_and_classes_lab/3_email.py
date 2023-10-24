class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


information = input()
emails = []

while information != "Stop":
    information = information.split()
    mail_sender = information[0]
    mail_receiver = information[1]
    mail_content = information[2]
    email = Email(mail_sender, mail_receiver, mail_content)
    emails.append(email)

    information = input()

indices = input().split(', ')
indices_as_integer = [int(index) for index in indices]

for index in indices_as_integer:
    if 0 <= index < len(emails):
        emails[index].send()

for email in emails:
    print(email.get_info())

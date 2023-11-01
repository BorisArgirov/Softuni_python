class Email:
    def __init__(self, sender, reciever, content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"

final_emails = []
info = input()
while info != "Stop":
    sender, reciever,content = info.split()
    email_info = Email(sender, reciever, content)
    final_emails.append(email_info)
    info = input()
indexes = [int(index) for index in input().split(', ')]
for index in indexes:
    final_emails[index].send()
for current_email in final_emails:
    print(current_email.get_info())
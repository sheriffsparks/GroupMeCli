
class Chat(object):
    def __init__(self, created_at, updated_at, message_count, other_user, last_message,last_sender):
        self.created_at=created_at
        self.updated_at=updated_at
        self.message_count = message_count
        self.other_user=other_user
        self.last_message=last_message
        self.last_sender=last_sender
    def showName(self):
        return self.other_user.nickname
    def getID(self):
        return self.other_user.user_id
    def showMessageCount(self):
        return self.message_count
    def showLastMessage(self):
        return self.last_message
    def showLastSender(self):
        return self.last_sender


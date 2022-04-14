class Message:
    def __init__(self, message_id: int, body: str, sender: str):
        self.message_id = message_id
        self.body = body
        self.sender = sender
        self.is_read = False

    def __str__(self):
        return f"id = {self.message_id}\ncontent: {self.body}\nfrom {self.sender}\n"

    @property
    def is_read(self):
        return self.__is_read

    @is_read.setter
    def is_read(self, is_read: bool):
        self.__is_read = is_read


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    Note: My changes- boxes now including list of massage and boolean which describes if message
    read before or not.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: list[str]):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender: str, recipient: str, message_body: str, urgent: bool = False) -> int:
        """Send a message to a recipient.

        Note: My changes- boxes now including list of massage and boolean which describes if message
        read before or not.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name: str, number_of_messages: int = None):
        """

        :param user_name:
        :param number_of_messages:
        :return:
        """
        if number_of_messages is None or number_of_messages > len(self.boxes[user_name]):
            number_of_messages = len(self.boxes[user_name])
        elif number_of_messages < 0:
            return []
        return_list = [str(message) for message in self.boxes[user_name][:number_of_messages] if not message.is_read]
        return return_list


def main_post_office() -> None:
    my_post_office = PostOffice(["Aviv", "Tal", "Yam", "Itay"])
    my_post_office.send_message("Aviv", "Tal", "Hey", True)
    my_post_office.send_message("Yam", "Tal", "Hello")
    my_post_office.send_message("Itay", "Tal", "Hi")
    print([str(message) for message in my_post_office.read_inbox("Tal", 2)])
    #print(my_post_office.read_inbox("Tal", 1))
    #print(my_post_office.read_inbox("Tal"))


if __name__ == "__main__":
    main_post_office()

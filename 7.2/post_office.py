from typing import Type


class Message:
    """ A Message class. Allow create message with all of its details.

    :ivar message_id: The id of the message.
    :ivar body: The body of the message.
    :ivar sender: The name of the person that sent the message.
    :ivar is_read: Flag to mark that the current message read before.

    :param message_id: The id of the message.
    :param body: The body of the message.
    :param sender: The name of the person that sent the message.
    """

    def __init__(self, message_id: int, body: str, sender: str):
        self.message_id = message_id
        self.body = body
        self.sender = sender
        self.is_read = False

    def __str__(self):
        return f"id = {self.message_id}\ncontent: {self.body}\nfrom {self.sender}\n"

    def is_string_in_body(self, string: str) -> bool:
        """ Returns if string appear inside message's body.

        :param str string: String to search for it inside message's content.
        :return: True if it is, otherwise false.
        """
        return string in self.body

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

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: list[str]):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender: str, recipient: str, message_body: str, urgent: bool = False) -> int:
        """Send a message to a recipient.

        Note: My changes- Message now is an class object that include all of the details about it that was here
        before. I think it's more appropriate.

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

    def read_inbox(self, user_name: str, number_of_messages: int = None) -> list[Type[Message]]:
        """ Return list of the first number_of_messages messages of wanted user and mark them as read.

        :param user_name: Wanted user's box.
        :param number_of_messages: Optional, to read the first number of messages at the box.
               Note: If the value is illegal, all of the messages return.
        :return: List of wanted messages.
        :raises KeyError: If user name doesn't exist.
        """
        if number_of_messages is None or not 0 <= number_of_messages <= len(self.boxes[user_name]):
            number_of_messages = len(self.boxes[user_name])

        # Written like this because I wanted to mark all of the messages as read.
        return_lst = []
        for message in self.boxes[user_name][:number_of_messages]:
            if not message.is_read:
                message.is_read = True
                return_lst.append(message)
        return return_lst

    def search_inbox(self, user_name: str, string: str) -> list[Type[Message]]:
        """ Return all the messages inside user_name's box that include at their body the string.

        :param user_name: Wanted user_name's box to search in.
        :param string: String to search for.
        :return: List of the messages that including the string at their body.
        :raises KeyError: If user name doesn't exist.
        """
        return [message for message in self.boxes[user_name] if message.is_string_in_body(string)]


def main_post_office() -> None:
    """ Checking wanted post office's functions.
    :return: None.
    """
    my_post_office = PostOffice(["Shay", "Emanuel", "Sharon", "Itzik"])
    my_post_office.send_message("Shay", "Itzik", "Hi, it's me. How are you?", True)
    my_post_office.send_message("Emanuel", "Itzik", "Hello Itzik,\nAre you looking for a job?")
    my_post_office.send_message("Sharon", "Itzik", "Hi")
    print("\n".join([str(message) for message in my_post_office.read_inbox("Itzik", 2)]))
    print("\n".join([str(message) for message in my_post_office.read_inbox("Itzik", 3)]))
    print("\n".join([str(message) for message in my_post_office.search_inbox("Itzik", "?")]))


if __name__ == "__main__":
    main_post_office()

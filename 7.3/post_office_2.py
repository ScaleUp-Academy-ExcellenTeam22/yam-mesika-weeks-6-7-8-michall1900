"""
Note: A Post office class is not here because I already made message class at post_office1 exercise
      and just added here __len__ function (to message class).
"""


class Message:
    """ A Message class. Allow create message with all of its details.

    :ivar message_id: The id of the message.
    :ivar title: The title of the message.
    :ivar body: The body of the message.
    :ivar sender: The name of the person that sent the message.
    :ivar is_read: Flag to mark that the current message read before.

    :param message_id: The id of the message.
    :param title: The title of the message.
    :param body: The body of the message.
    :param sender: The name of the person that sent the message.
    """

    def __init__(self, message_id: int, title: str, body: str, sender: str):
        self.message_id = message_id
        self.title = title
        self.body = body
        self.sender = sender
        self.is_read = False

    def __str__(self):
        return f"id = {self.message_id}\ntitle: {self.title}\ncontent: {self.body}\nfrom {self.sender}\n"

    def __len__(self):
        """ Return message's content length. """
        return len(self.body)

    def is_string_in_message(self, string: str) -> bool:
        """ Returns if string appear inside message's body.

        :param str string: String to search for it inside message's content.
        :return: True if it is, otherwise false.
        """
        return string in self.body or string in self.title

    @property
    def is_read(self):
        return self.__is_read

    @is_read.setter
    def is_read(self, is_read: bool):
        self.__is_read = is_read


def main_message():
    """ Print result of some functions.
    :return: None.
    """
    message = Message(1, "Interested you", "Hey, how are you?", "Michal")
    print(f"Result of print message:\n{message}")
    print(f"Message length is: {len(message)}")
    print("Result of searching for the word 'Hey': ", message.is_string_in_message('Hey'))
    print("Result of searching for the word 'Interested': ", message.is_string_in_message('Interested'))
    print("Result of searching for the word 'hello': ", message.is_string_in_message('hello'))


if __name__ == "__main__":
    main_message()

from abc import ABC, abstractmethod
from typing import Literal, Tuple, Union


FILE_TYPE = Literal["binary", "txt", "directory"]
POSSIBLE_FILE_TYPE = Union['TextualFile', 'BinaryFile', 'Directory']


class User(ABC):
    """ A User class. Have a user name and password.

    :ivar user_name: User name's string.
    :ivar password: User's password.

    :param user_name: Wanted user's name.
    :param password: Wanted password.

    """
    @abstractmethod
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

    def get_user_name(self) -> str:
        """ Returns user's name.
        :return: user's name.
        """
        return self.user_name

    def create_file(self, file_type: FILE_TYPE = "txt", file_name: str = "",
                    content: str = "") -> POSSIBLE_FILE_TYPE:
        """ Create file and return it to user.
        :param file_type: File type could be 'txt' for text file, 'binary' for binary file and 'directory' for
                          directory.
        :param file_name: The wanted name for file.
        :param content: The content of the file (when the file is textual or binary).
        :return: File object (TextualFile / BinaryFile/ Directory).
        """
        if file_type == "binary":
            return BinaryFile(file_name, content, self)
        elif file_type == "txt":
            return TextualFile(file_name, content, self)
        elif file_type == "directory":
            return Directory(file_name)


class SystemAdministratorUser(User):
    """ A System administrator user class. Inherits from User class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RegularUser(User):
    """ A Regular user class. Inherits from User class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class File(ABC):
    """ A File class to manage files.

    :ivar file_name: File's name.

    :param file_name: File's name.

    """
    @abstractmethod
    def __init__(self, file_name: str):
        self.file_name = file_name

    def rename(self, new_name: str = "") -> None:
        """ Rename file's name.
        :param new_name: The new file's name.
        :return: None.
        """
        self.file_name = new_name

    def get_name(self) -> str:
        """ Returns file's name.
        :return: File's name.
        """
        return self.file_name

    def __str__(self) -> str:
        return str(self.file_name)


class ReadableFile(File):
    """ A Readable file class to gather all readable functions into one class.

    :ivar file_name: File's name.
    :ivar float _weight_in_kilobytes: The weight of the file in kilobytes.
    :ivar content: File's content.
    :ivar _creator: User's object to hold the details about the creator of that file.

    :param file_name: File's name.
    :param content: File's content.
    :param creator: User's object to hold the details about the creator of that file.

    """
    _NUMBER_OF_BYTES_IN_KILOBYTE = 1024

    def __init__(self, file_name: str, content: str = "", creator: User = None):
        super().__init__(file_name)
        self._content = ""
        self._weight_in_kilobytes = 0.0
        self._creator = creator
        self.set_content(content)

    def read(self, user: User) -> Union[str, None]:
        """ Check if the user that wants to read the file is the one who creates it or the Administrator.
         If it is, return the file's content. Else, None.

        :param user: User's object.
        :return: The file's content or None depends on what kind of user is.
        """
        if user == self._creator or isinstance(user, SystemAdministratorUser):
            return self._content

    def set_content(self, content: str) -> None:
        """ Sets file's content and changes its weight according to the new content.

        :param content: The new content.
        :return: None.
        """
        self._content = content
        self._weight_in_kilobytes = len(self._content.encode('utf-8')) / self._NUMBER_OF_BYTES_IN_KILOBYTE


class TextualFile(ReadableFile):
    """ A Textual File class, inherits from ReadableFile class.
    """
    def count(self, search_for_string: str) -> int:
        """ Receives a string and returns how many times it appears inside the file's content.

        :param search_for_string: String to search for it inside file's content.
        :return: How many time it appeared.
        """
        return self._content.lower().count(search_for_string.lower())


class BinaryFile(ReadableFile):
    """ A Binary File class, inherits from ReadableFile class.
    """
    def get_dimensions(self) -> Tuple[float, float]:
        """ Returns width and height of the picture.
        :return: Width and height.
        """
        pass


class Directory(File):
    """ A Directory class, inherits from File class.

    :ivar: _my_files: For file list.
    """
    def __init__(self, file_name):
        super().__init__(file_name)
        self._my_files = []

    def add_file(self, file: POSSIBLE_FILE_TYPE) -> None:
        """ Add a file into the list if its name doesn't exist in the files' list.

        :param file: File object.
        :return: None.
        :raises: ValueError if file's name already at the list. 
        """
        try:
            if not self.get_file(file.get_name()):
                self._my_files.append(file)
            else:
                raise ValueError(f"There is already file named {file.get_name()} at the current directory.")

        except ValueError as error:
            print(error)

    def delete_file(self, file_name) -> None:
        """ Delete file from list.
        :param file_name: The wanted file to delete. 
        :return: None.
        """
        self._my_files.pop(self._my_files.index(self.get_file(file_name)))
        
    def __str__(self) -> str:
        return f"In directory named: {self.file_name}\n" + "\n".join([str(file) for file in self._my_files])

    def get_file(self, file_name: str) -> POSSIBLE_FILE_TYPE:
        """ Receives file's name and return it if it is exist.

        :param file_name: File's name.
        :return: One of the possible types of file if it is exist. Else, None.
        """
        for file in self._my_files:
            if file.get_name() == file_name:
                return file


def main_hierarchy() -> None:
    """ Doing some test on The classes.
    :return: None.
    """
    my_user = RegularUser(user_name="user1", password="123")
    other_user = RegularUser(user_name="user2", password="1234")
    admin = SystemAdministratorUser(user_name="admin", password="1111")
    print("Create directory named a")
    my_user_directory = my_user.create_file("directory", "a")
    print("Try to add banana txt file")
    my_user_directory.add_file(my_user.create_file("txt", "banana", "It's my favorite food! food food"))
    print("'a' directory print:\n", my_user_directory)
    print("Trying to add file named 'banana' again:")
    my_user_directory.add_file(my_user.create_file("txt", "banana", "bla bla"))
    print("'a' directory print:\n", my_user_directory)
    print("My user trying to read banana:")
    print(my_user_directory.get_file("banana").read(my_user))
    print("Other user trying to read banana:")
    print(my_user_directory.get_file("banana").read(other_user))
    print("Admin trying to read banana:")
    print(my_user_directory.get_file("banana").read(admin))
    print(f"At file {str(my_user_directory.get_file('banana'))} the number of appearance of the word 'food': ",
          my_user_directory.get_file("banana").count("food"))
    my_user_directory.delete_file("banana")
    print("After delete banana, 'a' directory include:\n", my_user_directory)


if __name__ == "__main__":
    main_hierarchy()

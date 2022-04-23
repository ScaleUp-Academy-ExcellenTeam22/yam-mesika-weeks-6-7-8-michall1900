from datetime import datetime


class LogFileError(Exception):
    """ A LogFileError , inherits from Exception class.
    Created to note that the program should close.

    :ivar: error_message: The error message that caused to that error.

    :param: error_message: The error message as string.

    """
    def __init__(self, error_message: str):
        self.error_message = error_message

    def __str__(self):
        return f"While trying to handle with log.txt file, there was an error:\n{self.error_message}.\n" +\
               "The program should exit now."


def _write_to_log_file(error_message: str, file_path: str, line_number: int) -> None:
    """ Receives error message and the parameters send to get_line_in_file function and write the error into
    file called log.txt with timestamp.

    :param error_message: The error message that raise while trying to return the line number at the wanted file.
    :param file_path: Path to file.
    :param line_number: Index to wanted line in file.
    :return: None.
    """
    try:
        with open("log.txt", "a") as error_file:
            error_file.write(f"At {datetime.now()}, try to run function get_line_in_file with file_path = {file_path}"
                             f" and line_number = {line_number}.\nThe error is: " + error_message + "\n")
    except(OSError, FileNotFoundError) as current_error:
        raise LogFileError(str(current_error))


def get_line_in_file(file_path: str, line_number: int) -> str:
    """ Returns the wanted line's number from the wanted file.
    :param file_path: Path to file.
    :param line_number: The wanted line's number at file.
    :return: The content of the file at the wanted line.
    """
    try:
        with open(file_path, "r") as find_in_file:
            index = line_number - 1
            if line_number <= 0:
                raise ValueError("line_number should be integer and greater than zero")
            return find_in_file.read().split("\n")[index]

    except (OSError, FileNotFoundError, ValueError, TypeError, IndexError) as error:
        _write_to_log_file(str(error), file_path, line_number)
        return ""


def main_the_syndicate() -> None:
    """ Doing test on get_line_in_file function.
    :return: None.
    """
    print(get_line_in_file("?", 5))
    print(get_line_in_file("eiofnwefl", 5))

    """ If there will be file here, you can try this:
    print(get_line_in_file(r"txt.txt", "a"))
    print(get_line_in_file(r"txt.txt", -3))
    print(get_line_in_file(r"txt.txt", 10))
    print(get_line_in_file(r"txt.txt", 1))
    """


if __name__ == "__main__":
    main_the_syndicate()

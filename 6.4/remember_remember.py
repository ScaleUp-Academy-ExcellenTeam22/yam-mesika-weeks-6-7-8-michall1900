from PIL import Image


def find_terrorist_code(path: str) -> str:
    """
    Receives path to an image that includes 256 rows and secretes code_image decrypted with a black pixel.
    The code should appear inside an image as black pixels when black pixel means - take the character
    that appears inside the ASCII table with that row number.
    The function is encrypting the code and returning the encryption as a string.
    :param path: Path into the image.
    :return: The encryption of the image.
    """
    code_image = Image.open(path)
    return "".join([chr(row) for col in range(code_image.width) for row in range(code_image.height)
                    if code_image.getpixel((col, row)) == 1])


def main_remember() -> None:
    """
    Print the code after encrypted it.
    :return: None.
    """
    print(find_terrorist_code("code.png"))


if __name__ == "__main__":
    main_remember()

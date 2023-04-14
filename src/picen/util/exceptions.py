class PicenException(RuntimeError):
    pass


class InvalidKeyValueException(PicenException):
    def __init__(self, key: str):
        super().__init__(f"Invalid key value: '{key}'.\n"
                         f"The key must be either 128 digits in base 2, 32 digits in base 16 or 22 digits in base 64.")


class InvalidBCModeException(PicenException):
    def __init__(self, mode: str):
        super().__init__(f"Invalid block cipher mode: '{mode}'.\n"
                         f"The mode must be either 'ofb' or 'ctr'.")


class InvalidImageModeException(PicenException):
    def __init__(self, mode: str):
        super().__init__(f"Invalid or unsupported image mode: '{mode}'.\n"
                         f"Supported modes: 1, L, RGB, RGBA")


class FileNotFoundException(PicenException):
    def __init__(self, path: str):
        super().__init__(f"File not found at path: '{path}'.")


class CouldNotWriteException(PicenException):
    def __init__(self, path: str):
        super().__init__(f"Could not write in file at path: '{path}'.")


class EncryptionException(PicenException):
    pass


class MalformedImageException(EncryptionException):
    def __init__(self, path: str):
        super().__init__(f"Could not read the image at path: '{path}'.")


class DecryptionException(PicenException):
    pass


class MalformedEncEntryException(DecryptionException):
    def __init__(self, entry: str):
        super().__init__(f"Malformed entry: '{entry}'.\n"
                         f"Entry must be in '<width:int> <height:int> <image_mode:str>' form.")


class MalformedEncBlockException(DecryptionException):
    def __init__(self, block: str):
        super().__init__(f"Malformed block: '{block}'.\n"
                         f"Blocks must be 128 digit binary strings.")


class EntryAndBlocksMismatchException(DecryptionException):
    pass


class MissingBlocksException(EntryAndBlocksMismatchException):
    def __init__(self, entry: str):
        super().__init__(f"Entry data and block count do not match.\n"
                         f"Entry: '{entry}'.\n"
                         f"Total number of blocks are less than the required amount.")


class ExtraBlocksException(EntryAndBlocksMismatchException):
    def __init__(self, entry: str):
        super().__init__(f"Entry data and block count do not match.\n"
                         f"Entry: '{entry}'.\n"
                         f"Total number of blocks are more than the required amount.")


class InvalidValueException(PicenException):
    def __init__(self, variables: list, values: list, extra_description: str = None):
        description = ('\n' + extra_description) if extra_description is not None else ''
        if len(variables) == len(values):
            s = '(s)' if len(variables) > 1 else ''
            length = len(variables)
            lines = ''
            for i in range(length):
                lines += f"\n'{variables[i]}' = '{values[i]}'"
            super().__init__(f"Invalid value{s} for variable{s}:"
                             f"{lines}"
                             f"{description}")
        else:
            super().__init__(f"Invalid value(s) for variable(s):\n"
                             f"Variable(s): '{variables}'\n"
                             f"Value(s): '{values}'"
                             f"{description}")

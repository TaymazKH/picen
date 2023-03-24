class PicenException(RuntimeError):
    pass


class InvalidKeyValueException(PicenException):
    def __init__(self, key: str):
        super().__init__(f"Invalid key value: '{key}'.\n"
                         f"The key must be either 128 digits in base 2, 32 digits in base 16 or 22 digits in base 64.")


class InvalidBCModeException(PicenException):
    def __init__(self, mode: str):
        super().__init__(f"Invalid block cipher mode: '{mode}'.\nThe mode must be either 'ofb' or 'ctr'.")


class MalformedEncTextException(PicenException):
    pass


class MalformedEncEntryException(MalformedEncTextException):
    def __init__(self, entry: str):
        super().__init__(f"Malformed entry: '{entry}'.\n"
                         f"Entry must be in '<width:int> <height:int> <image_mode:str>' form.\n")


class MalformedEncBlockException(MalformedEncTextException):
    def __init__(self, block: str):
        super().__init__(f"Malformed block: '{block}'.\n"
                         f"Blocks must be 128 digit binary strings.")


class EntryAndBlocksMismatchException(MalformedEncTextException):
    pass


class MissingBlocksException(EntryAndBlocksMismatchException):
    def __init__(self, entry: str, block_count: int):
        super().__init__(f"Entry data and block count do not match.\n"
                         f"Entry: '{entry}', block count: '{block_count}'.\n"
                         f"Total number of blocks are less than the required amount.")


class ExtraBlocksException(EntryAndBlocksMismatchException):
    def __init__(self, entry: str, block_count: int):
        super().__init__(f"Entry data and block count do not match.\n"
                         f"Entry: '{entry}', read block count: '{block_count}'.\n"
                         f"Total number of blocks are more than the required amount.")

from itertools import islice
from reader.reader import Reader
from util.exceptions import FileNotFoundException, MalformedEncEntryException, MalformedEncBlockException
from util.validators import is_length128_base2_string


class ImageFileReader(Reader):
    def __init__(self, path):
        self.path = path
        try:
            with open(path):
                pass
        except FileNotFoundError:
            raise FileNotFoundException(path)
        self.index = 1

    def _get_line(self, index):
        line = None
        with open(self.path) as file:
            for block in islice(file, index, index + 1):
                line = block[:-1]
                break
        if not is_length128_base2_string(line):
            raise MalformedEncBlockException(line)
        return line

    def has_unread_block(self) -> bool:
        return self._get_line(self.index) is not None

    def get_next_block(self) -> str:
        line = self._get_line(self.index)
        self.index += 1
        return line

    def get_entry(self):
        try:
            with open(self.path) as file:
                entry = file.readline()
                init_tuple = tuple(entry.split())
            if len(init_tuple) != 3:
                raise Exception()
            return int(init_tuple[0]), int(init_tuple[1]), init_tuple[2]
        except Exception:
            raise MalformedEncEntryException(entry)

    def get_end(self):
        return None

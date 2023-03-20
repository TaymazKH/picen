from itertools import islice
from reader.reader import Reader


class ImageFileReader(Reader):
    def __init__(self, path):
        self.path = path
        self.index = 1

    def _get_line(self, index):
        line = None
        with open(self.path) as file:
            for block in islice(file, index, index + 1):
                line = block[:-1]
                break
        return line

    def has_unread_block(self) -> bool:
        return self._get_line(self.index) is not None

    def get_next_block(self) -> str:
        line = self._get_line(self.index)
        self.index += 1
        return line

    def get_init(self):
        with open(self.path) as file:
            init = tuple(file.readline().split())
        return int(init[0]), int(init[1]), init[2]

    def get_end(self):
        return None

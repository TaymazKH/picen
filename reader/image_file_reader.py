from itertools import islice
from reader.reader import Reader


class ImageFileReader(Reader):
    def __init__(self, path):
        self.path = path
        self.index = 1
        self.unread_line = ''

    def has_unread_block(self) -> bool:
        with open(self.path) as file:
            for block in islice(file, self.index, self.index + 1):
                self.unread_line = block
                break
        return self.unread_line != ''

    def get_next_block(self) -> str:
        self.index += 1
        return self.unread_line

    def get_init(self):
        with open(self.path) as file:
            init = file.readline()
        return int(init[0]), int(init[1]), init[2]

    def get_end(self):
        return None

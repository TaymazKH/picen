from writer.writer import Writer
from util.exceptions import CouldNotWriteException


class ImageFileWriter(Writer):
    def __init__(self, path):
        self.path = path

    def write_next_block(self, block: str):
        with open(self.path, 'a') as file:
            try:
                file.write(block + '\n')
            except Exception:
                raise CouldNotWriteException(self.path)

    def write_entry(self, entry):
        with open(self.path, 'w') as file:
            try:
                file.write(f'{entry[0]} {entry[1]} {entry[2]}\n')
            except Exception:
                raise CouldNotWriteException(self.path)

    def write_end(self, end):
        pass

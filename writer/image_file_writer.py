from writer.writer import Writer


class ImageFileWriter(Writer):
    def __init__(self, path):
        self.path = path

    def write_next_block(self, block: str):
        with open(self.path, 'a') as file:
            file.write(block + '\n')

    def write_init(self, init):
        with open(self.path, 'w') as file:
            file.write(init[0] + init[1] + '\n')

    def write_end(self, end):
        pass

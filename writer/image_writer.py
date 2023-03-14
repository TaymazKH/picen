from PIL import Image
from writer.writer import Writer


class ImageWriter(Writer):
    def __init__(self, path: str = None):
        self.path = path
        self.width = 0
        self.height = 0
        self.image_mode = ''
        self.image = None
        self.pixel_x = 0  # iterates from top to bottom
        self.pixel_y = 0  # iterates from left to right
        self.incomplete_pixel = ''

    def write_next_block(self, block: str):
        pass

    def write_init(self, init):
        self.width = init[0]
        self.height = init[1]
        self.image_mode = init[2]
        self.image = Image.new(self.image_mode, (self.width, self.height))

    def write_end(self, end):
        pass

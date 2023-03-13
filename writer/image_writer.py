from PIL import Image
from writer.writer import Writer


class ImageWriter(Writer):
    def __init__(self, width, height, image_mode, path: str = None):
        self.path = path
        self.width = width
        self.height = height
        self.image_mode = image_mode
        self.pixel_x = 0
        self.pixel_y = 0
        self.incomplete_pixel = ''

    def write_next_block(self, block: str):
        pass

    def write_init(self, init):
        pass

    def write_end(self, end):
        pass

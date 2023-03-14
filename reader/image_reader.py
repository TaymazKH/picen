from PIL import Image
from util.functions import pixel_to_string
from reader.reader import Reader


class ImageReader(Reader):
    def __init__(self, path):
        self.image = Image.open(path)
        self.image.load()
        self.width = self.image.width
        self.height = self.image.height
        self.image_mode = self.image.mode
        self.pixel_x = 0  # iterates from top to bottom
        self.pixel_y = 0  # iterates from left to right
        self.incomplete_block = ''
        self.padded = False

    def has_unread_pixel(self):
        return self.pixel_x < self.height

    def get_next_pixel(self):
        pixel = self.image.getpixel((self.pixel_x, self.pixel_y))
        return pixel_to_string(pixel, self.image_mode)

    def has_unread_block(self) -> bool:
        return not self.padded

    def get_next_block(self) -> str:
        block = self.incomplete_block
        while len(block) < 128:
            if self.has_unread_pixel():
                block += self.get_next_pixel()
            else:
                self.padded = True
                block += '1' + '0' * 127
        self.incomplete_block = block[128:]
        return block[:128]

    def get_init(self):
        return self.width, self.height, self.image_mode

    def get_end(self):
        return None

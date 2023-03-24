from PIL import Image
from reader.reader import Reader
from util.exceptions import FileNotFoundException, MalformedImageException
from util.functions import pixel_to_string


class ImageReader(Reader):
    def __init__(self, path):
        try:
            self.image = Image.open(path)
        except FileNotFoundError:
            raise FileNotFoundException(path)
        except Exception:
            raise MalformedImageException(path)
        self.image.load()
        self.width = self.image.width
        self.height = self.image.height
        self.image_mode = self.image.mode
        self.pixel_x = 0  # iterates from left to right
        self.pixel_y = 0  # iterates from top to bottom
        self.incomplete_block = ''
        self.padded = False

    def has_unread_pixel(self):
        return self.pixel_y < self.height

    def get_next_pixel(self):
        pixel = self.image.getpixel((self.pixel_x, self.pixel_y))
        self.pixel_x += 1
        if self.pixel_x == self.width:
            self.pixel_x = 0
            self.pixel_y += 1
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

    def get_entry(self):
        return self.width, self.height, self.image_mode

    def get_end(self):
        return None

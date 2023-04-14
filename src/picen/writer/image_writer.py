from PIL import Image
from ..util.exceptions import MissingBlocksException, ExtraBlocksException, CouldNotWriteException, InvalidValueException
from ..util.functions import string_to_pixel, get_pixel_string_length
from .writer import Writer


class ImageWriter(Writer):
    def __init__(self, path: str = None):
        self.path = path
        self.entry = ''
        self.width = 0
        self.height = 0
        self.image_mode = ''
        self.pixel_str_len = 0
        self.image = None
        self.pixel_access = None
        self.pixel_x = 0  # iterates from left to right
        self.pixel_y = 0  # iterates from top to bottom
        self.incomplete_pixel = ''

    def is_image_incomplete(self):
        return self.pixel_y < self.height

    def write_pixel(self, pixel):
        self.pixel_access[self.pixel_x, self.pixel_y] = pixel
        self.pixel_x += 1
        if self.pixel_x == self.width:
            self.pixel_x = 0
            self.pixel_y += 1

    def write_next_block(self, block: str):
        if not self.is_image_incomplete():
            raise ExtraBlocksException(self.entry)
        block = self.incomplete_pixel + block
        while len(block) >= self.pixel_str_len and self.is_image_incomplete():
            pixel_str = block[:self.pixel_str_len]
            pixel = string_to_pixel(pixel_str, self.image_mode)
            self.write_pixel(pixel)
            block = block[self.pixel_str_len:]
        self.incomplete_pixel = block

    def write_entry(self, entry):
        self.width = entry[0]
        self.height = entry[1]
        self.image_mode = entry[2]
        self.pixel_str_len = get_pixel_string_length(self.image_mode)
        self.image = Image.new(self.image_mode, (self.width, self.height))
        self.pixel_access = self.image.load()

    def write_end(self, end):
        if self.is_image_incomplete():
            raise MissingBlocksException(self.entry)
        if self.path is None:
            self.image.show()
        else:
            try:
                self.image.save(self.path)
            except ValueError:
                raise InvalidValueException(['path'], [self.path], 'Could not determine output format.')
            except OSError:
                raise CouldNotWriteException(self.path)

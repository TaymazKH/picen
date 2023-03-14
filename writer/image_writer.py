from PIL import Image
from util.functions import string_to_pixel, get_pixel_string_length
from writer.writer import Writer


class ImageWriter(Writer):
    def __init__(self, path: str = None):
        self.path = path
        self.width = 0
        self.height = 0
        self.image_mode = ''
        self.pixel_str_len = 0
        self.image = None
        self.pixel_x = 0  # iterates from left to right
        self.pixel_y = 0  # iterates from top to bottom
        self.incomplete_pixel = ''

    def is_image_incomplete(self):
        return self.pixel_y < self.height

    def write_pixel(self, pixel):
        self.image[self.pixel_x, self.pixel_y] = pixel
        self.pixel_x += 1
        if self.pixel_x == self.width:
            self.pixel_x = 0
            self.pixel_y += 1

    def write_next_block(self, block: str):
        block = self.incomplete_pixel + block
        while len(block) >= self.pixel_str_len and self.is_image_incomplete():
            pixel_str = block[:self.pixel_str_len]
            pixel = string_to_pixel(pixel_str, self.image_mode)
            self.write_pixel(pixel)
            block = block[self.pixel_str_len:]
        self.incomplete_pixel = block

    def write_init(self, init):
        self.width = init[0]
        self.height = init[1]
        self.image_mode = init[2]
        self.pixel_str_len = get_pixel_string_length(self.image_mode)
        self.image = Image.new(self.image_mode, (self.width, self.height))

    def write_end(self, end):
        pass

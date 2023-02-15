from PIL import Image


class ImageReader:
    def __init__(self, path):
        self.image = Image.open(path)
        self.image.load()
        self.pixel_x = 0
        self.pixel_y = 0
        self.width = self.image.width
        self.height = self.image.height
        self.image_mode = self.image.mode
        self.incomplete_block = ''
        self.padded = False

    def has_unread_pixel(self):
        pass

    def get_next_pixel(self):
        pass

    def has_unread_block(self):
        return not self.padded

    def get_next_block(self):
        block = self.incomplete_block
        while len(block) < 128:
            if self.has_unread_pixel():
                block += self.get_next_pixel()
            else:
                self.padded = True
                block += '1' + '0' * 127
        self.incomplete_block = block[128:]
        return block[:128]

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
        self.half_read_block = ''

    def has_unread_pixel(self):
        pass

    def get_next_pixel(self):
        pass

    def has_unread_block(self):
        pass

    def get_next_block(self):
        pass

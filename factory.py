from lib.backend import get_img
from key_file import get_api_key

class Factory:
    def __init__(self, date, rover):
        self.date = date
        self.rover = rover
        self.images = []

    def search_api_imgs(date,rover):
        api_images = get_img(get_api_key(),date,rover)
        self.images.append(api_images)
        return self

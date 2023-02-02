from lib.api_query import get_img
from key_file import get_api_key

class Factory:
    def __init__(self, date, rover):
        self.date = date
        self.rover = rover
        self.images = []

    def search_api_imgs(self):
        api_images = get_img(get_api_key(),self.date,self.rover)
        self.images.append(api_images)
        return self

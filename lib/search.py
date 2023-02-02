from key_file import get_api_key
from lib.api_query import get_img

def search_api_imgs(date,rover):
    api_images = get_img(get_api_key(),date,rover)
    return api_images
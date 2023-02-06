import requests


def get_img(api_key,date,rover):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
    req_url = base_url + rover + "/photos?earth_date=" + date + "&api_key=" + api_key
    response = requests.get(req_url).json()
    return eval_payload(response)

def eval_payload(data):
    if 'error' in data:
        return data
    else:
        photo_json = data['photos']
        photos = []
        for i in photo_json:
            photos.append(i['img_src'])
        return photos
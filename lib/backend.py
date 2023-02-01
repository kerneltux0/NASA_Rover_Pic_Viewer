import requests

def get_img(api_key,date,rover):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
    req_url = base_url + rover + "/photos?earth_date=" + date + "&api_key=" + api_key
    response = requests.get(req_url).json()
    return response
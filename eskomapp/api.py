# eskomapp/api.py
import requests
from django.http import HttpResponse

BASE_URL = 'https://developer.sepush.co.za/business/2.0'
with open('token.txt', 'r') as token_file:
    TOKEN = token_file.read().strip()

headers = {
    'token': TOKEN,
}

def search_areas(text):
    # url = f'{BASE_URL}/areas_search?test=true&text={text}'  # Add the 'test' query parameter
    url = f'{BASE_URL}/areas_search?text={text}'  # Add the 'test' query parameter
    response = requests.get(url, headers=headers)
    # if response.status_code == 429:
    #     return HttpResponse('Rate limit exceeded', status=429)
        # raise Exception('Rate limit exceeded')
    return response.json()

def get_area_info(area_id):
    # url = f'{BASE_URL}/area?test=true&id={area_id}'
    url = f'{BASE_URL}/area?id={area_id}'
    response = requests.get(url, headers=headers)
    area_info = response.json()

    return area_info['info'], area_info['events']

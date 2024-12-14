import requests
from django.core.cache import cache
from rest_framework import exceptions

from CSA_test_task.settings import CAT_API_URL, BREED_CACHE_KEY


class Breeds:

    @staticmethod
    def __fetch_breeds_from_api():
        response = requests.get(CAT_API_URL)
        if response.status_code == 200:
            breeds = response.json()
            breed_names = [breed['name'] for breed in breeds]
            cache.set(BREED_CACHE_KEY, breed_names, 60 * 30)
            return breed_names
        raise exceptions.APIException('Failed to fetch breeds')

    @classmethod
    def get_breeds(cls):
        breeds = cache.get(BREED_CACHE_KEY)
        if not breeds:
            breeds = cls.__fetch_breeds_from_api()
        return breeds

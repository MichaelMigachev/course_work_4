import os

from src.abstract_class import API
import requests
import json

class HH_API(API):
    HH_API_URL = 'https://api.hh.ru/vacancies'
    HH_API_URL_AREAS = 'https://api.hh.ru/areas'

    def __init__(self, keyword):
        self.params = {
            'per_page': 100,
            'text': keyword,
            'area': 67
        }
        self.keyword = keyword
    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.params['per_page']}', {self.params['text']},"
                f" {self.params['area']}')")

    def get_vacancies(self):
        '''вакансии'''
        response = requests.get(self.HH_API_URL, self.params)
        return response.json()
        # response_data = json.loads(response.text)
        # if 'items' in response_data:
        #     return response_data['items']
        # else:
        #     return []


    def load_areas(self):
        '''список городов'''
        req = requests.get(self.HH_API_URL_AREAS)
        dict_areas = req.json()

        areas = {}
        for k in dict_areas:
            for i in range(len(k['areas'])):
                if len(k['areas'][i]['areas']) != 0:
                    for j in range(len(k['areas'][i]['areas'])):
                        areas[k['areas'][i]['areas'][j]['name'].lower()] = k['areas'][i]['areas'][j]['id']
                else:
                    areas[k['areas'][i]['name'].lower()] = k['areas'][i]['id']
        return areas

    def formate_vacancies(self, all_vacancies):
        vacancies = {'vacancies': []}
        for vacancy in all_vacancies['items']:
            if vacancy['salary'] is None:
                salary = "З/п не указана"
            elif vacancy['salary']['from'] is None:
                salary = vacancy['salary']['to']
            elif vacancy['salary']['to'] is None:
                salary = vacancy['salary']['from']
            else:
                salary = (int(vacancy['salary']['from']) + int(vacancy['salary']['to'])) // 2
            new_job = {'name': vacancy['name'], 'url': vacancy['url'], 'salary': salary, 'experience': vacancy['experience']['name']}
            vacancies['vacancies'].append(new_job)
        return vacancies

class SJ_API(API):
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
    api_key = os.getenv('J_API')
    # # headers = {"X-Api-App-Id": api_key}
    def __init__(self):

       self.base_url = "https://api.superjob.ru/2.0"

       self.params = {
        'count': 100,
        'id': 1
        }
    #     self.headers = {"X-Api-App-Id": api_key}
    def get_vacancies(self, keyword, count = 10):

        url = f"{self.base_url}/vacancies"
        headers = { "X-Api-App-Id": self.api_key}
        params = { "keyword": keyword, 'count': count,
        # если город не введен поиск ведется по всей России (установлено по умолчанию)
        'id': 1 }
        response = requests.get(url, headers=headers, params=params)
        vacancies = response.json()['objects']
        return vacancies

    def load_areas(self):
        headers = {"X-Api-App-Id": self.api_key}
        result = {}
        response = requests.get(self.SJ_API_URL_AREAS, headers=headers, params={'id_country': 1, 'all': 1})
        response_data = json.loads(response.text)
        for area in response_data['objects']:
            result[area["title"].lower()] = area["id"]

        return result

    def formate_vacancies(self, all_vacancies):
        pass
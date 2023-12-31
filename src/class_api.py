import os

from src.abstract_class import API
import requests
import json

class HH_API(API):
    """Класс для получения вакансий по API c hh.ru"""
    HH_API_URL = 'https://api.hh.ru/vacancies'
    # HH_API_URL_AREAS = 'https://api.hh.ru/areas'

    def __init__(self, keyword):
        self.params = {
            'per_page': 100,
            'text': keyword,
            'area': 1
        }
        self.keyword = keyword
    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.params['per_page']}', {self.params['text']},"
                f" {self.params['area']}')")

    def get_vacancies(self):
        '''Получение вакансий '''
        response = requests.get(self.HH_API_URL, self.params)
        return response.json()


    def formate_vacancies(self, all_vacancies):
        '''приведение списка вакансий к нужному формату '''
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
    """Класс для получения вакансий по API superjob.ru"""
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    #SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
    api_key = os.getenv('J_API')
    headers = {"X-Api-App-Id": api_key}
    def __init__(self, keyword):

       self.base_url = "https://api.superjob.ru/2.0"
       self.SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
       self.prof_name = keyword
       self.params = {
        "keyword": self.prof_name,
        'id': 1,
        'count': 29
        }


    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.params['count']}', {self.params['keyword']},"
                f" {self.params['id']}')")

    def get_vacancies(self):
        """Получение всех вакансий """
        url = f"{self.base_url}/vacancies"
        api_key = os.getenv('J_API')
        headers = {"X-Api-App-Id": api_key}
        response = requests.get( url, params = self.params, headers = headers )

        data = response.json()['objects']
        # -> list vacancies

        # lst = []
        # for row in data:
        #     lst.append(Vacancy(name=row['profession'], url=row['link'],
        #                 salary=row['payment_from'], exp=row['profession']))
        # return lst
        return response.json()



    def formate_vacancies(self, all_vacancies):
        '''приведение списка вакансий к нужному формату '''
        vacancies = {'vacancies': []}
        for vacancy in all_vacancies['objects']:
            if vacancy['payment_from'] is None:
                payment_from = "З/п не указана"
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']['to']
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']['from']
            else:
                salary = (int(vacancy['payment_from']) + int(vacancy['payment_to'])) // 2
            new_job = {'name': vacancy['profession'], 'url': vacancy['client']['link'], 'salary': salary,
                       'experience': vacancy['experience']['title']}
            vacancies['vacancies'].append(new_job)
        return vacancies

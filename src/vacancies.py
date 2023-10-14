import json
from src.class_save import Json_save

class Vacancy:
    '''класс для работы с вакансиями'''
    all = []
    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        if type(salary) == int:
            self.salary = salary
        else:
            self.salary = 0
        self.exp = exp

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.url}',"
                f" {self.salary}, '{self.exp}')")

    def __str__(self):
        return (f"{self.__class__.__name__} Профессия: {self.name}, Адрес объявления: {self.url},"
                f"  Зарплата: {self.salary}, Опыт: {self.exp})")
    def to_dict(self):
        return {
            'title':self.titie,
        }
    @staticmethod
    def instantiate_from_json(file_name='vacancies.json'):
        # with open(file_name, 'r', encoding="utf-8", errors='ignore') as json_file:
        data = Json_save.get_vacancies()
             # data = json.load(json_file)

        for vacancy in data['vacancies']:
            Vacancy.all.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['experience']))
        return Vacancy.all

    @classmethod
    def sort_vacancies(cls):
        """Сортировка вакансий по заработной плате."""
        cls.all.sort(key=lambda vacancy: vacancy.salary, reverse=True)
        return cls.all


    @staticmethod
    def get_top_vacancies(top_n: int, vacancies: list) -> list:
        """Получаем топ-N вакансий из нашего списка."""
        return vacancies[:top_n]

    @staticmethod
    def print_vacancies(for_print: list):
        """Печатает информацию о вакансиях в консоль."""
        count = 1
        for vacancy in for_print:
            # print(vacancy)
            print(
                f'Вакансия №{count}:\nНазвание:{vacancy.name}\nЗарплата:{vacancy.salary} '
                f'рублей\nОпыт работы: {vacancy.exp}\nАдрес объявления: {vacancy.url}\n')
            count += 1
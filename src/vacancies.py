import json


class Vacancy:
    all = []
    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        self.salary = salary
        self.exp = exp

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.url}',"
                f" {self.salary}, '{self.exp}')")

    def instantiate_from_json(self, file_name='vacancies.json'):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)

        for vacancies in data['vacancies']:
            Vacancy.all.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['exp']))
        return Vacancy.all

    def sort_vacancies(self):
        pass

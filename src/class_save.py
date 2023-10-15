import json


class Json_save:

    @staticmethod
    def add_vacancy(vacancies, file_name='vacancies.json'):
        """Добавляет информацию о вакансиях в файл формата json."""
        with open('vacancies.json', 'a', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)
    @staticmethod
    def delete_file(file_name='vacancies.json'):
        with open(file_name, 'w'):
            pass

    @staticmethod
    def get_vacancies(file_name='vacancies.json'):
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def save_vacancies(self, vacancies, file_name='vacancies.json'):
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)

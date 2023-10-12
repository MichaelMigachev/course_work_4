import json


class Json_save:

    def add_vacancy(self, vacancies, file_name='vacancies.json'):
        old_vacancies = self.get_vacancies(file_name='vacancies.json')

        for vac in vacancies:
            old_vacancies.append(vac.to_dict())

        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(old_vacancies, json_file, indent=4, ensure_ascii=False)

    def delete_file(self, file_name='vacancies.json'):
        with open(file_name, 'w'):
            pass

    def get_vacancies(self, file_name='vacancies.json'):
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def save_vacancies(self, vacancies, file_name='vacancies.json'):
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)

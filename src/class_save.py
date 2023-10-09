import json


class Json_save:

    def add_vacancy(self, vacancies, file_name='vacancies.json'):

        with open(file_name, 'a', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, indent=4, ensure_ascii=False)



    def delete_file(self, file_name = 'vacancies.json' ):

         with open(file_name, 'w'):
             pass

    def get_vacancies(self, file_name='vacancies.json'):
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data



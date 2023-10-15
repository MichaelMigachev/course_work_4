from src.class_api import HH_API, SJ_API
from src.vacancies import Vacancy
from pprint import pprint
from src.class_save import Json_save


if __name__ == "__main__":
    print()
    print(f"Программа для сбора информации о вакансиях\n")

    Json_save.delete_file()
    keyword = input(f"Выбери название вакансии, например 'python': ")
    print()
    platform = input(f"Выбери платформу:\n1 - HeadHunter\n2 - SuperJob\n0 - Выйти\n> ")
    print()

    if platform == "1":
        total_view = int(input(f"Сколько вакансий вывести (меньше 100): "))
        print()
        print(f'Вывожу список из {total_view} вакансий отсортированных по зарплате:')
        print()

        hh_api = HH_API(keyword)                        # создаём экземпляр Класса для получения нужной вакансий по API
        all_vacancies = hh_api.get_vacancies()                           # получаем список вакансий с HH
        all_vacancies = hh_api.formate_vacancies(all_vacancies)          # приводим список к нужному формату

        Vacancy.output_final_result(all_vacancies, total_view)           # вывод результата


    elif platform == "2":
        total_view = int(input(f"Сколько вакансий вывести (меньше 100): "))
        print()
        print(f'Вывожу список из {total_view} вакансий отсортированных по зарплате:')
        print()
        sj_api = SJ_API(keyword)                        # создаём экземпляр Класса для получения нужной вакансий по API
        all_vacancies = sj_api.get_vacancies()                           # получаем список вакансий с SJ
        all_vacancies = sj_api.formate_vacancies(all_vacancies)          # приводим список к нужному формату

        Vacancy.output_final_result(all_vacancies, total_view)           # вывод результата

    elif platform == "0":
        print("Пока!")

    else:
        print('В этой программе нет такой платформы')






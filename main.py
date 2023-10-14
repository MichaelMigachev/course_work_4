from src.class_api import HH_API, SJ_API
from src.vacancies import Vacancy
from pprint import pprint
from src.class_save import Json_save


if __name__ == "__main__":
    print(f"Программа для сбора информации о вакансиях\n")

    Json_save.delete_file()
    keyword = input(f"Выбери название вакансии, например 'python': ")
    print()
    platform = input(f"Выбери платформу:\n1 - HeadHunter\n2 - SuperJob\n0 - Выйти\n> ")
    print()

    if platform == "1":
        total_view = int(input(f"Сколько вакансий вывести (меньше 100): "))
        print()

        hh_api = HH_API(keyword)
        all_vacancies = hh_api.get_vacancies()
        all_vacancies = hh_api.formate_vacancies(all_vacancies)
        Json_save.add_vacancy(all_vacancies)
        vacancies = Vacancy.instantiate_from_json()
        numbers_of_vacancies = len(vacancies)
        top_vacancies = Vacancy.get_top_vacancies(top_n=total_view, vacancies=vacancies)

        sort_vacancies = Vacancy.sort_vacancies()
        top_vacancies = Vacancy.get_top_vacancies(top_n=total_view, vacancies=sort_vacancies)

        Vacancy.print_vacancies(top_vacancies)



        # dict = hh_api.formate_vacancies(all_vacancies)
        #
        # # вывод списка вакансий
        # for vacan in dict['vacancies']:
        #     print(f"Профессия: {vacan['name']}, Зарплата: {vacan['salary']}, Опыт: {vacan['experience']},\n"
        #           f"Адрес объявления: {vacan['url']}\n")
        #     total_view -=1
        #     if total_view == 0:
        #         break
        #

        # pprint(hh_api.formate_vacancies(all_vacancies))


    elif platform == "2":
        total_view = int(input(f"Сколько вакансий вывести (меньше 100): "))
        print()
        sj_api = SJ_API(keyword)
        all_vacancies_sj = sj_api.get_vacancies()
        dict = sj_api.formate_vacancies(all_vacancies_sj)
        # pprint(sj_api.formate_vacancies(all_vacancies_sj))
        # вывод списка вакансий
        for vacan in dict['vacancies']:
            print(f"Профессия: {vacan['name']}, Зарплата: {vacan['salary']}, Опыт: {vacan['experience']},\n"
                  f"Адрес объявления: {vacan['url']}\n")
            total_view -= 1
            if total_view == 0:
                break

    elif platform == "0":
        print("Пока!")

    else:
        print('В этой программе нет такой платформы')



# hh_api = HH_API('pytnon')
# all_vacancies = hh_api.get_vacancies()
# vacancies_ = hh_api.formate_vacancies(all_vacancies)
# # pprint(vacancies_)
# # for vacancy in vacancies_['vacancies']:
# #     Vacancy.all.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['experience']))
# # vacancy = Vacancy()
# # for vacancy in Vacancy.all:
# #     print(vacancy)
# # json_save = Json_save()
# Json_save().save_vacancies(vacancies_)
# # Json_save().add_vacancy(vacancies_)
# vacanc = Json_save().get_vacancies()
# Json_save().delete_file()
#
#
# pprint(vacanc)



# hh_api = HH_API('pytnon')
# all_vacancies = hh_api.get_vacancies()
# # pprint(all_vacancies )
# pprint(hh_api.formate_vacancies(all_vacancies))
# pprint(hh_api.load_areas())






# sj_api = SJ_API('pytnon')
# pprint(sj_api.load_areas())
# all_vacancies_sj = sj_api.get_vacancies()
#pprint(all_vacancies_sj)  #'python'
# pprint(sj_api.formate_vacancies(all_vacancies_sj))

# Json_save().save_vacancies(all_vacancies_sj)
#
#
# va = Json_save().get_vacancies()[:5]
# pprint(va)  #'python'
#----------------------------------------------
# print('введите параметры поиска')
#
# keyword = input('Введите ключевое слово вакансию: ')
#
# hh = HH_API(keyword)
# hh_vacancies = hh.formate_vacancies(hh.get_vacancies())
# pprint(hh_vacancies)

# sj = SJ_API(keyword)
# sj_vacancies = sj.formate_vacancies(sj.get_vacancies())
# pprint(sj_vacancies)
#-------------------------------------------------------------

# объединение вакансий в один общий список с двух ресурсов
vacancies = []




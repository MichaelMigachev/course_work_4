from src.class_api import HH_API, SJ_API
from pprint import pprint
from src.class_save import Json_save

if __name__ == "__main__":
    print(f"Программа для сбора информации о вакансиях\n")


    keyword = input(f"Выбери название вакансии, например 'pytnon' \n")
    print()
    platform = input(f"Выбери платформу:\n1 - HeadHunter\n2 - SuperJob\n0 - Выйти\n> ")

    if platform == "1":
        hh_api = HH_API(keyword)
        all_vacancies = hh_api.get_vacancies()
        pprint(hh_api.formate_vacancies(all_vacancies))


    elif platform == "2":
        sj_api = SJ_API(keyword)
        all_vacancies_sj = sj_api.get_vacancies()
        pprint(sj_api.formate_vacancies(all_vacancies_sj))


    else:
        print('В этой программе нет такой платформы')





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




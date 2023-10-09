from src.class_api import HH_API, SJ_API
from pprint import pprint

hh_api = HH_API('pytnon')
all_vacancies = hh_api.get_vacancies()
# print(all_vacancies )
pprint(hh_api.formate_vacancies(all_vacancies))
# pprint(hh_api.load_areas())

# sj_api = SJ_API()
# # pprint(sj_api.load_areas())
# pprint(sj_api.get_vacancies('python'))
#----------------------------------------------
# print('введите параметры поиска')
#
# keyword = input('Введите ключевое слово вакансию: ')
# hh = HH_API(keyword)
# hh_vacancies = hh.formate_vacancies(hh.get_vacancies())
#
# sj = SJ_API(keyword)
# sj_vacancies = sj.formate_vacancies(sj.get_vacancies())
#-------------------------------------------------------------

# объединение вакансий в один общий список с двух ресурсов
vacancies = []




from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    # @abstractmethod
    # def load_areas(self):
    #     pass

    @abstractmethod
    def formate_vacancies(self, all_vacancies):
        pass

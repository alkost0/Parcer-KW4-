from abc import ABC, abstractmethod
import json

class AbstractFileHandler(ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    @abstractmethod
    def add_jobs(self, jobs):
        """
        Метод для добавления вакансий в файл.

        :param jobs: Список вакансий.
        """
        pass

    @abstractmethod
    def get_jobs(self, vacancy):
        """
        Метод для получения данных из файла по указанным критериям.
        :return: Список вакансий.
        """
        pass

    @abstractmethod
    def delete_jobs(self, vacancy):
        """
        Метод для удаления информации о вакансиях.
       """
       pass

class Save_to_Json(AbstractFileHandler):

    def get_jobs(self, vacancies):
        """
        Забираем, незатирая из словаря полученного по api и добавляем новую запись
        """
        data = []
        for vacancy in vacancies:
            vacancy_in_dict = {
                "название": vacancy.title,
                "ссылка": vacancy.link,
                "зарплата": vacancy.salary,
                "описание": vacancy.description,
            }
            data.append(vacancy_in_dict)
        with open("../src/vacancy.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def delete_jobs(self, vacancy):
        with open("../src/vacancy.json", "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            new_vacancies = [vac for vac in vacancies if vacancy not in vac.values()]
        with open("../src/vacancy.json", "w", encoding="utf-8") as file:
            json.dump(new_vacancies, file, ensure_ascii=False, indent=2)

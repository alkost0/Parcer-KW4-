from abc import ABC, abstractmethod
import requests

class AbstractJobSiteAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def connect(self):
        """
        Метод для подключения к API сайта.
        """
        pass

    @abstractmethod
    def get_jobs(self, search_params):
        """
        Метод для получения вакансий с сайта.

        :param search_params: Параметры поиска вакансий.
        :return: Список вакансий.
        """
        pass





class HhRuAPI(AbstractJobSiteAPI):
    """
    Класс для работы с API сайта hh.ru.
    """

    def __init__(self, api_url):
        self.api_url = api_url

    def connect(self):
        """
        Подключение к API сайта hh.ru.
        """
        # Ничего не делаем, так как подключение к API hh.ru прописать отдельно.
        pass

    def get_jobs(self, search_params):
        """
        Получение вакансий с сайта hh.ru.

        :param search_params: Параметры поиска вакансий.
        :return: Список вакансий.
        """
        # Отправляем запрос к API сайта hh.ru и получаем список вакансий.
        response = requests.get(self.api_url, params=search_params)
        jobs = response.json()

        return jobs


from abc import ABC, abstractmethod

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
    def get_jobs(self, search_params):
        """
        Метод для получения данных из файла по указанным критериям.

        :param search_params: Параметры поиска вакансий.
        :return: Список вакансий.
        """
        pass

    @abstractmethod
    def delete_jobs(self, search_params):
        """
        Метод для удаления информации о вакансиях.

        :param search_params: Параметры поиска вакансий.
        """
        pass
from abc import ABC, abstractmethod
import requests
import os

API_KEY = os.getenv("API_KEY_SUPERJOB")

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
    def get_jobs(self, vacancy):
        """
        Метод для получения вакансий с сайта.
        Параметры поиска вакансий.
        :return: Список вакансий.
        """
        pass

class HhRuAPI(AbstractJobSiteAPI):
    """
    Класс для работы с API сайта hh.ru.
    """
    def get_jobs(self, search_params):
        """
        Получение вакансий с сайта hh.ru.
        """
        # Отправляем запрос к API сайта hh.ru и получаем список вакансий.
        def get_jobs(self, vacancy):
            hh_dict = {}
            for page in range(0, 3):
                params = {
                    "text": vacancy,
                    "per_page": 100,
                    "page": page,
                }
                response = requests.get("https://api.hh.ru/vacancies", params=params).json()
                hh_dict.update(response)
            return hh_dict

class SuperJobRuAPI(AbstractJobSiteAPI):
    """
    Класс для работы с API сайта superjob.ru.
    """
    def get_jobs(self, vacancy):
        params = {
            "keyword": vacancy
        }
        headers = {
            'X-Api-App-Id': API_KEY
        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies", params=params, headers=headers).json()
        return response


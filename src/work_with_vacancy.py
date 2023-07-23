class Job:
    """
    Класс для работы с вакансиями.
    """
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.__salary = salary
        self.description = description

    @property
    def salary(self):
        return self.__salary

    def __repr__(self):
        """
        Тут и ниже - различные дандер-методы для работы с зарплатами вакансий
        """
        return f"Job(title='{self.title}', salary='{self.__salary}')"

    def __eq__(self, other):
        return self.__salary == other.__salary
    def __str__(self):
        return f"'название': {self.title}, 'ссылка': {self.link}, 'зарплата': {self.__salary}, 'описание': {self.description}"

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary < other.__salary
        raise ValueError("Сравнивать можно только по зарплате вакансии")

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary <= other.__salary
        raise ValueError("Сравнивать можно только по зарплате вакансии")

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary > other.__salary
        raise ValueError("Сравнивать можно только по зарплате вакансии")

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.__salary >= other.__salary
        raise ValueError("Сравнивать можно только по зарплате вакансии")

    @staticmethod
    def validate_salary(salary):
        """
         Проверка валидности зарплаты.
         """
        if salary is None:
            return 0
        return salary

    @staticmethod
    def validate_description(description):
        """
         Проверка валидности описания вакансии.
         """
        if "<highlighttext>" in description or "</highlighttext>" in description:
            new_description = description.replace("<highlighttext>", "")
            new_description = new_description.replace("</highlighttext>", "")
            return new_description
        return description

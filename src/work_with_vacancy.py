class Job:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f"Job(title='{self.title}', salary='{self.salary}')"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def validate_salary(self):
        """
        Проверка валидности зарплаты.
        """
        # здесь может быть ваш код для проверки валидности данных
        pass

    def validate_link(self):
        """
        Проверка валидности ссылки на вакансию.
        """
        # здесь может быть ваш код для проверки валидности данных
        pass

    def validate_title(self):
        """
        Проверка валидности названия вакансии.
        """
        # здесь может быть ваш код для проверки валидности данных
        pass

    def validate_description(self):
        """
        Проверка валидности описания вакансии.
        """
        # здесь может быть ваш код для проверки валидности данных
        pass
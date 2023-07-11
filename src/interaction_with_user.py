def search_jobs():
    """
    Функция для взаимодействия с пользователем и поиска вакансий.
    """
    # Список поддерживаемых платформ
    platforms = ['HH', 'Superjob']

    # Запрашиваем у пользователя параметры поиска
    platform = input(f"Укажите платформу ({', '.join(platforms)}): ")
    while platform not in platforms:
        platform = input(f"Неверная платформа. Укажите платформу ({', '.join(platforms)}): ")

    query = input("Введите поисковый запрос: ")

    # Создаем объект для работы с соответствующей платформой
    if platform == 'HH':
        scraper = HhScraper()
    elif platform == 'Superjob':
        scraper = SuperjobScraper()

    # Получаем список вакансий
    jobs = scraper.search_jobs(query)

    # Запрашиваем у пользователя, как он хочет отсортировать вакансии
    sort_order = input("Укажите порядок сортировки (asc/desc): ")
    while sort_order not in ['asc', 'desc']:
        sort_order = input("Неверный порядок сортировки. Укажите порядок сортировки (asc/desc): ")

    # Сортируем вакансии по зарплате
    jobs = sorted(jobs, key=lambda job: job.salary, reverse=(sort_order == 'desc'))

    # Запрашиваем у пользователя, сколько вакансий он хочет увидеть
    num_jobs = input("Сколько вакансий вы хотите увидеть? ")
    while not num_jobs.isdigit():
        num_jobs = input("Неверное количество. Сколько вакансий вы хотите увидеть? ")
    num_jobs = int(num_jobs)

    # Выводим топ N вакансий по зарплате
    print(f"Топ {num_jobs} вакансий по зарплате:")
    for job in jobs[:num_jobs]:
        print(job)
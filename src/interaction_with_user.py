from src.main import HhRuAPI, SuperJobRuAPI
from src.save_to_json import Save_to_Json
from src.work_with_vacancy import Job


def get_hh_jobs(hh_data):
    """
    Выборка вакансий из HeadHunter
    """
    vacancies = []
    for hh_vacancy in hh_data:
        try:
            title = hh_vacancy['name']
            link = hh_vacancy['apply_alternate_url']
            salary = hh_vacancy['salary'].get('from')
            if hh_vacancy['snippet']['requirement'] is None:
                description = "Описание не указано"
            else:
                description = hh_vacancy['snippet']['requirement']
        except AttributeError:
            title = hh_vacancy['name']
            link = hh_vacancy['apply_alternate_url']
            salary = None
            if hh_vacancy['snippet']['requirement'] is None:
                description = "Описание не указано"
            else:
                description = hh_vacancy['snippet']['requirement']

        validate_salary = Job.validate_salary(salary)
        validate_description = Job.validate_description(description)
        hh_vacancy_done = Job(title, link, validate_salary, validate_description)
        vacancies.append(hh_vacancy_done)
    return vacancies

def get_superjob_jobs(superjob_data):
    """
    Выборка вакансий из SuperJob
    """
    vacancies = []
    for superjob_vacancy in superjob_data:
        try:
            title = superjob_vacancy['profession']
            link = superjob_vacancy['link']
            salary = superjob_vacancy['payment_from']
            description = superjob_vacancy['candidat']
        except AttributeError:
            title = superjob_vacancy['profession']
            link = superjob_vacancy['link']
            salary = None
            description = superjob_vacancy['candidat']

        validate_salary = Job.validate_salary(salary)
        validate_description = Job.validate_description(description)
        superjob_vacancy_done = Job(title, link, validate_salary, validate_description)
        vacancies.append(superjob_vacancy_done)
    return vacancies

def interaction_with_user(save_json: Save_to_Json):
    """
    Функция взаимодействия с пользователем
    """
    hh_vacancies = HhRuAPI()
    superjob_vacancies = SuperJobRuAPI()

    while True:
        user_input = input("Выберите где ищем вакансии: 1 - HeadHunter, 2 - SuperJob ")
        search_word = input("Введите ключевое слово для поиска: ")
        if user_input == "1":
            hh_data = hh_vacancies.get_jobs(search_word)["items"]
            vacancies = get_hh_jobs(hh_data)
            break
        elif user_input == "2":
            superjob_data = superjob_vacancies.get_jobs(search_word)["objects"]
            vacancies = get_superjob_jobs(superjob_data)
            break
        else:
            print("Неверный ввод! Введите 1 или 2")
    save_json.get_jobs(vacancies)
    while True:
        print('Выберите одно из доступных действий:')
        print('1 - Получить список всех вакансий')
        print('2 - Удалить вакансию')
        print('3 - Получить список вакансий по ключевым словам')
        print('4 - Получить список вакансий с зарплатой выше указанной')
        print('5 - Получить топ N вакансий по зарплате')
        print('6 - Выход')

        choice = input('> ')
        if choice == '1':
            for vacancy in vacancies:
                print(vacancy)
                print()
        elif choice == '2':
            vacancy = input("Введите ссылку удаляемой вакансии: ")
            save_json.delete_jobs(vacancy)
            print('Вакансия удалена!')
        elif choice == '3':
            filter_words = input('Введите ключевые слова для фильтрации вакансий: ')
            for vacancy in vacancies:
                if filter_words in vacancy.description:
                    print(vacancy)
                    print()
        elif choice == '4':
            min_salary = float(input('Введите минимальную зарплату: '))
            for vacancy in vacancies:
                if min_salary < float(vacancy.salary):
                    print(vacancy)
                    print()
        elif choice == '5':
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            sorted_vacancies = sorted(vacancies, reverse=True)
            for vacancy in sorted_vacancies[:top_n]:
                print(vacancy)
                print()
        elif choice == '6':
            break
        else:
            print('Некорректный ввод!')

if __name__ == "__main__":
    save_json = Save_to_Json()
    interaction_with_user(save_json)

class DBManager:
    """
    Класс для работы с базой данных
    """
    # def __init__(self, db_path: str):
    #     self.db_path = db_path
    #     self.db = sqlite3.connect(self.db_path)
    #     self.cursor = self.db.cursor()

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании
        """
        pass

    def all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        pass

    def avg_salary(self):
        """
        получает среднюю зарплату по вакансиям
        """
        pass

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        pass

    def get_vacancies_with_keyword(self):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        """
        pass

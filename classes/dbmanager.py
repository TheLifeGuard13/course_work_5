import typing


class DBManager:
    """
    Класс для работы с базой данных
    """

    def get_companies_and_vacancies_count(self, cur: typing.Any) -> dict:
        """
        получает список всех компаний и количество вакансий у каждой компании
        """
        cur.execute(
            """
        SELECT company_name, COUNT(*) AS vacancies_quantity
        FROM vacancies
        GROUP BY company_name
        ORDER BY vacancies_quantity DESC"""
        )
        rows = cur.fetchall()
        exit_data = {}
        for row in rows:
            exit_data[row[0]] = row[1]
        return exit_data

    def all_vacancies(self, cur: typing.Any) -> list:
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        cur.execute("SELECT company_name, vacancy_name, salary_to, vacancy_url FROM vacancies")
        rows = cur.fetchall()
        exit_data = []
        for row in rows:
            exit_data.append(list(row))
        return exit_data

    def avg_salary(self, cur: typing.Any) -> int:
        """
        получает среднюю зарплату по вакансиям
        """
        cur.execute(f"SELECT AVG(salary_to) FROM vacancies")
        avg_salary = cur.fetchall()
        return int(avg_salary[0][0])

    def get_vacancies_with_higher_salary(self, cur: typing.Any) -> list:
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        cur.execute(
            f"""
        SELECT company_name, vacancy_name, salary_to, vacancy_url FROM vacancies
        WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)"""
        )
        rows = cur.fetchall()
        exit_data = []
        for row in rows:
            exit_data.append(list(row))
        return exit_data

    def get_vacancies_with_keyword(self, cur: typing.Any, word: str) -> list:
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        """
        cur.execute(
            f"""
        SELECT company_name, vacancy_name, salary_to, vacancy_url 
        FROM vacancies
        WHERE vacancy_name LIKE '%{word}%'"""
        )
        rows = cur.fetchall()
        exit_data = []
        for row in rows:
            exit_data.append(list(row))
        return exit_data

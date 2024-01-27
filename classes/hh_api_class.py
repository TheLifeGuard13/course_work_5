import typing

import requests


class HeadHunterAPI:
    """
    Класс для выгрузки данных через API HeadHunter
    """

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies?employer_id="

    def get_companies_vacancies(self, company_id: int) -> typing.Any:
        """
        Получает данные о компании через API HeadHunter
        """
        try:
            company_vacancy = requests.get(f"{self.url}{company_id}", {"per_page": 100}).json()
            return company_vacancy
        except Exception as error:
            raise Exception(f"Ошибка {error}")

import json
import typing

import psycopg2

from config import COMPANIES_JSON_PATH


def get_companies_from_json(json_file: typing.Any = COMPANIES_JSON_PATH) -> list[dict]:
    """Извлекает данные о компаниях из JSON-файла и возвращает список компаний."""
    with open(json_file, encoding="utf-8") as file:
        return json.load(file)


def postgresql_format(input_data: typing.Any) -> list[tuple]:
    """Форматирует данные из списка словарей в список кортежей для PostgreSQL."""
    tupples_list = []
    for vacancy in input_data["items"]:
        company_name = vacancy["employer"]["name"]
        vacancy_name = vacancy["name"]
        vacancy_url = vacancy["alternate_url"]
        if vacancy["salary"]:
            salary_currency = vacancy["salary"]["currency"]
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]
            salary_gross = vacancy["salary"]["gross"]
        else:
            salary_currency = None
            salary_from = None
            salary_to = None
            salary_gross = False
        info = (company_name, vacancy_name, vacancy_url, salary_currency, salary_from, salary_to, salary_gross)
        tupples_list.append(info)
    return tupples_list


def create_database(params: dict, db_name: str) -> None:
    """Создает новую базу данных."""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.commit()
    conn.close()


def create_vacancy_table(cur: typing.Any) -> None:
    """Создает таблицу vacancies."""
    cur.execute(
        """CREATE TABLE vacancies 
    (vacancy_id SERIAL PRIMARY KEY, 
    company_name VARCHAR(100),
    vacancy_name VARCHAR(100),
    vacancy_url VARCHAR(100),
    currency VARCHAR(5),
    salary_from int,
    salary_to int,
    salary_gross bool)"""
    )


def insert_vacancy_data(cur: typing.Any, vacancies: list[tuple]) -> None:
    """Добавляет данные о вакансиях в таблицу vacancies."""
    for vacancy in vacancies:
        cur.execute(
            """INSERT INTO vacancies (company_name, vacancy_name, vacancy_url, currency, salary_from, salary_to, salary_gross) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            vacancy,
        )

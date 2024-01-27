import psycopg2

from classes.hh_api_class import HeadHunterAPI
from config import config
from src.utils import postgresql_format, create_database, create_vacancy_table, \
    get_companies_from_json, insert_vacancy_data


def main():
    vacancies_hh = HeadHunterAPI()

    db_name = "course_work_5"

    params = config()
    conn = None

    create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({"dbname": db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_vacancy_table(cur)
                print("Таблица vacancies успешно создана")

                for company in get_companies_from_json():
                    company_info = vacancies_hh.get_companies_vacancies(company['id'])
                    company_info_sql = postgresql_format(company_info)

                    insert_vacancy_data(cur, company_info_sql)
                    print(f"Данные о {company['name']} в vacancies успешно добавлены")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()

from sqlalchemy import or_
from country_scheme import Country
from connection import create_session, sqliteEngine, postgresEngine


def run_queries_with_sqlite():
    run_queries(create_session(sqliteEngine))


def run_queries_with_postgres():
    run_queries(create_session(postgresEngine))


def print_query_results(data):
    for row in data:
        print(row)


def run_queries(session):
    print("\n======Presentar todos los países del continente americano=========\n")

    query1 = session.query(Country).filter(
        or_(Country.continente == 'SA', Country.continente == 'NA')).all()
    print_query_results(query1)

    print("\n======Presentar los países de Asía, ordenados por el atributo 'Dial'.===========\n")
    query2 = session.query(Country).filter(
        Country.continente == 'AS').order_by(Country.dial).all()
    print_query_results(query2)

    print("\n======Presentar los lenguajes de cada país.===========\n")
    query3 = session.query(
        Country.nombre_pais, Country.lenguajes).all()
    print_query_results(query3)

    print("\n======Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa========\n")
    query4 = session.query(Country).filter(
        Country.continente == 'EU').order_by(Country.capital).all()
    print_query_results(query4)

    print("======Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'=========\n")
    query5 = session.query(Country).filter(
        or_(Country.nombre_pais.like('%uador%'), Country.capital.like('%ito%'))).all()
    print_query_results(query5)

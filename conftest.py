from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_transaction
from loan import Loan


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    loans = [
        Loan(
            loan=10,
            interest_rate=20,
            total=0,
        ),
        Loan(
            loan=10,
            interest_rate=30,
            total=0,
        ),
        Loan(
            loan=10,
            interest_rate=40,
            total=0,
        ),
    ]
    for loan in loans:
        insert_transaction(conn, loan)
    return postgres_container.get_connection_url()

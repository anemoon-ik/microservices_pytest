from sqlalchemy import create_engine
from loan import Loan
from sql_queries import insert_loan, create_table, get_loans, update_loan, complete_loan


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    loan = Loan(
        loan=100,
        interest_rate=20,
        total=0,
    )
    insert_loan(conn, loan)

    loans = get_loans(conn)
    assert len(loans) == 4
    loan = loans[-1]
    assert loan.loan == 100

    update_loan(conn)
    loans = get_loans(conn)
    for loan in loans:
        assert (loan.loan * loan.interest_rate)/10 == loan.total
        assert loan.status == "calculated"

    complete_loan(conn)
    loans = get_loans(conn)
    for loan in loans:
        assert loan.status == "paid"

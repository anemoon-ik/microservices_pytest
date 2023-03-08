from sqlalchemy.engine import Connection
from sqlalchemy import text

from loan import Loan

def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS loans (
        id SERIAL PRIMARY KEY,
        loan INTEGER NOT NULL,
        interest_rate INTEGER NOT NULL,
        total INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'taken'
        )
    """

    conn.execute(text(query))
    conn.commit()



def insert_loan(conn: Connection, loan: Loan):
    query = """
    INSERT INTO loans (loan, interest_rate, total)
    VALUES (:loan, :interest_rate, :total);
    """

    conn.execute(
        text(query),
        parameters={
            "loan": loan.loan,
            "interest_rate": loan.interest_rate,
            "total": loan.total,
        },
    )
    conn.commit()



def update_loan(conn: Connection):
    query = "UPDATE loans SET total=(loan*interest_rate)/10, status='total is calculated' WHERE status='taken';"
    conn.execute(text(query))
    conn.commit()


def complete_loan(conn: Connection):
    query = "UPDATE loans SET status='paid' WHERE status='total is calculated';"
    conn.execute(text(query))
    conn.commit()

def get_loans(conn: Connection) -> list[Loan]:
    query = "SELECT * FROM loans;"
    print("ddd")
    loans = conn.execute(text(query)).fetchall()
    print("ddd1")
    return [Loan(
        id=loan[0],
        loan=loan[1],
        interest_rate=loan[2],
        total=loan[3],
        created=loan[5],
        status=loan[6],
    ) for loan in loans]


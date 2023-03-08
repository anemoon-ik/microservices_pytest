from dataclasses import dataclass
from typing import Optional


@dataclass
class Loan:
    loan: int
    interest_rate: int
    total: int
    created: str = ""
    status: str = "taken"
    id: Optional[int] = None

# - id (int, primary key)
# - loan (integer)
# - interest rate (integer)
# - created (date) default now
# - status (varchar) default "taken"
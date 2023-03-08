Task:
Create a new table: loans, with the following columns:
- id (int, primary key)
- loan (integer)
- interest rate (integer)
- created (date) default now
- status (varchar) default "taken"

Services: 
1. Create a new loan every minute.
1. Reads all debts from the database and calculates the debt with the interest rate, saves it in the total and changes the status to "calculated".
1. Update all loans with the status "calculated" and change the status to "paid".
Instructions:

Inserting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (type, description, amount) VALUES (%s, %s, %s)", (expense.type, 
expense.description, expense.amount))
conn.commit()
```  
    
Selecting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return [{
        "id": expense[0],
        "type": expense[1],
        "description": expense[2],
        "amount": expense[3],
        "created": expense[4]
    } for expense in expenses
    ]
```
"# microservices_pytest" 

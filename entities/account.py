from datetime import datetime
from entities.user import User
from entities.transaction import Transaction
from persistence.db import get_connection
import pymysql
import random

class Account():

    def __init__(self, id: int, number: str, creation_date: datetime, id_user: int, user: User, transactions: list):
        self.id = id
        self.number = number
        self.creation_date = creation_date
        self.id_user = id_user
        self.user = user
        self.transactions = transactions

    def get_account_by_user(id_user: int):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            sql = "SELECT id, number, creation_date, id_user FROM account WHERE id_user = %s"
            cursor.execute(sql, (id_user,))
            rs = cursor.fetchone()

            user = User.get_by_id(rs["id_user"])
            transactions = Transaction.get_transactions_by_account(rs["id"])

            account = Account(
                rs["id"],
                rs["number"],
                rs["creation_date"],
                rs["id_user"],
                user,
                transactions
            )

            return account
        except Exception as ex:
            print(f"Error getting account: {ex}")
            return False
        
    def get_transactions_by_account(id_account: int) -> list:
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SHOW TABLES")
            print("TABLAS EN BD:", cursor.fetchall())

            sql = "SELECT id, description, date, amount, type FROM transaction WHERE id_account = %s ORDER BY date DESC"
            cursor.execute(sql, (id_account,))

            rows = cursor.fetchall()

            return [Transaction(r["id"], r["description"], r["date"], r["amount"], r["type"]) for r in rows]
        except Exception as ex:
            print(f"Error")
            return False
        
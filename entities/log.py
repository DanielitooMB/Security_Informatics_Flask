from datetime import datetime
from entities.user import User
from enums.log_type import LogType
from persistence.db import get_connection

class Log:

    def __init__(self, id: int, date: datetime, user: User, description: str, type: LogType):
        self.id = id
        self.date =date
        self.user = user
        self.description = description
        self.type = type

    def save_log(user: User, description: str, type: LogType) -> bool:
        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = "INSERT INTO user (user, description, type) VALUES (%s, %s, %s)"
            cursor.execute(sql, user, description, type)
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except Exception as ex:
            print(f"Error saving user:{ex}")
            return False
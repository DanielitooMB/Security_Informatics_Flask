import pymysql

from enums.value_permission import ValuePermission
from persistence.db import get_connection

class Permission ():
    def __init__(self, id: int, value: ValuePermission):
        self.id= id
        self.value = value
import os
import random
from sqlite3 import Cursor
from sqlite3.dbapi2 import OperationalError

from config import DATA, KEYS, MAX_INT


def get_and_check_file_exists(filename: str) -> str:
    if os.path.exists(filename):
        return filename
        
    raise ValueError(f"{filename} - Такого файла нет.")


def get_sql_commands_list_from_file(filename: str) -> list:
    if not filename.endswith(".sql"):
        raise ValueError("Ожидался файл с расширением .sql")

    with open(file=filename, mode="r", encoding="utf-8") as sql_file:
        return sql_file.read().split(";")


def execute_sql_command(cur: Cursor, command: str) -> None:
    try:
        cur.execute(command)
    except OperationalError:
        print(f"Не удалось выполнить команду - {command}")


def get_equipment():
    equip = []
    for k in KEYS[:-1]:
        name, records = map(DATA[k].get, ("name", "records"))
        equip.append(name.format(random.randint(1, records)))

    return equip


def generate_params(params_count: int) -> list:
    return [random.randint(1, MAX_INT) for _ in range(params_count)]

from os import name
import sqlite3

from config import DB_FILE_NAME, SQL_FILE_NAME, CONN, CUR
from utils import get_sql_commands_list_from_file, execute_sql_command, get_and_check_file_exists

if __name__ == "__main__":
    with CONN:
        file = get_and_check_file_exists(SQL_FILE_NAME)
        for command in get_sql_commands_list_from_file(file):
            execute_sql_command(CUR, command)

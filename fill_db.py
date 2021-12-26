from sqlite3.dbapi2 import IntegrityError, OperationalError, ProgrammingError

from config import DATA, KEYS, CUR, CONN
from utils import generate_params, get_equipment


if __name__ == "__main__":
    with CONN:
        for k in KEYS:
            table = DATA.get(k)
            need_make_ship = False if k != "Ships" else True

            records, name, params_count, query = map(table.get, tuple(table.keys()))
            values = []
            
            for n in range(1, records + 1):
                item_name = name.format(n)

                if need_make_ship:
                    values.append([item_name] + get_equipment())
                else:
                    values.append([item_name] + generate_params(params_count))

            try:
                CUR.executemany(query, values)
            except (
                ProgrammingError,
                OperationalError,
                IntegrityError
                ) as e:
                print(e.args)
            finally:
                values.clear()
    

import sqlite3


class Database:
    TABLE_NAME = 'excel_data'

    def __init__(self) -> None:
        self.con = sqlite3.connect('file::memory:')
        self._create_db()

    def _create_db(self) -> None:
        with self.con as con:
            sql = f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                value INTEGER NOT NULL,
                date STRING,
                data_type STRING,
                company STRING,
                timing STRING
            );
            """
            con.execute(sql)

    def save(self, data: list[tuple]) -> None:
        query = []
        for row in data:
            query.append(f"('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}')")

        query_string = f"INSERT INTO {self.TABLE_NAME} ('value', 'date', 'data_type', 'company', 'timing') VALUES " + ", ".join(
            query) + ";"

        with self.con as con:
            con.execute(query_string)

    def get_total(self) -> list[dict]:
        with self.con as con:
            sql = f'SELECT date, timing, SUM(value) from {self.TABLE_NAME} group by date, timing;'
            res = con.execute(sql)
            total = [i for i in res]

        return total

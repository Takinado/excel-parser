import sys
from pathlib import Path

from database import Database
from datasource import DataSource

BASE_DIR = Path(__file__).resolve(strict=True).parent


class ExcelApp:

    def __init__(self, data_source, database):
        self.data_source = data_source
        self.database = database

    def save_to_db(self, file_name: Path) -> list[tuple]:
        data = self.data_source.read(file_name)
        self.database.save(data)
        return data

    def calculate(self) -> list[tuple]:
        total_result = self.database.get_total()
        return total_result

    def print_total(self, total_result: list[tuple]) -> None:
        print('Рассчетный результат:')
        for row in total_result:
            print(f'Тотал{" прогнозируемый" if row[1] == "forecast" else ""} {row[0]} = {row[2]}')


def data_flow(file: str) -> None:
    app = ExcelApp(data_source=DataSource(), database=Database())
    file_name = Path(BASE_DIR).joinpath(file)
    app.save_to_db(file_name)
    app.print_total(app.calculate())


if __name__ == '__main__':
    data_flow(sys.argv[1])

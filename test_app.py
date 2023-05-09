import datetime
from pathlib import Path

from database import Database
from datasource import DataSource
from main import ExcelApp

BASE_DIR = Path(__file__).resolve(strict=True).parent

file_name = Path(BASE_DIR).joinpath('Приложение_к_заданию_бек_разработчика.xlsx')


def test_read_value():
    app = ExcelApp(DataSource(), Database())
    for data in app.save_to_db(file_name):
        # (value, date, data_type, company, timing)
        assert isinstance(data[0], int)


def test_read_date():
    app = ExcelApp(DataSource(), Database())
    for data in app.save_to_db(file_name):
        assert isinstance(data[1], datetime.date)


def test_read_count():
    app = ExcelApp(DataSource(), Database())
    data = app.save_to_db(file_name)

    assert len(data) == 160


def test_calculate_total():
    app = ExcelApp(DataSource(), Database())
    app.save_to_db(file_name)
    total = app.calculate()
    assert total == [
        ('2023-05-01', 'fact', 1180),
        ('2023-05-01', 'forecast', 1680),
        ('2023-05-02', 'fact', 1580),
        ('2023-05-02', 'forecast', 2080),
    ]

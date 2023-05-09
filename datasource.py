import datetime

from openpyxl.reader.excel import load_workbook


class DataSource:
    def read(self, file_name):

        wb = load_workbook(file_name)
        sheet = wb.worksheets[0]
        parsed_data: list = []
        for row in range(4, sheet.max_row + 1):
            for column in range(3, 11):
                value = sheet.cell(row, column).value
                date = sheet.cell(3, column).value
                data_type = sheet.cell(row=2, column=column if column % 2 != 0 else column - 1).value
                company = sheet.cell(row, 2).value
                timing = sheet.cell(row=1, column=3 if column in range(3, 7) else 7).value
                data_row = (
                    value,
                    datetime.datetime.today().replace(
                        day=1).date() if date == 'data1' else datetime.datetime.today().replace(day=2).date(),
                    data_type,
                    company,
                    timing,
                )
                parsed_data.append(data_row)
        return parsed_data

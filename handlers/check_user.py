import gspread

from sheets.google_sheets import sheet


def check_user_in_sheet(user_id):
    try:
        cell = sheet.find(str(user_id))
        if cell:
            return sheet.cell(cell.row, 3).value  # Возвращает существующий код
    except gspread.exceptions.CellNotFound:
        return None
    return None
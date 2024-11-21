import gspread
from sheets.google_sheets import sheet


def add_user_to_sheet(user_id, username, code):
    sheet.append_row([user_id, username, code])

def get_user_code(user_id):
    try:
        cell = sheet.find(str(user_id))
        if cell:
            return sheet.cell(cell.row, 3).value
    except gspread.exceptions.CellNotFound:
        return None
    return None

# Функция добавления пользователя в таблицу
def add_user(user_id, username, code):
    sheet.append_row([user_id, username, code])
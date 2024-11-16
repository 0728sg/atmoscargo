from sheets.google_sheets import sheet


def add_user_to_sheet(user_id, username, code):
    sheet.append_row([user_id, username, code])
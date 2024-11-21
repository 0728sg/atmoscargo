import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import CREDENTIALS_FILE, GOOGLE_SHEET_NAME


# Настройки Google Sheets
SCOPE = ['https://docs.google.com/spreadsheets/d/16peTXU4MyS3qiM0yH_dMXqw8mKDx2j5BQfg_oG1nhRc/edit']
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
gc = gspread.authorize(CREDENTIALS)
sheet = gc.open('Client Codes').sheet1
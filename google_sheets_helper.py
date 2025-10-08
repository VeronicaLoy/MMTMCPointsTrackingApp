import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Replace with your downloaded credentials file name
CREDENTIALS_FILE = ".streamlit/secrets.toml"#"google-credentials.json"

SHEET_ID = "1rA8elO0f7gjkA1IoNgsDb62Sq5_wAR5gVyqvDjDS1oA"


def get_sheet(sheet_name: str):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).worksheet(sheet_name)
    return sheet

def read_points(sheet_name: str):
    sheet = get_sheet(sheet_name)
    data = sheet.get_all_records()
    return data

def write_points(sheet_name: str, data):
    sheet = get_sheet(sheet_name)
    if hasattr(data, "values"):
        rows = data.values.tolist()
        # Optionally, add column headers if needed
        # sheet.append_row(list(data.columns))
    else:
        # If data is a list of dicts
        rows = [list(row.values()) for row in data]
    sheet.append_rows(rows)
    
    # sheet.append_rows(rows)
    # sheet.clear()
    # sheet.append(row(data))
    # sheet.append_row(list(data[0].keys()))
    # for row in data:
    #     sheet.append_row(list(row.values()))

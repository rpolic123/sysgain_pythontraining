import pandas as pd

excel_file = 'data.xlsx'
sheets = pd.ExcelFile(excel_file).sheet_names
for sheet in sheets:
    df = pd.read_excel(excel_file, sheet_name=sheet)
    df.to_csv(f"{sheet}.csv", index=False)
    print(f"Saved {sheet}.csv")
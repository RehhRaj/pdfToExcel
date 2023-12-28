import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_path, excel_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text()

    # Convert text to a pandas DataFrame
    df = pd.DataFrame([line.split('\n') for line in all_text.split('\n')])

    # Save DataFrame to Excel
    df.to_excel(excel_path, index=False)

def pdf_to_json(pdf_path, json_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text()

    # Convert text to a list of dictionaries
    data = [dict(zip(range(len(line.split('\n'))), line.split('\n'))) for line in all_text.split('\n')]

    # Save list of dictionaries to JSON
    with open(json_path, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

# Example usage
pdf_path = '2352798454.pdf'
excel_path = 'output.xlsx'
json_path = 'output.json'

pdf_to_excel(pdf_path, excel_path)
pdf_to_json(pdf_path, json_path)

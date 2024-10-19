import PyPDF2

def extract_headers(page_content):
    """Extract key headers from the page content."""
    headers = {}
    if "Invoice Date" in page_content:
        headers["Invoice Date"] = extract_specific_value(page_content, "Invoice Date")
    if "Invoice No" in page_content:
        headers["Invoice Number"] = extract_specific_value(page_content, "Invoice No")
    if "Vendor Name" in page_content:
        headers["Vendor Name"] = extract_specific_value(page_content, "Vendor Name")
    return headers

def extract_specific_value(content, label):
    """Extract the specific value associated with a given label."""
    start = content.find(label) + len(label) + 1  
    end = content.find('\n', start)  
    return content[start:end].strip() if end != -1 else content[start:].strip()

def extract_table(page_content):
    """Extract table data from the page content."""
    lines = page_content.split('\n')
    table_data = []
    for line in lines:
        if line.strip() and any(char.isdigit() for char in line):  
            table_data.append(line.strip().split())  
    return table_data

def extract_data_from_multiple_pages(pdf_path):
    """Extract data from multiple pages of the PDF."""
    extracted_data = []

    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_content = page.extract_text()
                headers = extract_headers(page_content)
                table_data = extract_table(page_content)
                extracted_data.append({"headers": headers, "table_data": table_data})
    except Exception as e:
        print(f"Error while processing PDF: {e}")

    return extracted_data

if __name__ == "__main__":
    pdf_path = '/media/prakash/dbc0ca7e-9552-4df3-a3a5-9b9f0c8a0f6f/project/sample-invoice.pdf'
    extracted_data = extract_data_from_multiple_pages(pdf_path)
    print(extracted_data)


# deep-logic-ai


# PDF Data Extraction Project

## Overview

This project is designed to extract structured data, such as headers and table information, from PDF files (invoices or receipts). The extracted data includes details like invoice date, invoice number, vendor name, and table entries for line items, quantities, and prices. The project is built using Python and the `PyPDF2` library.

## Features

- **Header Extraction**: Extracts key headers like "Invoice Date", "Invoice Number", and "Vendor Name".
- **Table Data Extraction**: Extracts table data including item details, quantities, and prices.
- **Multi-page Support**: Processes multiple pages in PDF files.
- **Error Handling**: Basic error handling for cases like missing fields or malformed data.

## Thought Process

1. **PDF Structure Understanding**:
   - Identified key data elements from invoices, which include headers (e.g., Invoice Date) and tabular data (e.g., itemized details).
   - Planned to extract headers as key-value pairs and table data as a list of rows.

2. **Header Extraction Logic**:
   - Used specific keyword labels (e.g., "Invoice Date", "Invoice No") to find and extract values following the label in the page content.
   - Implemented the `extract_headers` function to capture this information.

3. **Table Data Extraction**:
   - Assumed that rows in the table would contain numerical data (e.g., quantities or prices) and split the text content based on this assumption.
   - Implemented the `extract_table` function, which scans for rows with numeric data and splits them by whitespace.

4. **Multi-page Support**:
   - The solution processes each page individually, extracting headers and table data from each page.

## Assumptions

- **Consistent Labels**: Assumed that the labels "Invoice Date", "Invoice No", and "Vendor Name" would be present and consistent across different invoice formats.
- **Tabular Structure**: Assumed that table rows are single lines containing numerical data, making it easier to identify and extract rows.
- **Page Structure**: Assumed that each page follows the same structure with headers followed by tables.
  
## How to Run

### Prerequisites

- Python 3.x installed on your system
- Install `PyPDF2` by running the following command:

    ```bash
    pip install PyPDF2
    ```

### Running the Script

1. Clone the repository or download the script.
   
2. Place the PDF file (e.g., `sample-invoice.pdf`) in the same directory as the script.

3. Open the script file, and modify the `pdf_path` variable to point to your PDF file:

    ```python
    pdf_path = 'path/to/your/sample-invoice.pdf'
    ```

4. Run the script using the following command:

    ```bash
    python pdf_extractor.py
    ```

### Output

- The script will output extracted data to the console, including headers and table information.
- Example output:

    ```json
    [
        {
            "headers": {
                "Invoice Date": "2024-10-01",
                "Invoice Number": "123456",
                "Vendor Name": "Acme Corp"
            },
            "table_data": [
                ["Item1", "2", "$50"],
                ["Item2", "1", "$30"]
            ]
        }
    ]
    ```

## Project Structure

```plaintext
pdf_extractor.py        # Main script file
README.md               # Documentation for the project
sample-invoice.pdf      # Sample PDF to test the script

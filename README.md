# Subscription Pricing Calculator

This repository contains a web application built using Streamlit. The application allows users to upload CSV files, display data with pagination, and calculate subscription pricing based on the uploaded data. The application is designed to handle large datasets efficiently and provide real-time feedback during uploads.

## Features

- **CSV Upload Service:**
  - Users can upload CSV files.
  - Real-time progress indicators to keep users informed during uploads.
  
- **Data Display and Pagination:**
  - Display uploaded data in a tabular format.
  - Implement pagination for smooth navigation through large datasets.
  - Ensure the UI remains responsive even with extensive data.
  
- **Subscription Pricing Calculator:**
  - Calculate and display subscription pricing based on the uploaded data.
  - The subscription pricing formula is:  
    `SubscriptionPrice = BasePrice + (PricePerCreditLine * CreditLines) + (PricePerCreditScorePoint * CreditScore)`

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas

### Install Dependencies

Clone the repository and install the required dependencies:

### Running the Application

Run the Streamlit application using the following command:

streamlit run app.py

This will start a local web server, and you can access the application in your web browser at http://localhost:8501.

## Usage
1. Upload CSV File:

- Click on the "Browse files" button to upload your CSV file.
- The application will display a progress bar indicating the upload status.
- View Data with Pagination:

2. After the upload is complete, the data will be displayed in a table.
   
- Use the pagination controls to navigate through the data.
- Select the number of rows per page from the dropdown menu.
  
3. Calculate Subscription Prices:

- Enter the base price, price per credit line, and price per credit score point in the input fields.
- Click on the "Calculate Subscription Prices" button.
- The calculated subscription prices will be displayed in the table.
  
## Subscription Pricing Formula
To calculate the subscription pricing based on credit score and the number of credit lines mentioned in the CSV, use the following formula:

- CreditScore: The credit score obtained from the CSV data.
- CreditLines: The number of credit lines mentioned in the CSV.
- BasePrice: The base price for the subscription.
- PricePerCreditLine: The additional price per credit line.
- PricePerCreditScorePoint: The additional price per credit score point.
  
Formula:
SubscriptionPrice = BasePrice + (PricePerCreditLine * CreditLines) + (PricePerCreditScorePoint * CreditScore)

## Code Explanation
The main application code is located in app.py. Here's a brief overview of the code structure:

- File Upload:
  - Users can upload a CSV file using st.file_uploader.
  - The uploaded CSV file is read into a Pandas DataFrame.
    
- Data Display with Pagination:
  - The data is displayed in a paginated table.
  - Pagination controls are implemented to navigate through the data.
    
- Subscription Pricing Calculator:
  - Input fields for base price, price per credit line, and price per credit score point.
  - A button to calculate the subscription prices using the provided formula.
  - The calculated prices are displayed in the table.

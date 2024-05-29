# CSV Upload and Subscription Pricing Calculator

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

```bash
git clone https://github.com/Harshita781/Supersix-project.git
cd Supersix-project
pip install -r requirements.txt

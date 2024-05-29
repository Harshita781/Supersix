import streamlit as st
import pandas as pd

# Function to calculate subscription price
def calculate_subscription_price(row, base_price, price_per_credit_line, price_per_credit_score_point):
    return base_price + (price_per_credit_line * row['CreditLines']) + (price_per_credit_score_point * row['CreditScore'])

# Streamlit App
def main():
    st.title("Subscription Pricing Calculator")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Display progress indicator
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        # Load CSV data
        data = pd.read_csv(uploaded_file)
        data.columns = data.columns.str.strip()  # Remove any leading/trailing spaces from column names
        
        required_columns = {'CreditScore', 'CreditLines'}
        if not required_columns.issubset(data.columns):
            st.error(f"CSV file must contain the following columns: {', '.join(required_columns)}")
            return
        
        progress_bar.progress(50)
        progress_text.text("CSV file uploaded successfully.")
        
        # Display Data with Pagination
        st.subheader("Uploaded Data")
        
        # Set up pagination
        page_size = st.selectbox("Rows per page", [5, 10, 20, 50, 100], index=1)
        page_number = st.number_input("Page number", min_value=1, value=1, step=1)
        
        total_rows = data.shape[0]
        total_pages = (total_rows // page_size) + (total_rows % page_size > 0)
        
        if page_number > total_pages:
            st.warning(f"Page number exceeds total pages ({total_pages}). Showing last page.")
            page_number = total_pages
        
        start_row = (page_number - 1) * page_size
        end_row = start_row + page_size
        paginated_data = data.iloc[start_row:end_row]
        
        st.write(paginated_data)
        
        # Display progress completion
        progress_bar.progress(100)
        progress_text.text("Data displayed with pagination.")
        
        # Subscription Pricing Calculator
        st.subheader("Subscription Pricing Calculator")
        
        base_price = st.number_input("Base Price", min_value=0.0, value=10.0, step=0.1)
        price_per_credit_line = st.number_input("Price per Credit Line", min_value=0.0, value=1.0, step=0.1)
        price_per_credit_score_point = st.number_input("Price per Credit Score Point", min_value=0.0, value=0.1, step=0.01)
        
        if st.button("Calculate Subscription Prices"):
            data['SubscriptionPrice'] = data.apply(
                lambda row: calculate_subscription_price(row, base_price, price_per_credit_line, price_per_credit_score_point),
                axis=1
            )
            st.write(data[['CreditScore', 'CreditLines', 'SubscriptionPrice']])
        
if __name__ == "__main__":
    main()

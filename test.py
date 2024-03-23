import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Sample data for the table (list of dictionaries)
    data = [
        {"Name": "John", "Age": 30, "Country": "USA"},
        {"Name": "Alice", "Age": 25, "Country": "UK"},
        {"Name": "Bob", "Age": 35, "Country": "Canada"}
    ]

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame as a table
    st.write(df)

if __name__ == "__main__":
    main()

import streamlit as st
import sqlite3

# Function to create database table
def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, email):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# Function to retrieve data from the database
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return data

# Main function for Streamlit app
def main():
    st.title('SQLite3 Web App')

    # Create database table if not exists
    create_table()

    # Sidebar for adding users
    st.sidebar.header('Add New User')
    name = st.sidebar.text_input('Name')
    email = st.sidebar.text_input('Email')
    if st.sidebar.button('Add User'):
        insert_data(name, email)
        st.success('User added successfully!')

    # Display all users
    st.header('All Users')
    users = get_data()
    for user in users:
        st.write(f'Name: {user[1]}, Email: {user[2]}')

if __name__ == '__main__':
    main()

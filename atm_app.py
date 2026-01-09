import streamlit as st

st.title("Simple ATM System")

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 500000
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# PIN check
pin = st.text_input("Enter your 4-digit PIN", type="password")
if st.button("Login"):
    if pin == "1234":
        st.success("Login Successful!")
        st.session_state.logged_in = True
    else:
        st.error("Incorrect PIN!")

if st.session_state.get('logged_in', False):
    st.subheader("ATM Operations")

    # Check Balance
    if st.button("Check Balance"):
        st.info(f"Your balance is: ${st.session_state.balance}")

    # Deposit Money
    deposit_amount = st.number_input("Deposit Amount", min_value=0)
    if st.button("Deposit"):
        st.session_state.balance += deposit_amount
        st.session_state.transactions.append(f"Deposited: ${deposit_amount}")
        st.success(f"Deposited ${deposit_amount}. New balance: ${st.session_state.balance}")

    # Withdraw Money
    withdraw_amount = st.number_input("Withdraw Amount", min_value=0)
    if st.button("Withdraw"):
        if withdraw_amount > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= withdraw_amount
            st.session_state.transactions.append(f"Withdrawn: ${withdraw_amount}")
            st.success(f"Withdrawn ${withdraw_amount}. New balance: ${st.session_state.balance}")

    # View Transactions
    if st.button("View Transactions"):
        if len(st.session_state.transactions) == 0:
            st.info("No transactions yet.")
        else:
            st.write("**Transactions:**")
            for t in st.session_state.transactions:
                st.write(t)

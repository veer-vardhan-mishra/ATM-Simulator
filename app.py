import streamlit as st
from atm_logic import get_balance, credit, debit, mini_statement

st.set_page_config(page_title="ATM Machine", page_icon="🏦")

# ---------- ALWAYS CREATE KEYS ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "exited" not in st.session_state:
    st.session_state.exited = False


st.title("🏦 ATM Machine")


# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in and not st.session_state.exited:

    pin = st.text_input("Enter your 4-digit PIN:", type="password")

    if st.button("Login"):
        if pin == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()   # <<< HERE
        else:
            st.error("Wrong PIN. Try again.")


# ---------- EXIT PAGE ----------
elif st.session_state.exited:
    st.success("You have exited the ATM. See you again 👋")

    if st.button("Login Again"):
        st.session_state.exited = False
        st.rerun()


# ---------- ATM MENU ----------
elif st.session_state.logged_in:

    st.subheader("Select an Option")

    option = st.radio(
        "Menu",
        ["Balance", "Credit (Deposit)", "Debit (Withdraw)", "Mini Statement", "Exit"]
    )

    # --- Balance ---
    if option == "Balance":
        st.info(f"💰 Current Balance: ₹{get_balance():.2f}")

    # --- Deposit ---
    elif option == "Credit (Deposit)":
        amt = st.number_input("Enter amount to deposit", min_value=1.0, step=1.0)
        if st.button("Deposit"):
            new_bal = credit(amt)
            st.success(f"₹{amt:.2f} deposited successfully")
            st.info(f"New Balance: ₹{new_bal:.2f}")

    # --- Withdraw ---
    elif option == "Debit (Withdraw)":
        amt = st.number_input("Enter amount to withdraw", min_value=1.0, step=1.0)
        if st.button("Withdraw"):
            result = debit(amt)
            if result is None:
                st.error("❌ Insufficient balance")
            else:
                st.success(f"₹{amt:.2f} withdrawn successfully")
                st.info(f"New Balance: ₹{result:.2f}")

    # --- Mini Statement ---
    elif option == "Mini Statement":
        ms = mini_statement()
        if ms is None:
            st.info("No transactions yet.")
        else:
            st.table(ms)

    # --- Exit ---
    elif option == "Exit":
        st.session_state.exited = True
        st.session_state.logged_in = False
        st.rerun()

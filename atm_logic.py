# atm_logic.py
import pandas as pd
from datetime import datetime as dt
import os

CSV_FILE = "transactions.csv"

# ---------- Load existing data if available ----------
if os.path.exists(CSV_FILE):
    transactions = pd.read_csv(CSV_FILE)

    # Restore last balance from CSV
    if not transactions.empty and "balance" in transactions.columns:
        balance = float(transactions.iloc[-1]["balance"])
    else:
        balance = 1000
else:
    transactions = pd.DataFrame(columns=["date", "amount", "type", "balance"])
    balance = 1000


# ---------- Append only (do not overwrite) ----------
def append_transaction(row):
    file_exists = os.path.exists(CSV_FILE)

    pd.DataFrame([row]).to_csv(
        CSV_FILE,
        mode="a",
        index=False,
        header=not file_exists  # header only first time
    )


def get_balance():
    return balance


def credit(amount):
    global balance
    balance += float(amount)

    row = {
        "date": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": float(amount),
        "type": "credit",
        "balance": balance
    }

    append_transaction(row)
    return balance


def debit(amount):
    global balance
    amount = float(amount)

    if amount > balance:
        return None

    balance -= amount

    row = {
        "date": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": -amount,
        "type": "debit",
        "balance": balance
    }

    append_transaction(row)
    return balance


def mini_statement():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            return None
        return df.tail(5)
    return None

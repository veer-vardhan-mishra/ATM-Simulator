ATM Simulator — Streamlit App

This is a simple ATM Simulator Web App built using Python + Streamlit.

It allows a user to:

- Login using a PIN
- Check account balance
- Deposit (Credit) money
- Withdraw (Debit) money
- View a Mini Statement (last 5 transactions)
- Save transactions permanently in a CSV file

All ATM logic is stored in a separate backend file so the UI and logic stay independent.


PROJECT STRUCTURE

ATM-Simulator/
app.py              -> Streamlit Frontend UI
atm_logic.py        -> Backend ATM functions
transactions.csv    -> Stores all transactions (auto-created)
requirements.txt
README.txt


FEATURES

Secure PIN Login
Only users with the correct PIN can access the ATM.

Balance Enquiry
Displays the current account balance.

Deposit (Credit)
Adds money to account and records it in the CSV file.

Withdraw (Debit)
Withdraws money safely and prevents overdraft.

Mini Statement
Shows the latest 5 transactions.

Permanent Storage
All transactions are stored inside transactions.csv and are not erased when the app restarts.


HOW TO RUN THE APP

1. Install Python (if not installed)
Download from: https://python.org


2. (Optional) Create Virtual Environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate


3. Install Required Libraries

pip install -r requirements.txt


4. Run the App

streamlit run app.py


5. Open in Browser

If the browser does not open automatically, go to:

http://localhost:8501


DEFAULT PIN

1234

(You can change it in app.py)


TRANSACTION STORAGE

Transactions are saved in:

transactions.csv

Each entry includes:

date & time
amount
type
balance

So your data is safely stored even after restarting.


BUILT USING

Python 3
Streamlit
Pandas
CSV File Storage


FUTURE IMPROVEMENTS

Multiple user accounts
Change PIN option
UI theme upgrade
Export full statement


CONTRIBUTING

Pull requests and improvements are welcome.


LICENSE

This project is free to use for learning and personal development.

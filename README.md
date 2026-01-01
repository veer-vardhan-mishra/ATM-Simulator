🏦 ATM Simulator — Streamlit Web App

A full-stack ATM Simulator built using Python + Streamlit that lets users securely log in using a PIN, manage a virtual bank balance, and perform real-world ATM operations — all inside a clean, interactive web interface.

This project focuses on end-to-end app development — combining authentication, validation, UI interaction, permanent transaction storage, and real-time balance updates.

📌 Overview

This project allows users to:

🔐 Securely log in using a PIN
💰 Check account balance
➕ Deposit (Credit) money
➖ Withdraw (Debit) money
📜 View a Mini-Statement (last 5 transactions)
💾 Store every transaction permanently in a CSV file

The goal is to simulate a real ATM experience while demonstrating frontend + backend separation using Streamlit and Python.

🧠 System Architecture
User Input (PIN / Amount)
        ↓
Authentication & Validation
        ↓
Transaction Logic
(Credit / Debit / Balance Check)
        ↓
Balance & CSV Storage Update
        ↓
Streamlit UI Refresh


Your balance is updated instantly — and every transaction is logged safely into a CSV file that persists across sessions.

🖥️ Live UI Experience

The app includes:

✔ Real-time balance updates
✔ Color-coded alerts (success / errors)
✔ Clean input forms
✔ Simple ATM-style interface

Beginner-friendly, yet professional.

🧩 Features
🔐 PIN-Based Login Authentication

Only valid users gain access.

💳 Balance Enquiry

Instantly view your current account balance.

💵 Deposit & Withdraw

Supports safe transactions with validation.

🚨 Smart Validation

Prevents overdrafts
Blocks invalid / negative inputs
Shows clear feedback messages

💾 Permanent Storage

Every transaction is saved to:

transactions.csv


So your history never resets when you restart the app.

📜 Mini-Statement

View your latest 5 transactions anytime.

🛠 Tech Stack

🐍 Python
🌐 Streamlit — UI Framework
📊 Pandas — Data Handling
📂 CSV — Transaction Storage

📂 Project Structure
ATM-Simulator/
├── app.py               # Streamlit frontend UI
├── atm_logic.py         # Backend logic & CSV storage
├── transactions.csv     # Auto-created transaction log
├── requirements.txt     # Dependencies
└── README.md            # Documentation

▶️ How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start the Web App
streamlit run app.py

3️⃣ Open in Browser

If not auto-opened, visit:

http://localhost:8501

🔐 Authentication Model

Users log in using a 4-digit PIN
(Default PIN → 1234, configurable in app.py)

Once authenticated, ATM functions unlock.

💵 Transaction Logic
➕ Deposit

✔ Adds money
✔ Saves transaction
✔ Updates balance instantly

➖ Withdraw

✔ Withdraws only if sufficient funds
✔ Prevents negative or invalid values
✔ Displays alerts for failed attempts

🔍 Output & User Feedback
Action	App Response
Valid login	✅ Success message
Wrong PIN	❌ Error alert
Deposit success	💚 Balance updated
Withdrawal success	💸 New balance displayed
Insufficient funds	🔴 Warning
Invalid entry	⚠️ Input validation alert
📊 Optional Dashboard Enhancements (Future-Ready)

✨ Full transaction history viewer
✨ Charts for spending & deposits
✨ Account insights
✨ Export statements

Great for school projects and portfolios 🎒💻

🚧 Planned Improvements

🧑‍🤝‍🧑 Multi-user support
🗃 SQLite / Firebase storage
📱 Mobile-responsive UI
🔒 Secure hashed PINs
📜 Downloadable statements
📊 Analytics dashboard
☁ Deployment to Streamlit Cloud / Render

📌 Important Note

⚠ This is an educational project — not a real banking system.
Please do NOT use real bank credentials.

🤝 Contributing

Pull requests and suggestions are always welcome!
Feel free to open an issue or submit improvements 🚀

📄 License

This project is open-source and free for learning & development.

📧 Contact

Have questions or ideas?
Open an issue on GitHub — happy to help 😊

Built with ❤️ to simulate banking safely and learn full-stack development.

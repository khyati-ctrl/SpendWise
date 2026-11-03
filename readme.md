# SpendWise – Student Expense Tracker

SpendWise is a Python-based GUI application designed to help students track and understand their daily expenses. It provides a simple, organized interface to view spending, manage a monthly budget, and explore category-wise expense summaries.

The application is built using **CustomTkinter** and **Matplotlib**, with a clean and user-friendly interface.

## Features

- **Dashboard:** Displays an overview of monthly budget, total spending, remaining budget, and average daily spending.
- **Add Expense:** Provides a form to enter expense details such as amount, category, date, and description.
- **Transactions:** Displays a table of recent expenses.
- **Analytics:** Shows category-wise spending through visual charts.
- **Budget Overview:** Displays monthly budget progress.
- **Spending Insights:** Includes sample insights to demonstrate how spending patterns can be presented.

## Expense Categories

The application uses the following categories:

- Food
- Transport
- Academics
- Shopping
- Entertainment
- Snacks
- Social
- Others

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CustomTkinter | GUI development |
| Matplotlib | Data visualization |
| Tkinter | GUI components |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-link>
```

### 2. Navigate to the Project Folder

```bash
cd SpendWise
```

### 3. Install Dependencies

```bash
pip install customtkinter matplotlib
```

### 4. Run the Application

```bash
python main_updated.py
```

If you rename the file to `main.py`, run:

```bash
python main.py
```

## Project Structure

```text
SpendWise/
│
├── main_updated.py
├── README.md
└── requirements.txt
```

## User Interface

SpendWise uses a clean light-themed interface with a dark teal sidebar, organized dashboard cards, and visual spending summaries.

The application includes the following sections:

1. Dashboard
2. Add Expense
3. Transactions
4. Analytics

## Current Development Status

The current version focuses on the **Graphical User Interface (GUI)** and demonstrates the layout and navigation of the application.

The displayed transactions, budget values, charts, and insights currently use sample data. Expense storage, automatic calculations, and database integration are not implemented yet.

## Future Enhancements

- Integrate SQLite for permanent expense storage.
- Implement actual Add, Edit, and Delete expense operations.
- Calculate total and category-wise spending automatically.
- Add monthly budget alerts at 80% and 100%.
- Implement search and filtering options.
- Generate monthly expense reports.
- Enable CSV export.
- Generate personalized spending insights using transaction data.

## Objective

The main objective of SpendWise is to provide students with a simple and convenient way to monitor their expenses, understand their spending habits, and become more aware of their monthly budgets.

---

**SpendWise – Track Your Spending. Stay on Budget.**
# Codomax AI & ML Internship — Module 2

## Python Mini Project — Smart Expense Tracker

This repository contains my work for **Module 2 of the Codomax AI & ML Internship**.

The project is a beginner-friendly command-line application developed using Python. It allows users to add, view, analyze, and delete personal expenses.

---

## Project Objective

The objective of this project is to apply fundamental Python programming concepts to build a practical mini project.

The project demonstrates:

- Variables
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input
- Exception handling
- Calculations
- Basic data processing

---

## Project Features

### 1. Add Expense

Users can enter:

- Expense category
- Expense description
- Expense amount

The application automatically records the current date.

### 2. View Expenses

Displays all recorded expenses in a structured format.

### 3. View Total

Calculates and displays the total amount spent.

### 4. View By Category

Groups expenses by category and calculates the total amount spent in each category.

### 5. Delete Expense

Allows users to delete an expense by selecting its number.

### 6. Exit

Safely closes the application.

---

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## Python Concepts Used

### Variables

Variables are used to store expense information and program data.

### Lists

A list is used to store multiple expense records.

### Dictionaries

Each expense is represented using a dictionary containing:

- Category
- Description
- Amount
- Date

### Functions

The application is organized into reusable functions, including:

- `add_expense()`
- `view_expenses()`
- `calculate_total()`
- `view_by_category()`
- `delete_expense()`
- `display_menu()`
- `main()`

### Loops

Loops are used to:

- Display expenses
- Repeatedly show the menu
- Validate user input

### Conditional Statements

Conditional statements are used to process menu choices and validate input.

### Exception Handling

`try-except` blocks are used to handle invalid numeric input and prevent the application from crashing.

---

## Project Structure

```text
codomax-module-2-python-project
│
├── README.md
│
└── main.py

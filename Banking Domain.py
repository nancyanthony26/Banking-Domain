#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import random
import datetime

class BankManagementSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register_user(self, username, password):
        if username not in self.users:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            account_number = str(random.randint(100000, 999999))
            self.users[username] = {
                'password': hashed_password,
                'account_number': account_number,
                'balance': 0,
                'transactions': []
            }
            print(f"User {username} registered successfully. Account Number: {account_number}")
        else:
            print("Username already exists. Please choose a different username.")

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == hashlib.sha256(password.encode()).hexdigest():
            self.logged_in_user = username
            print(f"Welcome, {username}!")
        else:
            print("Invalid credentials. Please try again.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully.")

    def deposit(self, amount):
        if self.logged_in_user:
            self.users[self.logged_in_user]['balance'] += amount
            self.users[self.logged_in_user]['transactions'].append(
                f"Deposit: +${amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            print(f"${amount} deposited successfully.")
        else:
            print("Please log in to perform transactions.")

    def withdraw(self, amount):
        if self.logged_in_user:
            if self.users[self.logged_in_user]['balance'] >= amount:
                self.users[self.logged_in_user]['balance'] -= amount
                self.users[self.logged_in_user]['transactions'].append(
                    f"Withdrawal: -${amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Please log in to perform transactions.")

    def display_balance(self):
        if self.logged_in_user:
            balance = self.users[self.logged_in_user]['balance']
            print(f"Account balance for {self.logged_in_user}: ${balance}")
        else:
            print("Please log in to view the balance.")

    def display_transactions(self):
        if self.logged_in_user:
            transactions = self.users[self.logged_in_user]['transactions']
            for transaction in transactions:
                print(transaction)
        else:
            print("Please log in to view transactions.")


# Example usage
bank_system = BankManagementSystem()

# Registering users
bank_system.register_user("user1", "password1")
bank_system.register_user("user2", "password2")

# Logging in
bank_system.login("user1", "password1")

# Performing transactions
bank_system.deposit(1000)
bank_system.withdraw(200)

# Displaying balance and transactions
bank_system.display_balance()
bank_system.display_transactions()

# Logging out
bank_system.logout()


# In[ ]:





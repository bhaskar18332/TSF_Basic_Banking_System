# Basic Banking System
Sparks Foundation Web Development Internship Project : Basic Banking System website.
A web application used to tranfer virtual money between multiple users and also record the banking transactions/ activities.

# Task
Start with a dummy data for upto 10 customers. Customers table with basic fields such as name, email, current balance etc. Transaction status: Transfer table/ Transfer History which records all the transactions

Flow : Home Page > View all customers > Select and View one customer > Transfer Money > Select customer to transfer to > View all Customers.

# Requirements
Os: Linux
1) Python
2) Pip
3) Virtual Environment

# How to run
1) Pull the Github repo
2) Enter the repo root directory
3) Create a python virtual environment using command "virtualenv venv"
4) Activate the environment using the command "source venv/bin/Activate"
5) Install the dependencies specified in requirements.txt by using the command "pip3 install -r requirements.txt"
6) Enter the task directory
7) Create a local_settings.py file (storing your secret key) in task/task/ directory along with the settings.py
8) Run the command "python3 manage.py runserver". The site should be live at localhost:8000.

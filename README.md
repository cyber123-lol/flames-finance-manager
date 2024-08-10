# flame's finance manager

**flame's finance manager** is a web application designed to help you manage your personal finances effectively. this application enables users to track their income and expenses, set and monitor savings goals, analyze financial data, and generate detailed reports. with a user-friendly interface and support for dark mode, it ensures that you can manage your finances in a way that suits your preferences


## features

flame's finance manager includes a range of features to help you stay on top of your finances:

* 1. user authentication and profile management


* 2. transaction management


* 3. savings goals setting and tracking


* 4. financial analytics and visualizations


* 5. report generation


## installation

follow these steps to install and run flame's finance manager on your local machine.

### 1. prerequisites

ensure you have the following installed:

- **python 3+**: the application is built using python, so make sure you have python 3.x installed

- **pip**: python's package installer, used to install the required python packages

### 2. clone the repository

clone the repository from github to your local machine by running this command within your IDE:

> sudo git clone https://github.com/cyber123-lol/flames-finance-manager.git

### 3. installing the requirements

navigate into the project's directory,

> cd flames-finance-manager

then install the required python packages by running the following command:

> pip install -r requirements.txt

### 4. initialization of the database

before running the applicaation, initialize the database by running the following command:

> python3 initialize_db.py

### 5. start the application

now run the flask application by running this command:
> flask run

now the application should be running locally on *http://127.0.0.1:5000/*

open this URL in your browser to access the application!




## usage

### 1. user registration and login

- **register**: create an account with a unique username and secure password

- **login**: access your dashboard using your registered credentials

### 2. dashboard

- **overview**: view a summary of your transactions and savings goals. the dashboard is neatly organized with collapsible sections for transactions and goals

- **dark/light mode**: use the toggle button at the top right of the navbar (navigation bar at the top of the site) to switch between dark and light themes

### 3. managing your transactions

- **add transaction**: enter details for new income or expense transactions, categorized by type and date

- **view transactions**: transactions are listed in a paginated format, with a limit of 10 per page for compact and easy browsing.

- **remove transaction**: delete transactions using the provided interface

### 4. setting and tracking savings goals

- **create goal**: define a new savings goal with a target amount

- **update goal**: add contributions to your goal and track progress as a percentage

- **delete goal**: remove goals that are no longer relevant

### 5. financial analysis

- **visual insights**: access pie charts displaying the distribution of your income and expenses by category

- **dark/light mode (again)**: charts adapt to the current theme, ensuring clear visibility in both dark and light modes

### 6. report generation

- **generate PDF reports**: compile your financial data into a downloadable PDF report. this report includes a summary of all transactions and goals, providing a comprehensive view of your financial status

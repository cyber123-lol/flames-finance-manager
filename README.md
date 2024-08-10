# flame's finance manager

**flame's finance manager** is a web application designed to help you manage your personal finances effectively. this application enables users to track their income and expenses, set and monitor savings goals, analyze financial data, and generate detailed reports. with a user-friendly interface and support for dark mode, it ensures that you can manage your finances in a way that suits your preferences


## features

flame's finance manager includes a range of features to help you stay on top of your finances:

### 1. user authentication and profile management
- **secure registration and login**: users can register with a unique username and password. login to access your personal finance dashboard.
- **profile management**: update your profile details and securely manage your account.

### 2. transaction management
- **add transactions**: record your income and expenses, categorized for easy tracking.
- **view transactions**: browse through a paginated list of your transactions, filtered by type, category, and date.
- **remove transactions**: delete any transaction that you no longer need.

### 3. savings goals setting and tracking
- **create goals**: set savings goals by defining a target amount and tracking your progress.
- **update goals**: add funds to your savings goals and monitor the percentage completion.
- **delete goals**: remove goals that are no longer relevant to your financial plan.

### 4. financial analytics and visualizations
- **expense and income charts**: visualize your financial data through interactive pie charts.
- **dark/light mode**: toggle between dark and light themes to suit your preference.

### 5. report generation
- **generate reports**: create comprehensive financial reports in pdf format, summarizing your transactions and goals.



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
open this URL in your browser to access the application.




## usage

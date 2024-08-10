from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify, send_file
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from reportlab.pdfgen import canvas
from io import BytesIO
from initialize_db import initialize_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
initialize_db()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# user model for authentication
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    # load a user from the database by user ID
    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    connection.close()
    if user:
        return User(id=user[0], username=user[1], password=user[2])
    return None

# home route that redirects to the registration page
@app.route('/')
def home():
    return redirect(url_for('dashboard'))

# user registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username.isalnum():
            flash('username must contain only letters and numbers', 'danger')
            return redirect(url_for('register'))
        if not password:
            flash('password is required!', 'danger')
            return redirect(url_for('register'))

        # hash the password securely
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        connection = sqlite3.connect('finance_manager.db')
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            connection.commit()
            flash('account created successfully.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('username already exists.', 'danger')
        finally:
            connection.close()
    return render_template('register.html')

# user login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        connection = sqlite3.connect('finance_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        connection.close()

        if user and check_password_hash(user[2], password):
            user_obj = User(id=user[0], username=user[1], password=user[2])
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        else:
            flash('login unsuccessful. please check username and password', 'danger')
    return render_template('login.html')

# user dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (current_user.id,))
    transactions = cursor.fetchall()

    cursor.execute('SELECT * FROM goals WHERE user_id = ?', (current_user.id,))
    goals = cursor.fetchall()

    connection.close()
    return render_template('dashboard.html', transactions=transactions, goals=goals)

# add transaction management route
@app.route('/manage_transaction', methods=['GET', 'POST'])
@login_required
def manage_transaction():
    page = int(request.args.get('page', 1))  # get the page number from the URL, default to 1
    per_page = 10  # results per page
    offset = (page - 1) * per_page

    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()

    if request.method == 'POST':
        action = request.form.get('action', 'add')
        
        if action == 'add':
            amount = request.form.get('amount')
            category = request.form.get('category')
            type = request.form.get('type')
            date = request.form.get('date')

            if amount.isdigit() and category and type and date:
                cursor.execute('INSERT INTO transactions (user_id, amount, category, type, date) VALUES (?, ?, ?, ?, ?)',
                               (current_user.id, amount, category, type, date))
                connection.commit()  # Commit changes to the database
                flash('transaction added successfully!', 'success')
            else:
                flash('please fill in all fields correctly.', 'danger')

        elif action == 'remove':
            transaction_id = request.form.get('transaction_id')
            cursor.execute('DELETE FROM transactions WHERE id = ? AND user_id = ?', (transaction_id, current_user.id))
            connection.commit()  # Commit changes to the database
            flash('transaction removed successfully!', 'success')

    # Fetch transactions for pagination
    cursor.execute('SELECT * FROM transactions WHERE user_id = ? LIMIT ? OFFSET ?', (current_user.id, per_page, offset))
    transactions = cursor.fetchall()

    # Get total count of transactions
    cursor.execute('SELECT COUNT(*) FROM transactions WHERE user_id = ?', (current_user.id,))
    total_transactions = cursor.fetchone()[0]
    
    connection.close()

    total_pages = (total_transactions + per_page - 1) // per_page  # calculate total number of pages

    return render_template('manage_transaction.html', transactions=transactions, page=page, total_pages=total_pages)

# add goal management route
@app.route('/manage_goal', methods=['GET', 'POST'])
@login_required
def manage_goal():
    page = int(request.args.get('page', 1))  # get the page number from the URL, default to 1
    per_page = 10  # results per page
    offset = (page - 1) * per_page

    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()

    if request.method == 'POST':
        action = request.form.get('action', 'add')
        
        if action == 'add':
            goal_name = request.form.get('goal_name')
            goal_amount = request.form.get('goal_amount')

            if goal_amount.isdigit() and goal_name:
                cursor.execute('INSERT INTO goals (user_id, goal_name, goal_amount) VALUES (?, ?, ?)',
                               (current_user.id, goal_name, goal_amount))
                connection.commit()  # commit changes to the database
                flash('goal added successfully!', 'success')
            else:
                flash('please fill in all fields correctly.', 'danger')

        elif action == 'remove':
            goal_id = request.form.get('goal_id')
            cursor.execute('DELETE FROM goals WHERE id = ? AND user_id = ?', (goal_id, current_user.id))
            connection.commit()  # commit changes to the database
            flash('goal removed successfully!', 'success')

        elif action == 'update':
            goal_id = request.form.get('goal_id')
            amount_to_add = request.form.get('amount_to_add')
            if amount_to_add.isdigit():
                cursor.execute('UPDATE goals SET current_amount = current_amount + ? WHERE id = ? AND user_id = ?',
                               (amount_to_add, goal_id, current_user.id))
                connection.commit()  # commit changes to the database
                flash('goal updated successfully!', 'success')
            else:
                flash('please enter a valid amount to add.', 'danger')

    # get goals for the current page
    cursor.execute('SELECT * FROM goals WHERE user_id = ? LIMIT ? OFFSET ?', (current_user.id, per_page, offset))
    goals = cursor.fetchall()

    # get total count of goals
    cursor.execute('SELECT COUNT(*) FROM goals WHERE user_id = ?', (current_user.id,))
    total_goals = cursor.fetchone()[0]

    connection.close()

    total_pages = (total_goals + per_page - 1) // per_page  # calculate total number of pages

    return render_template('manage_goal.html', goals=goals, page=page, total_pages=total_pages)

@app.route('/analytics')
@login_required
def analytics():
    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND type = "expense" GROUP BY category', (current_user.id,))
    expense_data = cursor.fetchall()

    cursor.execute('SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND type = "income" GROUP BY category', (current_user.id,))
    income_data = cursor.fetchall()

    connection.close()
    return render_template('analytics.html', expense_data=expense_data, income_data=income_data)

@app.route('/generate_report')
@login_required
def generate_report():
    connection = sqlite3.connect('finance_manager.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (current_user.id,))
    transactions = cursor.fetchall()

    cursor.execute('SELECT * FROM goals WHERE user_id = ?', (current_user.id,))
    goals = cursor.fetchall()

    connection.close()

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    
    # title
    p.drawString(250, 800, "> financial report <")
    
    # transactions section
    p.drawString(70, 780, "your transactions:")
    y = 760
    for transaction in transactions:
        p.drawString(100, y, f"ID: {transaction[0]}, Amount: {transaction[2]}, Category: {transaction[3]}, Type: {transaction[4]}, Date: {transaction[5]}")
        y -= 20

    # separator
    y -= 20
    p.drawString(70, y, "----------------------------------------------------------------------------------------------------------------------")
    y -= 20

    # goals section
    p.drawString(70, y, "your goals:")
    y -= 20
    for goal in goals:
        goal_progress = (goal[4] / goal[3]) * 100 if goal[3] > 0 else 0
        p.drawString(85, y, f"ID: {goal[0]}, Name: {goal[2]}, Amount: {goal[3]}, Current Amount: {goal[4]}, Progress: {goal_progress:.2f}%")
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='financial_report.pdf', mimetype='application/pdf')

@app.route('/toggle_dark_mode', methods=['POST'])
def toggle_dark_mode():
    data = request.get_json()
    session['dark_mode'] = data.get('dark_mode', False)
    return jsonify(success=True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
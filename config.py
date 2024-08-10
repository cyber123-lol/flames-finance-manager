import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    DATABASE = os.path.join(os.getcwd(), 'finance_manager.db')
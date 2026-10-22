import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'corporate-attendance-super-secret-key-2024')
    DATABASE_PATH = os.environ.get('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'attendance.db'))
    JWT_EXPIRATION_HOURS = 24
    TIMEZONE = 'Asia/Kolkata'

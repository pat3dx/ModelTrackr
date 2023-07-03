import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    CHATURBATE_API_KEY = os.environ.get('CHATURBATE_API_KEY')
    AI_SERVICE_URL = os.environ.get('AI_SERVICE_URL') or 'http://localhost:5000'
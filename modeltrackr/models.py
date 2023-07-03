```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Model(db.Model):
    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    last_online = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, status, last_online):
        self.name = name
        self.status = status
        self.last_online = last_online

class Recording(db.Model):
    __tablename__ = 'recordings'

    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    file_path = db.Column(db.String(256), nullable=False)

    def __init__(self, model_id, start_time, end_time, file_path):
        self.model_id = model_id
        self.start_time = start_time
        self.end_time = end_time
        self.file_path = file_path
```
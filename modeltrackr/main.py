```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from modeltrackr.config import DATABASE_URI, SECRET_KEY
from modeltrackr.controllers import login_user, logout_user, get_model_status, start_recording, end_recording, send_notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

@app.route('/login', methods=['POST'])
def login():
    return login_user()

@app.route('/logout', methods=['POST'])
def logout():
    return logout_user()

@app.route('/model_status', methods=['GET'])
def model_status():
    return get_model_status()

@app.route('/start_recording', methods=['POST'])
def start():
    return start_recording()

@app.route('/end_recording', methods=['POST'])
def end():
    return end_recording()

@app.route('/notification', methods=['POST'])
def notification():
    return send_notification()

if __name__ == "__main__":
    app.run(debug=True)
```
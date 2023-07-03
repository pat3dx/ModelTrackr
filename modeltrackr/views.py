```python
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import app, db
from .models import User, Model, Recording
from .controllers import login_user, logout_user, get_model_status, start_recording, end_recording
from .services.ai_service import AI_Service
from .services.chaturbate_service import Chaturbate_Service
from .services.recording_service import Recording_Service
from .services.notification_service import Notification_Service

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = login_user(username, password)
        if user:
            flash('user_logged_in')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('user_logged_out')
    return redirect(url_for('home'))

@app.route('/models')
@login_required
def models():
    models = Model.query.all()
    return render_template('models.html', models=models)

@app.route('/recordings')
@login_required
def recordings():
    recordings = Recording.query.all()
    return render_template('recordings.html', recordings=recordings)

@app.route('/model/<int:model_id>')
@login_required
def model(model_id):
    model = Model.query.get_or_404(model_id)
    status = get_model_status(model)
    return render_template('model.html', model=model, status=status)

@app.route('/start_recording/<int:model_id>')
@login_required
def start_rec(model_id):
    model = Model.query.get_or_404(model_id)
    recording = start_recording(model)
    if recording:
        flash('recording_started')
    return redirect(url_for('model', model_id=model.id))

@app.route('/end_recording/<int:recording_id>')
@login_required
def end_rec(recording_id):
    recording = Recording.query.get_or_404(recording_id)
    end_recording(recording)
    flash('recording_ended')
    return redirect(url_for('recordings'))
```
```python
from flask import request, jsonify
from modeltrackr import app, db
from modeltrackr.models import User, Model, Recording
from modeltrackr.services.ai_service import AI_Service
from modeltrackr.services.chaturbate_service import Chaturbate_Service
from modeltrackr.services.recording_service import Recording_Service
from modeltrackr.services.notification_service import Notification_Service

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'user_logged_in', 'user': user.username}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout_user():
    # Assuming user authentication is handled elsewhere
    return jsonify({'message': 'user_logged_out'}), 200

@app.route('/models', methods=['GET'])
def get_model_status():
    models = Model.query.all()
    model_status = Chaturbate_Service.get_model_status(models)
    return jsonify({'message': 'model_updated', 'models': model_status}), 200

@app.route('/recordings/start', methods=['POST'])
def start_recording():
    data = request.get_json()
    model = Model.query.get(data['model_id'])
    if model:
        recording = Recording_Service.start_recording(model)
        return jsonify({'message': 'recording_started', 'recording': recording.id}), 200
    return jsonify({'message': 'Model not found'}), 404

@app.route('/recordings/end', methods=['POST'])
def end_recording():
    data = request.get_json()
    recording = Recording.query.get(data['recording_id'])
    if recording:
        Recording_Service.end_recording(recording)
        return jsonify({'message': 'recording_ended', 'recording': recording.id}), 200
    return jsonify({'message': 'Recording not found'}), 404

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    Notification_Service.send_notification(data['user_id'], data['message'])
    return jsonify({'message': 'Notification sent'}), 200
```
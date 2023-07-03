```python
import requests
from modeltrackr.config import CHATURBATE_API_KEY, AI_SERVICE_URL

def get_model_status(model_name):
    response = requests.get(f"https://chaturbate.com/api/{model_name}?api_key={CHATURBATE_API_KEY}")
    return response.json()['status']

def start_recording(model_name):
    response = requests.post(f"{AI_SERVICE_URL}/start_recording", json={"model_name": model_name})
    return response.json()['recording_id']

def end_recording(recording_id):
    response = requests.post(f"{AI_SERVICE_URL}/end_recording", json={"recording_id": recording_id})
    return response.json()['status']

def send_notification(user_id, message):
    response = requests.post(f"{AI_SERVICE_URL}/send_notification", json={"user_id": user_id, "message": message})
    return response.json()['status']
```
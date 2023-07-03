```python
import requests

class AI_Service:
    def __init__(self, ai_service_url):
        self.ai_service_url = ai_service_url

    def analyze_model_performance(self, model_id):
        response = requests.get(f"{self.ai_service_url}/analyze/{model_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def predict_model_status(self, model_id):
        response = requests.get(f"{self.ai_service_url}/predict/{model_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
```
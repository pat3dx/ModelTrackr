```python
import requests
from modeltrackr.models import Model

class ChaturbateService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_model_status(self, model_name):
        response = requests.get(f"https://chaturbate.com/api/model/{model_name}?api_key={self.api_key}")
        data = response.json()
        return data['online']

    def update_model_status(self, model: Model):
        online = self.get_model_status(model.name)
        model.online = online
        return model

    def get_model_performance(self, model_name):
        response = requests.get(f"https://chaturbate.com/api/model/{model_name}/performance?api_key={self.api_key}")
        data = response.json()
        return data['performance']

    def record_model_performance(self, model_name):
        performance = self.get_model_performance(model_name)
        with open(f"{model_name}_performance.txt", "w") as file:
            file.write(performance)
```

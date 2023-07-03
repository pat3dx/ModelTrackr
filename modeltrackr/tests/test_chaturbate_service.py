```python
import unittest
from modeltrackr.services.chaturbate_service import Chaturbate_Service

class TestChaturbateService(unittest.TestCase):

    def setUp(self):
        self.chaturbate_service = Chaturbate_Service()

    def test_get_model_status(self):
        model_name = 'test_model'
        status = self.chaturbate_service.get_model_status(model_name)
        self.assertIn(status, ['online', 'offline'])

    def test_get_model_performance(self):
        model_name = 'test_model'
        performance = self.chaturbate_service.get_model_performance(model_name)
        self.assertIsInstance(performance, dict)

    def test_get_model_list(self):
        model_list = self.chaturbate_service.get_model_list()
        self.assertIsInstance(model_list, list)

if __name__ == '__main__':
    unittest.main()
```
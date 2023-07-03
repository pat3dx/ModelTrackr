```python
import unittest
from modeltrackr.services.ai_service import AI_Service

class TestAIService(unittest.TestCase):

    def setUp(self):
        self.ai_service = AI_Service()

    def test_get_model_status(self):
        model_id = 'test_model'
        status = self.ai_service.get_model_status(model_id)
        self.assertIn(status, ['online', 'offline'])

    def test_start_recording(self):
        model_id = 'test_model'
        recording_id = self.ai_service.start_recording(model_id)
        self.assertIsInstance(recording_id, str)

    def test_end_recording(self):
        recording_id = 'test_recording'
        result = self.ai_service.end_recording(recording_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```
```python
import unittest
from modeltrackr.services.recording_service import Recording_Service
from modeltrackr.models import RecordingSchema

class TestRecordingService(unittest.TestCase):

    def setUp(self):
        self.recording_service = Recording_Service()
        self.recording_schema = RecordingSchema()

    def test_start_recording(self):
        model_id = 'test_model'
        self.recording_service.start_recording(model_id)
        recording = self.recording_service.get_recording(model_id)
        self.assertIsNotNone(recording)
        self.assertEqual(recording['model_id'], model_id)
        self.assertTrue(recording['is_recording'])

    def test_end_recording(self):
        model_id = 'test_model'
        self.recording_service.start_recording(model_id)
        self.recording_service.end_recording(model_id)
        recording = self.recording_service.get_recording(model_id)
        self.assertIsNotNone(recording)
        self.assertEqual(recording['model_id'], model_id)
        self.assertFalse(recording['is_recording'])

    def test_get_recording(self):
        model_id = 'test_model'
        self.recording_service.start_recording(model_id)
        recording = self.recording_service.get_recording(model_id)
        self.assertIsNotNone(recording)
        self.assertEqual(recording['model_id'], model_id)

    def test_get_all_recordings(self):
        model_id1 = 'test_model1'
        model_id2 = 'test_model2'
        self.recording_service.start_recording(model_id1)
        self.recording_service.start_recording(model_id2)
        recordings = self.recording_service.get_all_recordings()
        self.assertEqual(len(recordings), 2)

if __name__ == '__main__':
    unittest.main()
```
```python
import unittest
from modeltrackr import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        self.model_data = {
            'model_name': 'test_model',
            'online_status': True
        }
        self.recording_data = {
            'model_name': 'test_model',
            'recording_status': True
        }

    def test_login_user(self):
        result = utils.login_user(self.user_data)
        self.assertEqual(result, 'user_logged_in')

    def test_logout_user(self):
        result = utils.logout_user(self.user_data)
        self.assertEqual(result, 'user_logged_out')

    def test_get_model_status(self):
        result = utils.get_model_status(self.model_data)
        self.assertEqual(result, True)

    def test_start_recording(self):
        result = utils.start_recording(self.recording_data)
        self.assertEqual(result, 'recording_started')

    def test_end_recording(self):
        result = utils.end_recording(self.recording_data)
        self.assertEqual(result, 'recording_ended')

    def test_send_notification(self):
        result = utils.send_notification('test_message')
        self.assertEqual(result, 'test_message')

if __name__ == '__main__':
    unittest.main()
```
```python
import unittest
from modeltrackr import app, db
from modeltrackr.controllers import login_user, logout_user, get_model_status, start_recording, end_recording
from modeltrackr.models import User, Model, Recording

class TestControllers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_login_user(self):
        response = login_user('test_user', 'test_password')
        self.assertEqual(response, 'user_logged_in')

    def test_logout_user(self):
        response = logout_user('test_user')
        self.assertEqual(response, 'user_logged_out')

    def test_get_model_status(self):
        model = Model('test_model')
        self.db.session.add(model)
        self.db.session.commit()
        response = get_model_status('test_model')
        self.assertIsNotNone(response)

    def test_start_recording(self):
        model = Model('test_model')
        self.db.session.add(model)
        self.db.session.commit()
        response = start_recording('test_model')
        self.assertEqual(response, 'recording_started')

    def test_end_recording(self):
        model = Model('test_model')
        recording = Recording('test_recording', model.id)
        self.db.session.add(model)
        self.db.session.add(recording)
        self.db.session.commit()
        response = end_recording('test_model')
        self.assertEqual(response, 'recording_ended')

if __name__ == '__main__':
    unittest.main()
```
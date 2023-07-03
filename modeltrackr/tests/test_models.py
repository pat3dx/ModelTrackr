```python
import unittest
from modeltrackr.models import User, Model, Recording
from modeltrackr import db

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User(username='testuser', password='testpassword')
        self.model = Model(name='testmodel', status='online')
        self.recording = Recording(model_id=1, duration=30)

        db.session.add(self.user)
        db.session.add(self.model)
        db.session.add(self.recording)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testpassword')

    def test_model_model(self):
        self.assertEqual(self.model.name, 'testmodel')
        self.assertEqual(self.model.status, 'online')

    def test_recording_model(self):
        self.assertEqual(self.recording.model_id, 1)
        self.assertEqual(self.recording.duration, 30)

if __name__ == "__main__":
    unittest.main()
```
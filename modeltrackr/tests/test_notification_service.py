```python
import unittest
from modeltrackr.services.notification_service import Notification_Service

class TestNotificationService(unittest.TestCase):

    def setUp(self):
        self.notification_service = Notification_Service()

    def test_send_notification(self):
        result = self.notification_service.send_notification("test_user", "model_updated")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```
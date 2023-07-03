import unittest
from modeltrackr import config

class TestConfig(unittest.TestCase):

    def test_database_uri(self):
        self.assertEqual(config.DATABASE_URI, 'your_database_uri')

    def test_secret_key(self):
        self.assertEqual(config.SECRET_KEY, 'your_secret_key')

    def test_chaturbate_api_key(self):
        self.assertEqual(config.CHATURBATE_API_KEY, 'your_chaturbate_api_key')

    def test_ai_service_url(self):
        self.assertEqual(config.AI_SERVICE_URL, 'your_ai_service_url')

if __name__ == '__main__':
    unittest.main()
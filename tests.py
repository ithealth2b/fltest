import unittest
import main as tested_app
'''
tests
'''

class FlaskTest(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello, World!')

    def test_get_new(self):
        r = self.app.get('/new')
        self.assertEqual(r.data, b'new word')


if __name__ == '__main__':
    unittest.main()

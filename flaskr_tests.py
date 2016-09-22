import TestSam2
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):

        TestSam2.app.config['TESTING'] = True
        self.app = TestSam2.app.test_client()

    def test_getFolderUrl(self):
        rv = self.app.get('/directory/fokat')
        self.assertEqual(rv.status_code, 200)

    def test_getFileUrl(self):
        rv = self.app.get('/directory/fokat/files/myFile')
        self.assertEqual(rv.status_code, 200)

    def test_postFolderUrl(self):
        rv = self.app.post('/directory/fokat')
        self.assertEqual(rv.status_code, 200)

    def test_postFileUrl(self):
        rv = self.app.post('/directory/fokat/files/myFile')
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()
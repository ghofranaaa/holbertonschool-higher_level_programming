import unittest
import requests

class TestEndpoints(unittest.TestCase):
    
    def test_root_endpoint(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")
        
    def test_data_endpoint(self):
        response = requests.get('http://localhost:8000/data')
        self.assertEqual(response.status_code, 200)
        expected_json = {"name": "John", "age": 30, "city": "New York"}
        self.assertDictEqual(response.json(), expected_json)
        
    def test_status_endpoint(self):
        response = requests.get('http://localhost:8000/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
        
    def test_undefined_endpoint(self):
        response = requests.get('http://localhost:8000/undefined')
        self.assertEqual(response.status_code, 404)  # Expecting a 404 Not Found
        self.assertIn("Endpoint not found", response.text)  # Check for specific error message

if __name__ == '__main__':
    unittest.main()

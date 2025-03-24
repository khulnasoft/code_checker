import unittest
from fastapi.testclient import TestClient
from code_checker.src.api.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Security Scanner API"})

    def test_scan_code(self):
        response = self.client.post("/scan/", json={"directory": "test_dir"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("sast_issues", response.json())
        self.assertIn("dep_issues", response.json())

if __name__ == '__main__':
    unittest.main()

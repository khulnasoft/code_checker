import unittest
import os
import json
from code_checker.src.scanner.dep_scan import DependencyScanner, load_config, scan_directory

class TestDependencyScanner(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.scanner = DependencyScanner(self.config)

    def test_scan_file(self):
        dependencies = ["example==1.0.0"]
        with open('test_requirements.json', 'w') as f:
            json.dump(dependencies, f)
        issues = self.scanner.scan_file('test_requirements.json')
        self.assertEqual(len(issues), 1)
        self.assertIn("Vulnerable dependency found: example==1.0.0", issues)

    def test_scan_dependencies(self):
        dependencies = ["example==1.0.0"]
        issues = self.scanner.scan_dependencies(dependencies)
        self.assertEqual(len(issues), 1)
        self.assertIn("Vulnerable dependency found: example==1.0.0", issues)

    def test_scan_directory(self):
        os.makedirs('test_dir', exist_ok=True)
        dependencies = ["example==1.0.0"]
        with open('test_dir/requirements.txt', 'w') as f:
            json.dump(dependencies, f)
        issues = scan_directory('test_dir')
        self.assertEqual(len(issues), 1)
        self.assertIn("Vulnerable dependency found: example==1.0.0", issues)

if __name__ == '__main__':
    unittest.main()

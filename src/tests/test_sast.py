import unittest
import ast
from code_checker.src.scanner.sast import SASTScanner, ExampleRule, load_rules

class TestSASTScanner(unittest.TestCase):
    def setUp(self):
        self.rules = load_rules()
        self.scanner = SASTScanner(self.rules)

    def test_scan_file(self):
        code = """
def example():
    pass
"""
        with open('test_file.py', 'w') as f:
            f.write(code)
        issues = self.scanner.scan_file('test_file.py')
        self.assertEqual(len(issues), 1)
        self.assertIn("Function named 'example' found at line 2", issues)

    def test_scan_tree(self):
        code = """
def example():
    pass
"""
        tree = ast.parse(code)
        issues = self.scanner.scan_tree(tree)
        self.assertEqual(len(issues), 1)
        self.assertIn("Function named 'example' found at line 2", issues)

if __name__ == '__main__':
    unittest.main()

from main import extract_title
import unittest

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# title")
        self.assertEqual(title, "title")
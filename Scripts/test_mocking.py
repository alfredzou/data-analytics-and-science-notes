import unittest

# We import patch, which allows us to intercept mocking.requests.get and replaces it with a Mock object
from unittest.mock import patch

from mocking import visit_website


class TestWebsite(unittest.TestCase):
    def test_connection(self):
        # We patch mocking.requests.get instead of requests.get, to ensure we use it
        with patch("mocking.requests.get") as mocked_get:
            # Checking the positive case
            # mocked_get.return_value = r()
            # mocked_get.return_value.ok = r.ok

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "I'm mocked"

            self.assertEqual(visit_website(), "I'm mocked")

            # Checking the negative case
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "I'm not mocked"

            self.assertEqual(visit_website(), "Bad Response!")


if __name__ == "__main__":
    unittest.main()

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Runs at the beginning of the test suite
        print("setupClass\n")

    @classmethod
    def tearDownClass(cls):
        # Runs at the end of the test suite
        print("tearDownClass\n")

    def setUp(self):
        # Runs at the beginning of every test
        print("setting up employee 1 & 2")
        self.emp_1 = Employee("Tim", "Wong")
        self.emp_2 = Employee("Julia", "Bishop")

    def tearDown(self):
        # Runs at the end of every test
        print("deleting employee 1 & 2\n")
        del self.emp_1
        del self.emp_2

    def test_init(self):
        # Test init is working
        print("Checking init OK")
        self.assertEqual(self.emp_1.firstname, "Tim")
        self.assertEqual(self.emp_1.lastname, "Wong")
        self.assertEqual(self.emp_2.firstname, "Julia")
        self.assertEqual(self.emp_2.lastname, "Bishop")

    def test_fullname(self):
        print("Checking fullname OK on init and changing firstname")
        # Test init is working
        self.assertEqual(self.emp_1.fullname, "Tim Wong")
        self.assertEqual(self.emp_2.fullname, "Julia Bishop")

        # Test setter is working
        self.emp_1.firstname = "John"
        self.emp_2.firstname = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Wong")
        self.assertEqual(self.emp_2.fullname, "Jane Bishop")

    def test_email(self):
        print("Checking email OK on init and changing firstname")
        # Test init is working
        self.assertEqual(self.emp_1.email, "Tim.Wong@email.com")
        self.assertEqual(self.emp_2.email, "Julia.Bishop@email.com")

        # Test setter is working
        self.emp_1.firstname = "John"
        self.emp_2.firstname = "Jane"

        self.assertEqual(self.emp_1.email, "John.Wong@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Bishop@email.com")

    def test_nametype(self):
        print("Checking input conditions are string only")
        # Test input conditions
        self.assertRaises(TypeError, Employee, 1, 2)

    def test_return_firstname(self):
        print("Checking getter method")
        # Testing getter method
        self.assertEqual(self.emp_1.firstname, "Tim")


if __name__ == "__main__":
    unittest.main()

import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student("Ali", "Mali")
        self.assertEqual(student.full_name, "Ali Mali")

    def test_alert_santa(self):
        student = Student("Ali", "Mali")
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email(self):
        student = Student("Ali", "Mali")
        self.assertEqual(student.email, "ali.mali@email.com")


if __name__ == "__main__":
    unittest.main()

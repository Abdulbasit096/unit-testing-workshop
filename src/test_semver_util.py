import unittest
import src.semver_util as su


class TestSemverUtil(unittest.TestCase):

    def test_break_into_parts(self):
        actual_major, actual_minor, actual_micro, actual_release_type = su.break_into_parts('0.0.1')
        exp_major, exp_minor, exp_micro = 0, 0, 1
        self.assertEqual(exp_major, actual_major)
        self.assertEqual(exp_minor, actual_minor)
        self.assertEqual(exp_micro, actual_micro)
        self.assertIsNone(actual_release_type)

    def test_break_into_parts_with_release_type(self):
        actual_major, actual_minor, actual_micro, actual_release_type = su.break_into_parts('0.2.5-beta')
        exp_major, exp_minor, exp_micro, exp_release_type = 0, 2, 5, 'beta'
        self.assertEqual(exp_major, actual_major)
        self.assertEqual(exp_minor, actual_minor)
        self.assertEqual(exp_micro, actual_micro)
        self.assertEqual(exp_release_type, actual_release_type)

    def test_break_into_parts_with_release_type(self):
        try:
            su.break_into_parts('0.2.5-delta')
        except Exception:
            pass
        else:
            self.fail('The version has an invalid release type.')

    def test_increase_major(self):
        actual = su.increase_major('1.4.0')
        expected = '2.0.0'  # Since minor and micro versions will be reset
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

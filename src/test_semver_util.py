import unittest
import semver_util as su


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

    def test_break_into_parts_without_release_type(self):
        actual_major, actual_minor, actual_micro, actual_release_type = su.break_into_parts('2.6.3')
        exp_major, exp_minor, exp_micro, exp_release_type = 2, 6, 3, None
        self.assertEqual(exp_major, actual_major)
        self.assertEqual(exp_minor, actual_minor)
        self.assertEqual(exp_micro,actual_micro)
        self.assertEqual(exp_release_type,actual_release_type)

    def test_is_version_valid(self):
        try:
            su.is_version_valid('5.3')
        except Exception:
            pass
        else:
            self.fail('Invalid version')

    def test_is_version_valid_with_wrong_release_type(self):
        try:
            su.is_version_valid('5.3-gama')
        except Exception:
            pass
        else:
            self.fail('Invalid version')




    def test_increase_major(self):
        actual = su.increase_major('1.4.0')
        expected = '2.0.0'  # Since minor and micro versions will be reset
        self.assertEqual(expected, actual)

    def test_increase_major_with_release_type(self):
        actual = su.increase_major('1.4.0-beta')
        expected = '2.0.0-beta'  # Since minor and micro versions will be reset
        self.assertEqual(expected, actual)

    def test_increase_major_with_wrong_release_type(self):
        try:
            su.increase_major('1.4.0-gama')
        except Exception:
            pass
        else:
            self.fail('The version has an invalid release type.')

    def test_increase_minor(self):
        actual = su.increase_minor('1.4.5')
        expected = '1.5.0'  # Since micro versions will be reset
        self.assertEqual(expected, actual)

    def test_increase_minor_with_release_type(self):
        actual = su.increase_minor('1.4.6-beta')
        expected = '1.5.0-beta'  # Since micro versions will be reset
        self.assertEqual(expected, actual)

    def test_increase_minor_with_wrong_release_type(self):
        try:
            su.increase_minor('1.4.0-gama')
        except Exception:
            pass
        else:
            self.fail('The version has an invalid release type.')

    def test_increase_micro(self):
        actual = su.increase_micro('1.4.5')
        expected = '1.4.6'
        self.assertEqual(expected, actual)

    def test_increase_micro_with_release_type(self):
        actual = su.increase_micro('1.4.6-beta')
        expected = '1.4.7-beta'
        self.assertEqual(expected, actual)

    def test_increase_micro_with_wrong_release_type(self):
        try:
            su.increase_micro('1.5.7-sigma')
        except Exception:
            pass
        else:
            self.fail('The version has an invalid release type.')

    def test_is_aplha(self):
        self.assertTrue(su.is_alpha('8.4.9-alpha'))

    def test_is_aplha_with_wrong_release_type(self):
        self.assertFalse(su.is_alpha('8.9.5-beta'))

    def test_is_aplha_with_no_release_type(self):
        self.assertFalse(su.is_alpha('8.9.5'))

    def test_is_beta(self):
        self.assertTrue(su.is_beta('8.4.9-beta'))

    def test_is_beta_with_wrong_release_type(self):
        self.assertFalse(su.is_beta('8.9.5-alpha'))

    def test_is_beta_with_no_release_type(self):
        self.assertFalse(su.is_beta('8.9.5'))

    def test_is_release(self):
        self.assertTrue(su.is_release('8.4.9'))

    def test_is_release_with_alpha(self):
        self.assertFalse(su.is_release('8.9.5-alpha'))

    def test_is_release_with_beta(self):
        self.assertFalse(su.is_release('8.9.5-beta'))

if __name__ == '__main__':
    unittest.main()

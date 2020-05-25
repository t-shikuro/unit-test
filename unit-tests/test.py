import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_doing_things(self):
        """ Testing 1st """
        test_param = 10
        result = main.doing_things(test_param)
        self.assertEqual(result, 15)

    def test_doing_things2(self):
        test_param = 'fsdfex'
        result = main.doing_things(test_param)
        self.assertIsInstance(result, ValueError)

    def test_doing_things3(self):
        test_param = None
        result = main.doing_things(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print('cleaning up')


if __name__ == "__main__":
    unittest.main()

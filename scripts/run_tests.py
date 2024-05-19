import unittest

def run_tests():
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == "__main__":
    run_tests()


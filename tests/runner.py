import unittest
import tests.SyncFileTest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(tests.SyncFileTest))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)


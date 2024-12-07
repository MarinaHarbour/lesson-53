import unittest
import tests_12_3


tests_12_3_ST = unittest.TestSuite()
tests_12_3_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tests_12_3_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests_12_3_ST)

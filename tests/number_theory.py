import unittest

from algorithms.number_theory.sieve_of_eratosthenes import prime_sieve

class Test(unittest.TestCase):

    def prime_sieve_test(self):
        self.assertEqual(list(prime_sieve(10)), [2, 3, 5, 7])

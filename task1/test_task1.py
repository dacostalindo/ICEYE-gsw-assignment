#!/usr/bin/env python3

import unittest
import random
from task1 import return_coins

class TestTask1(unittest.TestCase):

    def test_sum(self):

        # Randomly genarated prices
        coffee_price = random.randint(5,200)
        eur_inserted = random.randint(100, 300)

        # Theoretical Change
        change_theoretical = eur_inserted - coffee_price

        # Actual Change
        change_dictionary = return_coins(coffee_price, eur_inserted)
        change_experimental = 0
        for key in change_dictionary:
            change_experimental += key * change_dictionary[key]

        # Test
        self.assertEqual(change_experimental, change_theoretical)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

import unittest
from task1 import return_coins
import random

class TestTask1(unittest.TestCase):

    def test_sum(self):

        coffee_price = round(random.uniform(0.5,2),2)
        eur_inserted = round(random.uniform(2, 10), 2)

        # Theoretical Change
        change_theoretical = eur_inserted - coffee_price

        # Actual Change
        change_dictionary = return_coins(coffee_price, eur_inserted)
        change_experimental = 0

        for key in change_dictionary:
            change_experimental += key * change_dictionary[key]

        self.assertEqual(change_experimental, change_theoretical)



if __name__ == '__main__':
    unittest.main()

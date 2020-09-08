#!/usr/bin/env python3

import unittest
from task1 import return_coins
import random

class TestTask1(unittest.TestCase):

    def test_sum(self):

        coffee_price = random.randint(5,200)
        eur_inserted = random.randint(200, 1000)

        # Theoretical Change
        change_theoretical = eur_inserted - coffee_price
        # print("The change: {}".format(change_theoretical))

        # Actual Change
        change_dictionary = return_coins(coffee_price, eur_inserted)
        change_experimental = 0


        for key in change_dictionary:
            # print("coins: {} *num_of_coins: {}".format(key, change_dictionary[key])))
            change_experimental += key * change_dictionary[key]
            # print(change_experimental)

        self.assertEqual(change_experimental, change_theoretical)



if __name__ == '__main__':
    unittest.main()

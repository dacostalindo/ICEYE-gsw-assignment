#!/usr/bin/env python3

import unittest
import xkcd as xkcd_class
import random

class TestXKCD(unittest.TestCase):

    def test_storing(self):

        max_comics  = 2356
        xkcd_object = xkcd_class.XKCD_SERVICE(max_comics)
        xkcd_object.save_comic()
        print("Comics List: {}".format(xkcd_object._get_comiclist()))


if __name__ == '__main__':
    unittest.main()

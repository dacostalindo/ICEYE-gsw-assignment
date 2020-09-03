#!/usr/bin/env python3

import unittest
import xkcd as xkcd_class

class TestXKCD(unittest.TestCase):

    def test(self):
        xkcd_object = xkcd_class.XKCD_SERVICE(2355)
        json = xkcd_object.get_JSON()
        xkcd_object.save_images()



if __name__ == '__main__':
    unittest.main()

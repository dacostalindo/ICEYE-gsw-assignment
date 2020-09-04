#!/usr/bin/env python3

import unittest
import xkcd as xkcd_class
<<<<<<< HEAD
import random

class TestXKCD(unittest.TestCase):

    def test_storing(self):

        # number_tests = 10

        max_comics   = 2
        xkcd_object = xkcd_class.XKCD_SERVICE(max_comics)
        xkcd_object.save_comic()

        # for i in number_tests:
        #     xkcd_object = xkcd_class.XKCD_SERVICE(random.randint(0, max_comics))
        #     comic_list  = xkcd_object._get_comiclist()
        #
        #     if xkcd_object.consecutive_bad == True:
        #         raise ValueError("We have got equal consecutive photos!")
        #
        #     if len(comic_list) > 2:
        #         raise ValueError("We have got equal consecutive photos!")
        #     else if len(comic_list) < 2:
        #         xkcd_object.save_comic()
        #     else:
        #         print("We have too many comics saved")



        print("Comics List: {}".format(xkcd_object._get_comiclist()))




    # def test_same_consecutive_images(self):
    #
    #     debug = True
    #     fake_comics_nums = [1, 23, 23, 4, 5, 5, 6]
    #
    #     for comic_num in fake_comics_nums :
    #         xkcd_object = xkcd_class.XKCD_SERVICE(comic_num, debug)
    #         xkcd_object.save_image()

=======

class TestXKCD(unittest.TestCase):

    def test(self):
        xkcd_object = xkcd_class.XKCD_SERVICE(2355)
        json = xkcd_object.get_JSON()
        xkcd_object.save_images()
>>>>>>> f329c70682e57992e43b827a9e8a0a1ce52b06a2



if __name__ == '__main__':
    unittest.main()

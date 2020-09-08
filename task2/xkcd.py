#!/usr/bin/env python3

import urllib.request
import json
import random
import os


class  XKCD_SERVICE(object) :

    def __init__(self, max_comics):
        self.comic_max = max_comics


    def save_comic(self):

        comic_removed = ""
        new_comic_url, new_comic_name = self._get_JSON()
        comics_list = self._get_comiclist()

        if not comics_list :
            urllib.request.urlretrieve(new_comic_url, new_comic_name)

        else:

            last_comic_added = comics_list[-1]
            # print("Last comic added: {} and new comic to be added: {}".format(last_comic_added, new_comic_name))
            while last_comic_added == new_comic_name:
                # print("We have got equal consecutive photos!")
                new_comic_url, new_comic_name = self._get_JSON()
                # print("New comic inside while loop: {}:".format(new_comic_name))


            if len(comics_list) == 1:
                urllib.request.urlretrieve(new_comic_url, new_comic_name)

            else:
                comic_removed = random.choice(comics_list)
                os.remove(comic_removed)
                urllib.request.urlretrieve(new_comic_url, new_comic_name)


        # print("Just removed: '{}' and stored the image: '{}'".format(comic_removed, new_comic_name))


    def _get_JSON(self):

        with urllib.request.urlopen("https://xkcd.com/{}/info.0.json".format(self._get_random_num_comic())) as url:
            data = json.loads(url.read().decode())
            new_comic_url = data['img']
            new_comic_name = data['title']+'.jpg'
        return new_comic_url, new_comic_name


    def _get_comiclist(self):

        filelist =os.listdir('./')
        for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
            if not(fichier.endswith(".jpg")):
                filelist.remove(fichier)
        sorted_jpgcomics = sorted(filelist, key=os.path.getmtime)
        return sorted_jpgcomics


    def _get_random_num_comic(self):

        comic_num = random.randint(1, self.comic_max)
        return comic_num


"""
Do not like this one bit. Find a way to determine the number of available comic
strips whitout iterating through every url from 0 to n. Maybe binary search
algorithm
"""

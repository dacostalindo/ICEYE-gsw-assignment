#!/usr/bin/env python3
import urllib.request
import json
import random
import os


class  XKCD_SERVICE(object) :

    def __init__(self, max_comics):
        if max_comics > 2356:
            raise ValueError("Max comics should be below or equal to 2356 - the max number of comics available on the website! - and above 0 - the min on the website!")
        else:
            self.comic_max = max_comics


    def save_comic(self):

        comic_removed = ""
        new_comic_url, new_comic_name = self._get_JSON()
        comics_list = self._get_comiclist()

        if not comics_list : #no images
            urllib.request.urlretrieve(new_comic_url, new_comic_name)

        else:

            last_comic_added = comics_list[-1]

            while last_comic_added == new_comic_name: # repeated images to be downloaded
                new_comic_url, new_comic_name = self._get_JSON()

            if len(comics_list) == 1: #1 image
                urllib.request.urlretrieve(new_comic_url, new_comic_name)

            else: #2 images
                comic_removed = random.choice(comics_list)
                os.remove(comic_removed)
                urllib.request.urlretrieve(new_comic_url, new_comic_name)




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

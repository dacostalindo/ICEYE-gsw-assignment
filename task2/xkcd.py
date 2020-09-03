#!/usr/bin/env python3

import urllib.request
import json
import random
import os


class  XKCD_SERVICE(object) :

    def __init__(self, max_comics):
        self.comic_num = random.randint(0, max_comics) # 2355



    def get_JSON(self):

        with urllib.request.urlopen("https://xkcd.com/{}/info.0.json".format(self.comic_num)) as url:
            data = json.loads(url.read().decode())
            image_url = data['img']
            image_name = data['title']+'.jpg'
        return image_url, image_name


    def get_filelist(self):

        filelist=os.listdir('./')
        for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
            if not(fichier.endswith(".jpg")):
                filelist.remove(fichier)
        return filelist


    def save_images(self):

        image_url, image_name = self.get_JSON()
        filelist = self.get_filelist()


        latest_file = max(list_of_files, key=os.path.getctime)

        while image_name == filelist[-1]:
            data = self.get_JSON()

        if len(filelist) < 2 :
            urllib.request.urlretrieve(image_url, image_name)
        else:
            os.remove(random.choice(filelist))
            urllib.request.urlretrieve(image_url, image_name)







        #
        # image_name !=  filename[:-4] and len(filelist) == 1:
        #     urllib.request.urlretrieve(image_url, "{}.jpg".format(image_name))
        # else if image_name !=  filename[:-4]  and len(filelist) == 2:
        #     os.remove(random.choice(filename))




        # else:
        #     if name[:-4] != image_name and len(filelist) < 2:
        #         urllib.request.urlretrieve(image_url, "{}.jpg".format(image_name))
        #     else
        #     if len(filelist) ==  2:
        #




"""
Do not like this one bit. Find a way to determine the number of available comic
strips whitout iterating through every url from 0 to n. Maybe binary search
algorithm
"""
#
# self.comic_num = random.randint(0, max_comics) # 2355

# Number of comic strips available so far on https://xkcd.com
#
# with urllib.request.urlopen("https://xkcd.com/{}/info.0.json".format(comic_num)) as url:
#     data = json.loads(url.read().decode())





# filelist=os.listdir('./')
# for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
#     if not(fichier.endswith(".jpg")):
#         filelist.remove(fichier)


# check if images names in the local filesystem coincide with the randomly generated
# if not filelist: # Checks if filelist is empty
#     urllib.request.urlretrieve(image_url, "{}.jpg".format(image_name))
# else:
#     if name[:-4] != image_name and len(filelist) < 2:
#         urllib.request.urlretrieve(image_url, "{}.jpg".format(image_name))
#     else
#     if len(filelist) ==  2
#
#
#
# for name in filelist:
#     if name[:-4] != image_name and len(filelist) < 2 :
#         urllib.request.urlretrieve(image_url, "{}.jpg".format(image_name))

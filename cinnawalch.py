# File: cinnawallch.py
# Author: kodejak <mail at kodejak dot de>
#
# Usage: "python cinnawallch.py &"

import os, os.path
import time
import sys
from random import randint

wall_allowed = ['.jpg', '.jpeg', '.png', '.bmp']
wall_dir = '/home/cipher/ownCloud/Wallpaper'
sleeptime = 30 #minutes

def getrandomfile(directory):
    walls_a = []
    walls_s = set(wall_allowed)
    for root, dirs, files in os.walk(directory):
        for f in files:
            fullpath = os.path.join(root, f)
            if os.path.splitext(fullpath)[1] in walls_s:
                walls_a.append(fullpath)
                #print fullpath

    a_len = len(walls_a)
    num = randint(1, a_len)
    pos = 0
    for elem in walls_a:
        pos+=1
        if pos == num:
            return elem

def changewall(fname):
    if len(fname) > 0:
        command = 'gsettings set org.cinnamon.desktop.background picture-uri  "file:///%s"' % fname
        os.system(command)

def main():
    curr_file = ''
    while (1):
        curr_file = getrandomfile(wall_dir)
        #print curr_file
        changewall(curr_file)
        time.sleep(sleeptime*60)


main()

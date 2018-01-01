# -*- coding: utf-8 -*-
"""
getting the fm4 jahrescharts from the online player
"""

import sys
from selenium import webdriver
import time
import pandas as pd

# 100-66: http://fm4.orf.at/player/20171231/CH
# 66-33: http://fm4.orf.at/player/20171231/CH1
# 33-1: http://fm4.orf.at/player/20171231/CH2

url = sys.argv[1]

# open firefox browser and navigate to fm4 player
wd = webdriver.Firefox()
wd.get(url)
time.sleep(3)

# click on tracklist to get tracklist
wd.find_element_by_xpath("""/html/body/div[1]/div/main/div/div[4]/section/h4/a/span""").click()
# get playlist
playlist = wd.find_element_by_id("broadcast-playlist")

# get info from playlist
tracks = playlist.find_elements_by_class_name("start-time")
interpreter = playlist.find_elements_by_class_name("interpreter")
titles = playlist.find_elements_by_class_name("title")

# when was the song played
started = []
for t in tracks:
    s = t.text
    started.append(s)
    
# name of artist
artist = []
for i in interpreter:
    inter = i.text
    artist.append(inter)

# name of the song
song = []
for tit in titles:
    so = tit.find_element_by_css_selector('a').get_attribute('text')
    song.append(so)
    
# tidy it up
jahrescharts = pd.DataFrame({'played': started,
                             'artist': artist,
                             'song': song})
        
# save data
tracklist_name = 'data/' + sys.argv[2]
print('file saved to ' + tracklist_name)
jahrescharts.to_csv(tracklist_name)


# close browser    
wd.quit()
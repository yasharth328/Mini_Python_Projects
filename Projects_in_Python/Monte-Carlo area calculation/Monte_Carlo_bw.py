"""
Only black and white images possible
Any size

"""

import numpy as np
import cv2
import random

def black_ratio(black_pixel,white_pixel):
    ratio_black = float("{:.5f}".format(black_pixel/(black_pixel+white_pixel)))
    return ratio_black*100

def pixel_count(img,h,w):
    black_pixel = white_pixel = 0
    for i in range(h):
        for j in range(w):
            if img[i,j] == 0:
                black_pixel += 1
            else :
                white_pixel += 1
    return black_pixel,white_pixel


img = cv2.imread(r'C:\Users\varun\Coding\python_practice\Project_pie\test_c_01_tt.png',0)
# Image as a numpy array

# Getting shape of image
h, w = img.shape

iterations = [100,1000,10000,1000000]

# Count of black and white pixel in the random sampling
count_white = [0]*4
count_black = [0]*4

bl_px,wh_px = pixel_count(img,h,w)

print("Actual total black pixel(brute force) :",bl_px)
print("Actual ratio of black pixels(brute force) :",black_ratio(bl_px,wh_px))

# Getting "iteration" number of pixels
for i in range(4):
    for j in range(iterations[i]):
        # Random pixel values
        x = random.randint(0,h-1)
        y = random.randint(0,w-1)

        check_list = []
        # Ensuring no repeatation of pixels
        if [x,y] not in check_list : 
            if img[x,y] == 0 :
                count_black[i] += 1
            else :
                count_white[i] += 1

        else :
            j -= 1

    # Appending black pixel to total value to the list
    print('\n')
    print(f"Number of black pixels for {iterations[i]} iterations :",int(black_ratio(count_black[i],count_white[i])*h*w)//100)
    print(f"Ratio of black pixels for {iterations[i]} ierations :",round(black_ratio(count_black[i],count_white[i]),3))
    
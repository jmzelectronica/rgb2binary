
import cv2 
import matplotlib.pyplot as plt
import numpy as np
import glob

folder_dir = './train_w/*.*' #Mask
folder_output = 'train_ww' #carpeta de las mascaras nuevas

for bb,file in enumerate (glob.glob(folder_dir)):
    img = cv2.imread(file)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    binary = img_hsv[:,:,0]
    plt.imsave('manglar{}.png'.format(bb), binary,cmap = 'gray')

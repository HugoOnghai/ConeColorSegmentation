# Hugo Onghai (hpo8)
# ECE 5242, Project 1
# Step 1. Hand Labeling Training Data

'''
My process:
for each image in the training set:
    define the roi for the cone region
    define three rois for non-cone regions
        (don't just do the entire background, because it's too much information/the final gaussian will be too big)

Functions:
extractROI(name_of_region, mask_file, mask_array, image_file)
'''

import numpy as np
import pandas as pd
from roipoly import RoiPoly
from matplotlib import pyplot as plt
from pathlib import Path
import glob
import os

cwd = Path.cwd()
training_path = (cwd / 'ECE5242Proj1-train').resolve()

def extractROI(name_of_region, mask_file, image_file):
    # display the training image
    plt.figure()
    training_image = plt.imread(image_file)
    plt.imshow(training_image)
    plt.title(f"Make a mask for the {name_of_region}")

    # request roi from user, and convert it to a mask
    roi = RoiPoly(color = 'r')
    mask = roi.get_mask(training_image[:, :, 0])

    # convert boolean mask to an array of unsigned ints
    mask_u8 = (mask.astype(np.uint8) * 255)

    # make the mask directory if it doesn't already exist
    mask_dir = mask_file.parent
    if not os.path.isdir(mask_dir):
        os.mkdir(mask_dir)
    
    # write mask binary image to file 
    plt.imsave(mask_file, mask_u8)


# for each file in my training set
for file_path in training_path.glob('*_6_dist305.png'):
    # get path metadata
    file_name = os.path.basename(file_path)
    train_idx = str(file_name).split('_')[1]
    str_dist_to_cone = str(file_name).split('_')[-1].replace("dist", "").replace(".png", "")
    int_dist_to_cone = int(str_dist_to_cone)

    # prepare where to save masks
    cone_folder = 'cone_masks'
    cone_file = (cwd / cone_folder / ('cone_' + 'train_' + train_idx + '_dist' + str_dist_to_cone + '.png')).resolve()

    extractROI("Cone", cone_file, file_path)

    # get 3 regions of the background that look similar in color to a cone or that could be tricky for my model
    for i in range(3):
        bkgd_folder = 'bkgd_masks'
        bkgd_file = (cwd / bkgd_folder / ('bkgd_' + 'train_' + train_idx + f'_{i}.png')).resolve()

        extractROI(f"Background {i}", bkgd_file, file_path)
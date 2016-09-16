# Emily Savela; Created 15 September 2016
# Lesson 40 implementing image processing functions

import numpy as np
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

# Import functions
import image_utils

# Load image data
phase_im_original = skimage.io.imread('data/bsub_100x_phase.tif')
phase_im = phase_im_original.copy()
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

# Remove hot pixels
phase_im_med = image_utils.med_filter(phase_im, mask_size=3)

# Gaussian Mask
phase_im_gauss = image_utils.gauss_mask(phase_im_med, blur_radius=50.0)

# Threshold the image
phase_im_thresh = image_utils.img_thresholding(phase_im_gauss)

# Remove too big and too small objects
im_bw_filt, num_object = image_utils.isolate_objects(phase_im_thresh, 130, 400)

# Display Figures
with sns.axes_style('dark'):
    fig, ax = plt.subplots(1, 2, figsize=(9.5, 8))
    ax[0].imshow(phase_im_original, cmap=plt.cm.viridis)
    ax[1].imshow(im_bw_filt, cmap=plt.cm.Greys_r)

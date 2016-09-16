# Emily Savela; Created 15 September 2016

"""Image utils: A collection of functions for Image Processing"""

import numpy as np
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

def seg_mask(image, mask, blur_radius):
    """
    Returns labeled, segmentation mask.
    Calls functions above to compute the complete segmentation.
    """
    # Create gaussian mask to correct for uneven illumination


def med_filter(image, mask_size=3):
    """
    Corrects for 'hot' or 'bad' pixels in an image.
    Then, corrects for uneven illumination by appling a gaussian blur
    """
    # Create median filter
    selem = skimage.morphology.square(mask_size)
    image_median = skimage.filters.median(image, selem)

    return image_median

def gauss_mask(image, blur_radius=50.0):
    # Create gaussian mask
    im_blur = skimage.filters.gaussian(image, blur_radius)
    image_float = skimage.img_as_float(image)
    image_gauss = image_float - im_blur

    return image_gauss


def img_thresholding(image):
    """
    Perform a thresholding operation on an image.
    """
    thresh_otsu = skimage.filters.threshold_otsu(image)
    image_bw = image < thresh_otsu

    return image_bw

# def rm_border_objects():
#     """
#     Remove bacteria or objects near/touching the image border.
#     """
#
#
# def isolate_bacteria():
#     """
#     Remove objects out of the size range of bacteria (too big or too small).
#     """
#
#
# def rm_improper_seg():
#     """
#     Removes improperly segmented cells.
#     """

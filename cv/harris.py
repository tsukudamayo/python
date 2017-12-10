#!/bin/usr/env python3
# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import filters

def compute_harris_response(im, sigma=3):
    """
    define functions which response harris corner
    about each pixels of gray scale image
    """

    # differencial coefficient
    imx = np.zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)
    imy = np.zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1,0), imy)

    # compute the components of the harris matrix
    Wxx = filters.gaussian_filter(imx*imx, sigma)
    Wxy = filters.gaussian_filter(imx*imy, sigma)
    Wyy = filters.gaussian_filter(imy*imy, sigma)

    # discriminat formula and diagonal componnt
    Wdat = Wxx*Wxy - Wxy**2
    Wtr = Wxx + Wyy

    return Wdat / Wtr


def get_harris_points(harrisim, min_dist=10, threshold=0.1):
    """
    return : corner from image
    min_dist : minimum number of pixels to separate from corners
               and image boundaries
    """
    # find a corner candidate that exceed the threshold
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1

    # get the candidate corner
    coords = np.array(harrisim_t.nonzero()).T

    # get the candidate values
    candidate_values = [harrisim[c[0], c[1]] for c in coords]

    # sort the cnaidate values
    index = np.argsort(candidate_values)

    # store the coordinates of the allowable points in the array
    allowed_locations = np.zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1

    # Gain the best point while considering the minmum distance
    filterd_coords = []
    for i in index:
        if allowed_locations[coords[i, 0], coords[i, 1]] == 1:
            filterd_coords.append(coords[i])
            allowed_locations[
                    (coords[i, 0]-min_dist):(coords[i, 0]+min_dist),
                    (coords[i, 1]-min_dist):(coords[i, 1]+min_dist)
            ] = 0

    return filterd_coords


def plot_harris_points(image, filterd_coords):
    """
    plot corner found in the image
    """
    plt.figure()
    plt.gray()
    plt.imshow(image)
    plt.plot(
            [p[1] for p in filterd_coords],
            [p[0] for p in filterd_coords],
            '*'
    )
    plt.axis('off')
    plt.show()


def get_descriptors(image, filterd_coords, wid=5):
    """
    return : neighbor pixcels of width 2*wid+1 around points for each points
             (assume the minimum distance min_distance > wid of points)
    """
    desc = []
    for coords in filterd_coords:
        patch = image[coords[0]-wid:coords[0]+wid+1,
                      coords[1]-wid:coords[1]+wid+1,].flatten()
        desc.append(patch)

    return desc


def match(desc1, desc2, threshold=0.5):
    """
    return : the correspoiding point of the second image is selected.
             Using the normalized cross-correlation,
             for each corner point descriptor of the first image,
    """
    n = len(desc1[0])

    # distance for each correspoinding point
    d = -np.ones((len(desc1), len(desc2)))
    for i in range(len(desc1)):
        for j in range(len(desc2)):
            d1 = (desc1[i] - np.mean(desc1[i])) / np.std(desc1[i])
            d2 = (desc2[j] - np.mean(desc2[j])) / np.std(desc2[j])
            ncc_value = np.sum(d1 * d2) / (n-1)
            if ncc_value > threshold:
                d[i, j] = ncc_value

    ndx = np.argsort(-d)
    matchscores = ndx[:, 0]

    return matchscores


def match_twosided(desc1, desc2, threshold=0.5):
    """
    when checking for a match in both directions
    """
    matches_12 = match(desc1, desc2, threshold)
    matches_21 = match(desc2, desc1, threshold)
    ndx_12 = np.where(matches_12 >= 0)[0]

    # remove asymmetric case
    for n in ndx_12:
        if matches_21[matches_12[n]] != n:
                matches_12[n] = -1

    return matches_12


def appendimages(im1, im2):
    """
    return : two images arrangd side by side
    """
    # choose the one with fewer rows and choose the blank with 0
    rows1 = im1.shape[0]
    rows2 = im2.shape[0]

    if rows1 < rows2:
        im1 = np.concatenate((im1.zeros(
            (rows2 - rows1, im1.shpae[1]))),axis=0)
    elif rows1 > rows2:
        im2 = np.concatenate((im2.zeros(
            (rows1 - rows2, im2.shape[1]))),axis=0)
    # if the lines are the same, you do not need to pad with 0

    return np.concatenate((im1, im2), axis=1)

def plot_matches(im1, im2, locs1, locs2,
                 matchscores, show_below=True):
    """
    connect corresponding points with lines to display image
    """
    im3 = appendimages(im1, im2)
    if show_below:
        im3 = np.vstack((im3, im3))

    plt.imshow(im3)

    cols1 = im1.shape[1]
    for i, m in enumerate(matchscores):
        if m>0:
            plt.plot([locs1[i][1], locs2[m][1]+cols1],
                     [locs1[i][0], locs2[m][0]], 'c'
            )
        plt.axis('off')


if __name__ == '__main__':
    # harris corner
    im = np.array(Image.open('empire.jpg').convert('L'))
    harrisim = compute_harris_response(im)
    filterd_coords = get_harris_points(harrisim, 6)
    plot_harris_points(im, filterd_coords)

    # match correspoding point from images
    im1 = np.array(Image.open('sf_view1.jpg').convert('L'))
    im2 = np.array(Image.open('sf_view2.jpg').convert('L'))
    wid = 5
    harrisim = compute_harris_response(im1, 5)
    filterd_coords1 = get_harris_points(harrisim, wid+1)
    d1 = get_descriptors(im1, filterd_coords1, wid)

    harrisim = compute_harris_response(im2, 5)
    filterd_coords2 = get_harris_points(harrisim, wid+1)
    d2 = get_descriptors(im2, filterd_coords2, wid)

    print('starting matching')
    matches = match_twosided(d1, d2)

    plt.figure()
    plt.gray()
    plot_matches(im1, im2, filterd_coords1, filterd_coords2, matches)
    plt.show()


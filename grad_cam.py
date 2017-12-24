#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from __future__ import print_function

from scipy.misc import imsave
import numpy as np
import time
from keras.applications import vgg16
from keras import backend as K


img_width = 128
img_height = 128

layer_name = 'block5_conv1'


def deprocess_image(x):
    # normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + K.epsilon())
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # convert to RGB array
    x *= 255
    if K.image_data_format() == 'channels_first':
        x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')

    return x


# build the VGG16 network with IMageNet weights
model = vgg16.VGG16(weights='imagenet', include_top=False)
print('Model loaded.')

model.summary()

# this is the placeholder for the inpute images
input_img = model.input

# get the symbolic outputs of the "key" layer (we gave them unique names)
layer_dict = dict([(layer.name, layer) for layer in model.layers[1:]])


def normalize(x):
    # utility functions to normalize a tensor by its L2 norm
    return x / (K.sqrt(K.mean(K.square(x))) + K.epsilon())


kept_filters = []
for filter_index in range(200):
    print('Processing filter %d' % filter_index)
    start_time = time.time()
    layer_output = layer_dict[layer_name].output

    # we build a loss function
    if K.image_data_format() == 'channels_first':
        loss = K.mean(layer_output[:, filter_index, :, :])
    else:
        loss = K.mean(layer_output[:, :, :, filter_index])

    grads = K.gradients(loss, input_img)[0]
    grads = normalize(grads)
    iterate = K.function([input_img], [loss, grads])
    step = 1.

    # we start from a gray image with some random noise
    if K.image_data_format() == 'channels_first':
        input_img_data = np.random.random((1, 3, img_width, img_height))
    else:
        input_img_data = np.random.random((1, img_width, img_height, 3))

    input_img_data = (input_img_data - 0.5) * 20 + 120

    # we run gradient ascent for 20 steps
    for i in range(20):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * step
        print('Current lass value', loss_value)

        if loss_value <= 0:
            break

    if loss_value > 0:
        img = deprocess_image(input_img_data[0])
        kept_filters.append((img, loss_value))

    end_time = time.time()
    print('FIlter %d processed in %ds' \
                %(filter_index, end_time - start_time))


# we will stich the best 64 filters on 8x8 grid
n = 8

# the filters that have the highest loss are assumed to better looking.
# we will only step the top 64 filters.
kept_filters.sort(key=lambda x: x[1], reverse=True)
kept_filters = kept_filters[:n * n]

# build a black picture with enough space for
# our 8x8 filters of size 128x128, with a 5px margin inn between
margin = 5
width = n * img_width + (n-1) * margin
height = n * img_height + (n-1) * margin
stiched_filters = np.zeros((width, height, 3))

# fill the picture with our saved filters
for i in range(n):
    for j in range(n):
        img, loss = kept_filters[i * n + j]
        stiched_filters[
    (img_width + margin) * i: (img_width + margin) * i + img_width,
    (img_height + margin) * j: (img_height + margin) * j + img_height, :] = img

# save the result to disk
imsave('stiched_filters_%dx%d.png' %(n, n), stiched_filters)

import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

# image size and number of classes
size_img = 28
n_label = 10

# dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train_img = x_train.reshape(
        -1, size_img, size_img, 1).astype('float32') / 255.
x_test_img = x_test.reshape(
        -1, size_img, size_img, 1).astype('float32') / 255.
y_train_label = np_utils.to_categorical(y_train, n_label)
y_test_label = np_utils.to_categorical(y_test, n_label)

# show image
i = 7
print('x_train:', x_train[i][:])
#print('x_train_img: ', x_train_img[i][:])
print('x_train_dim: ', x_train[i][:].shape)
print('x_train_img_dim: ', x_train_img[i][:].shape)
plt.imshow(np.array(x_train[i][:]), interpolation='nearest', cmap=cm.binary)
plt.show()
print('label:', y_train_label[i][:])

# define models
n_filter = 16
size_filter = 5
size_pool = 2
n_hidden = 100

model = Sequential()
model.add(Convolution2D(n_filter,
                        kernel_size=(size_filter),
                        strides=(1, 1),
                        padding='same',
                        data_format='channels_last',
                        input_shape=(size_img,size_img, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(size_pool, size_pool),
                       data_format='channels_last'))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(n_hidden))
model.add(Dropout(0.2))
model.add(Dense(n_label))
model.add(Activation('softmax'))

model.compile(
        loss='categorical_crossentropy',
        optimizer='Adam',
        metrics=['accuracy']
)

# train
model.fit(x_train_img,
          y_train_label,
          batch_size=50,
          epochs=1,
          verbose=1,
          validation_split=0.1
)

ev = model.evaluate(x_test_img, y_test_label)
print('\nAccuracy:\t%0.05f' % (ev)[1])
print('Confusion Matrix')
y_pred = model.predict_classes(x_test_img)
# @test(assert 1-dimension)
print('y_test: ', y_test)
# @test(assert 1-dimension)
print('y_pred: ', y_pred)
# @test(assert 1-dimension)
print('pred shape', y_pred.shape)
# @test(assert 1-dimension)
print('test shape', y_test.shape)
print(pd.crosstab(y_pred, y_test))

x_test_img_show = x_test.reshape(
        -1, 1, size_img, size_img).astype('float32') / 255.

# verify incorrect result of test
incorrect = [incorrect_img for incorrect_img in zip (x_test_img_show, y_pred, y_test) if incorrect_img[1] != incorrect_img[2]]
# print('incorrect_img', incorrect_img)
print('incorrect', incorrect)
print('number of incorrect result', len(incorrect))

# plot incorrect images and labels
plt.figure(figsize=(15,15))
fig_window_size = int(np.ceil(np.sqrt(len(incorrect))))
for idx, value in enumerate(incorrect):
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.subplot(fig_window_size, fig_window_size, idx+1)
    img = 1 - value[0][0]
    plt.axis('off')
    plt.imshow(img, cmap='gray')
    plt.text(8, 0, value[1], fontsize=14, color='red')
    plt.text(0, 0, value[2], fontsize=14, color='blue')
plt.show()


# plot weights of each layers
layers_list = model.layers
for idx, layer in enumerate(layers_list):
    print(idx+1, layer)
w1 = model.layers[0].get_weights()[0]
b1 = model.layers[0].get_weights()[1]
print('layer1 weight: ', w1.shape)
print('layer1 bias: ', b1.shape)
print('fully connected layer: ', model.layers[7].get_weights()[0].shape)

# layer1 filter
print('****** layer1 filter ******')
w1 = model.layers[0].get_weights()[0]
plt.figure(figsize=(16, 3.5))
for idx, value in enumerate(w1):
    print('idx: ', idx)
    print('value: ', value)
    plt.subplot(2, 8, idx+3)
    # XXX FIXME cannot reshape because arrays value is 80 
    img = value.reshape((size_filter, size_filter))
    plt.axis('off')
    plt.imshow(img, cmap='coolwarm', interpolation='nearest')
plt.show()

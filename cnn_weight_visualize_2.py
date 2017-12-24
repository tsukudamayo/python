import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as cm

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

# image size and number of classes
size_img = 28
n_label = 10

# dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(
        -1, 1, size_img, size_img).astype('float32')/255.
X_test = X_test.reshape(
        -1, 1, size_img, size_img).astype('float32')/255.
Y_train = np_utils.to_categorical(y_train, n_label)
Y_test = np_utils.to_categorical(y_test, n_label)


# model define
n_filter = 16
size_filter = 5
size_pool = 2
n_hidden = 100

model = Sequential()
model.add(Convolution2D(n_filter,
                        kernel_size=size_filter,
                        strides=(1,1),
                        padding='same',
                        data_format='channels_first',
                        input_shape=(1, size_img, size_img)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(size_pool, size_pool),
                       data_format='channels_first'))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(n_hidden))
model.add(Dropout(0.2))
model.add(Dense(n_label))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

# train
model.fit(X_train,
          Y_train,
          batch_size=50,
          epochs=1, 
          verbose=1,
          validation_split=0.1
)

# eval
vs = model.evaluate(X_test, Y_test)
print("\n Test Classification rate %0.05f" % vs[1])

# confusion_matrix
y_pred = model.predict_classes(X_test)

# visualize eval result
incorrect = [incorrect_img for incorrect_img in zip(X_test, y_pred, y_test) if incorrect_img[1] != incorrect_img[2]]
print(len(incorrect))

window_size = np.ceil(np.sqrt(len(incorrect)))
plt.figure(figsize=(15,15))
for idx, value in enumerate(incorrect):
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.subplot(window_size, window_size, idx+1)
    image = 1 - value[0][0]
    plt.axis('off')
    plt.imshow(image, cmap='gray')
    plt.text(8, 0, value[1], fontsize=14, color='red')
    plt.text(0, 0, value[2], fontsize=14, color='blue')
plt.show()

# get parameters each layers
layers_list = model.layers
for i, j in enumerate(layers_list):
    print(i+1, j)
w1 = model.layers[0].get_weights()[0]
b1 = model.layers[0].get_weights()[1]

print(w1.shape)
print(b1.shape)
print(model.layers[7].get_weights()[0].shape)
# do not transpose the tensor, you can not output the image 
w1  = w1.transpose(3, 2, 0, 1)
print(w1.shape)


# weights parameter visualization
#w1 = model.layers[0].get_weights()[0]
plt.figure(figsize=(16, 3.5))
for idx, value in enumerate(w1):
    plt.subplot(2, 8, idx+1)
    # XXX FIXME cannot reshape because arrays value is 80 
    image = value.reshape((size_filter, size_filter))
    plt.axis('off')
    plt.imshow(image, cmap='coolwarm', interpolation='nearest')
plt.show()

# a function that get the result as to whether or not the image has been correctly evaluated
def eval_collect_whether_or_not(num, fig_correct=True):
    if fig_correct:
        mask = (y_test == num) & (y_pred == y_test)
    else:
        mask = (y_test == num) & (y_pred != y_test)

    return X_test[mask], y_pred[mask]

# get layer2 (conv->relu)
layers=model.layers.copy()[:2]
model2 = Sequential()

for layer in layers:
    model2.add(layer)

model2.compile(loss='categorical_crossentropy',
               optimizer='RMSprop'
)


# visualize before fileterd and after filtered
num = 0
m = 5

# visualize filter
w1 = model2.layers[0].get_weights()[0]
print('model2 shape:', w1.shape)
w1 = w1.transpose(3, 2, 0, 1)
print('model2 shpae transpose:', w1.shape)
plt.figure(figsize=(16, 3.5))
for idx, value in enumerate(w1):
    plt.subplot(2, 8, idx+1)
    image = value.reshape(size_filter, size_filter)
    plt.axis('off')
    plt.imshow(image, cmap='coolwarm', interpolation='nearest')
plt.show()

# get correct image and incorrect image
image_correct, label_correct = eval_collect_whether_or_not(
        num, fig_correct=True
)
image_incorrect, label_incorrect = eval_collect_whether_or_not(
        num, fig_correct=False
)
print('image_correct', image_correct)
print('image_incorrect', image_incorrect)
print('label_correct', label_correct)
print('label_incorrect', label_incorrect)

# merge m items 
image_concat = np.concatenate([image_correct[:m], image_incorrect[:m]])
label_concat = np.concatenate([label_correct[:m], label_incorrect[:m]])

# get filtered images
filtered_images = model2.predict(image_concat)

# visualize
for x, num_pred, filtered_image in zip(image_concat, 
                                       label_concat, 
                                       filtered_images):
    plt.figure(figsize=(3, 3))
    plt.axis('off')
    plt.imshow(x[0], cmap='gray', interpolation='nearest')
    plt.text(0, -1, num, fontsize=14, color='blue')
    plt.text(8, -1, num_pred, fontsize=14, color='red')
    # filtered images
    plt.show()
    plt.figure(figsize=(16, 3.5))
    print('filtered image length:', len(filtered_image))
    for idx, image in enumerate(filtered_image):
        print('idx: ', idx)
        plt.subplot(2, 8, idx+1)
        plt.axis('off')
        plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.show()


# all
nums = range(10)
m = 3

for num in nums:
    # filter
    w1 = model2.layers[0].get_weights()[0]
    w1 = w1.transpose(3, 2, 0, 1)
    plt.figure(figsize=(16, 3.5))
    for idx, value in enumerate(w1):
        plt.subplot(2, 8, idx+1)
        image = value.reshape((size_filter, size_filter))
        plt.axis('off')
        plt.imshow(image, cmap='coolwarm', interpolation='nearest')
    plt.show()

    image_correct_10, label_correct_10 = eval_collect_whether_or_not(
            num, fig_correct=True
    )
    image_incorrect_10, label_incorrect_10 = eval_collect_whether_or_not(
            num, fig_correct=False
    )
    image_concat_10 = np.concatenate(
            [image_correct_10[:m], image_incorrect_10[:m]]
    )
    label_concat_10 = np.concatenate(
            [label_correct_10[:m], label_incorrect_10[:m]]
    )

    # get filtred images
    filtered_images = model2.predict(image_concat_10)

    # visualize
    for x, num_pred, filtered_image in zip(image_concat_10,
                                           label_concat_10,
                                           filtered_images):
        # before
        plt.figure(figsize=(3,3))
        plt.axis('off')
        plt.imshow(x[0], cmap='gray', interpolation='nearest')
        plt.text(0, -1, num, fontsize=14, color='blue')
        plt.text(8, -1, num_pred, fontsize=14, color='red')
        plt.show()

        # after
        plt.figure(figsize=(16,3.5))
        for idx, image in enumerate(filtered_image):
            plt.subplot(2, 8, idx+1)
            plt.axis('off')
            plt.imshow(image, cmap='gray', interpolation='nearest')
        plt.show()

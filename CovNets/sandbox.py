"""
@author: Nikunj Lad
Date: 04/02/2019

"""


import cv2
import numpy as np
import os, shutil
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

if os.path.isdir("./temp"):
    shutil.rmtree("./temp")

if not os.path.isdir("./temp"):
    os.makedirs(os.getcwd() + "/temp")

black = np.zeros((800,800,4), np.float32)

cv2.imwrite("./temp/image.png", black)
black = cv2.imread("./temp/image.png")
black = cv2.cvtColor(black, cv2.COLOR_BGR2RGBA)
plt.imshow(black)
plt.show()

print("hey:", black.shape)
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir('../data/dataset/images/leaves/acer_campestre')
data_dir = os.getcwd()
img = cv2.imread(data_dir + "/acer_campestre1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
print(data_dir)
print(black.shape)
print(img.shape)
# cv2.imshow("img2", img)
plt.imshow(img)
plt.show()
print(type(img))
print(type(black))

# # Read the images
# foreground = cv2.imread("puppets.png")
# background = cv2.imread("ocean.png")
# alpha = cv2.imread("puppets_alpha.png")
#
# # Convert uint8 to float
# foreground = foreground.astype(float)
# background = background.astype(float)
#
# # Normalize the alpha mask to keep intensity between 0 and 1
# alpha = alpha.astype(float) / 255
#
# # Multiply the foreground with the alpha matte
# foreground = cv2.multiply(alpha, foreground)
#
# # Multiply the background with ( 1 - alpha )
# background = cv2.multiply(1.0 - alpha, background)
#
# # Add the masked foreground and background.
# outImage = cv2.add(foreground, background)
#
# # Display image
# cv2.imshow("outImg", outImage / 255)
# cv2.waitKey(0)

h = int(800 / 2) - int(img.shape[0] / 2)
black[h:h + img.shape[0],0:0 + img.shape[1]] = img
# cv2.imshow("img3", black)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
plt.imshow(black)
plt.show()


"""
******************************** BARE MINIMUM TENSORFLOW IMPLEMENTATION ********************************************

import os
import logging
import tensorflow as tf
import pathlib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.enable_eager_execution()
tf.VERSION

categories = ['A', 'B']
Img_Size = [100, 100]

# Image Parameters
N_CLASSES = 185  # CHANGE HERE, total number of classes
IMG_HEIGHT = 64  # CHANGE HERE, the image height to be resized to
IMG_WIDTH = 64  # CHANGE HERE, the image width to be resized to
CHANNELS = 3  # The 3 color channels, change to 1 if grayscale

sess = tf.InteractiveSession()
initializer = tf.global_variables_initializer()


def create_data(file_path, mode):
    img_path, labels = list(), list()

    if mode == "file":
        pass
    elif mode == "folder":

        # initially the labels are kept as 0, we will increment them as and when more classes data is read
        label = 0

        # read all the directory names by walking over the root directory and store the names in the classes file as a list
        try:
            classes = sorted(os.walk(file_path).__next__()[1])
        except Exception as e:
            logging.log(e)
            print(e)
            print("Error reading the classes")

        for leafs in classes:

            # once a leaf directory is encountered, append it's name to the root path so as to access its images
            leaf_dir = os.path.join(file_path, leafs)

            try:
                walk = os.walk(leaf_dir).__next__()
            except Exception as e:
                logging.log(e)
                print(e)
                print("Error reading the images from the individual folders")

            for img in walk[2]:

                if img.endswith("jpg") or img.endswith("jpeg") or img.endswith("png"):
                    img_path.append(os.path.join(leaf_dir, img))
                    labels.append(label)

            label += 1
    else:
        raise Exception("Unknown mode!")

    # convert image path inputs to tensors
    imagepaths = tf.convert_to_tensor(img_path, dtype=tf.string)
    labels = tf.convert_to_tensor(labels, dtype=tf.int32)

    # Build a TF Queue, shuffle data
    # image, label = tf.train.slice_input_producer([imagepaths, labels], shuffle=True)

    # Build a TF Queue and shuffle data, another method since above one is deprecated
    tensor_list = [imagepaths, labels]
    dataset = tf.data.Dataset.from_tensor_slices(tuple(tensor_list)).shuffle(tf.shape(imagepaths, out_type=tf.int64)[0])
    image, label = dataset.output_classes

    # sess.run(image)
    # # Read images from disk
    image = tf.read_file(image)
    image = tf.image.decode_jpeg(image, channels=CHANNELS)
    #
    # # Resize images to a common size
    # image = tf.image.resize_images(image, [IMG_HEIGHT, IMG_WIDTH])
    #
    # # Normalize
    # image = image * 1.0 / 127.5 - 1.0
    #
    # # Create batches
    # X, Y = tf.train.batch([image, label], batch_size=batch_size,
    #                       capacity=batch_size * 8,
    #                       num_threads=4)
    #
    # 
    # Citations: Python documentation was referred for understanding directory traversing using os
    # :param filename: the current filename - in this case it point to this file -> signs1.py
    # :return: current direcotory, train data and test data directory paths
    # 
    # current_dir = os.path.dirname(os.path.abspath(filename))
    # os.chdir('../data')
    # data_dir = os.getcwd()
    # train_data_dir = data_dir + '/asl_alphabet_train/'
    # test_data_dir = data_dir + '/asl_alphabet_test/'

    # return current_dir, train_data_dir, test_data_dir
    sess.close()


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir('../data/dataset/images/leaves')
data_dir = os.getcwd()
print(data_dir)
create_data(data_dir, "folder")

************************************************************************************************************************
"""

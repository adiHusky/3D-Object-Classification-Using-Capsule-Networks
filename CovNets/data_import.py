"""
Copyright (c) 2018 Nikunj Lad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""

import tensorflow as tf
import pathlib as p
import random, os, cv2, shutil
from processing import *

# disabling warning and enabling eager execution to avoid mapping things on tensorflow graphs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.enable_eager_execution()
print(tf.VERSION)


# this class contains various helper functions to acquire data for training
# various cases are handled and determined by modes. further these modes can be segmented into functions based on
# more cases coming in.
#
# CASES:
# mode 1 = directory containing various sub-directories. Each sub-directory is a class label with images in it.
# mode 2 = a directory containing various images of all classes and not segregated properly
#

class DataImport:
    """
    DataImport Class contains functions to import data in the right format from any given file type or hierarchical
    structure.

    various cases to tackle
    CASE 1: Training and Testing folders seperate, each folder has multiple sub folders corresponding to 1 class. Each
    sub folder representing 1 class has many images. All images of the same size.

    CASE 2: Training and Testing folders seperate, each folder has multiple sub folders corresponding to 1 class. Each
    sub folder representing 1 class has many images. All images of the different sizes.

    CASE 3: data folder contains many folders each representing a class and each class consisting of many images. Data
    not divided into training and testing here and all images are of the same size.

    CASE 4: data folder contains many folders each representing a class and each class consisting of many images. Data
    not divided into training and testing here and all images are of the different sizes.

    CASE 5: All images randomly of the same size but not segregated by folders or seperated into training or testing.

    CASE 6: All images randomly of the different sizes but not segregated by folders or seperated into training or 4
    testing.

    Functions used:
    1. Get image data from folders
    2. Create training data
    3. Create testing data
    4. Get directory paths and information.
    
    """

    def __init__(self, filename):

        self.filename = filename
        self.train_matrix = list()
        self.train_labels = list()
        self.test_matrix = list()
        self.test_labels = list()
        self.process = Processing()

    def image_data_from_folders(self, parent_path, data_path, temp_path):

        # 1. Retrieving images from the image directory
        # print(path)             # print incoming paths
        data_dir = p.Path(data_path)  # convert os path to pathlib path for working with file and folder traversing
        print("Pathlib path: ", data_dir)  # print the type of pathlib object generated

        # get all the image paths in posixPath format from the image directory and append them in a list
        all_image_paths = list(data_dir.glob('*/*'))
        all_image_paths = [str(path) for path in all_image_paths]  # convert them to a string format

        # random.shuffle(all_image_paths)  # randomly shuffle the image paths

        # 2. Generating list of labels
        label_names = sorted(item.name for item in data_dir.glob('*/') if item.is_dir())
        print(label_names)

        # resizing images
        resize_height = 320
        resize_width = 320
        fit_style = "square"

        resized_images = list()
        if isinstance(all_image_paths, list):
            os.chdir(parent_path)

            if os.path.isdir("processed"):
                shutil.rmtree("processed")

            if not os.path.isdir("processed"):
                os.makedirs(os.getcwd() + "/processed")

            os.chdir("processed")
            proc_dir = os.getcwd()
            for image in all_image_paths:
                resized = self.process.image_resize_with_aspect(resize_height, resize_width, image, fit_style, temp_path, debug=False)

                label = image.split('/')[-2]
                if not os.path.isdir(label):
                    os.makedirs(proc_dir + "/" + label)

                save_path = proc_dir + "/" + label + "/" + image.split('/')[-1].split(".")[0] + ".png"
                cv2.imwrite(save_path, cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))
                resized_images.append(save_path)

        print("Current path after processing: ", os.getcwd())

        """
        Logic to create seperate folder and split data into training and testing folders. Training folder has all the 
        classes folder and about 80-90% data while testing folder will have all the folders of all classes but with 
        about 10-20% data.
        """

    def create_training_data(self, categories, train_data_dir, colormap):

        for index1, Category in enumerate(categories):
            path = os.path.join(train_data_dir, Category)  # path to cats or dogs Category

            for img in os.listdir(path):
                try:
                    # reading the image in gray scale mode and resizing it
                    image = self.process.read_image(os.path.join(path, img), colormap)

                    self.train_matrix.append(image)
                    self.train_labels.append(index1)
                except Exception as e:
                    pass

        return self.train_matrix, self.train_labels

    def create_testing_data(self, categories, test_data_dir, colormap):

        for index2, Category in enumerate(categories):
            path = os.path.join(test_data_dir, Category)  # path to cats or dogs Category

            for img in os.listdir(path):
                try:
                    image = self.process.read_image(os.path.join(path, img), colormap)

                    self.test_matrix.append(image)
                    self.test_labels.append(index2)
                except Exception as e:
                    print(e)
                    pass

        return self.test_matrix, self.test_labels

    def data_dirs(self):
        """
        :param filename: the current filename - in this case it point to this file -> signs1.py
        :return: current direcotory, train data and test data directory paths
        """
        current_dir = os.path.dirname(os.path.abspath(self.filename))
        os.chdir('../data/dataset/images/processed')
        data_dir = os.getcwd()
        train_data_dir = data_dir + '/asl_alphabet_train/'
        test_data_dir = data_dir + '/asl_alphabet_test/'

        return current_dir, train_data_dir, test_data_dir

    """
    logic to seperate the images from processed folder to train and test folders each having all the classes
    and data associated with it. At the end this function should return the parent folder path (containing train
    and test folders -> each train and test folders will contain class folders containing images therein. 
    function should also train and test dir paths and labels list
    
    input:
    image path
    temp path
    fit_style
    resize_height
    resize_width
    debug status
    color space
    
    return:
    class labels
    parent dir path
    train dir path (sub to parent)
    test dir path (sub to parent)
    
    """

    """
    *************** TO BE USED FOR TENSORFLOW ******************************************************************
    *
    *
    # # counting total number of images
    # image_count = len(resized_images)
    # print("Total number of images:", image_count)
    # 
    # # mapping labels with index in the array
    # label_to_index = dict((name, index) for index, name in enumerate(label_names))
    # print(label_to_index)
    # 
    # all_image_labels = [label_to_index[p.Path(path).parent.name]
    #                     for path in resized_images]
    # 
    # print("First 10 labels indices: ", all_image_labels[:10])
    # 
    # # 3. Load and process the images
    # img_path = all_image_paths[9]
    # print(img_path)
    # 
    # img_raw = tf.read_file(img_path)
    # 
    # # decode the image. provide the image, channels, datatype
    # img_tensor = tf.image.decode_image(contents=img_raw, dtype=tf.dtypes.float32)
    # 
    # print(img_tensor.dtype)
    *
    *
    ************************************************************************************************************
    """


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)
    os.chdir("../data/dataset/images")
    parent_dir_path = os.getcwd()
    os.chdir('../data/dataset/images/leaves')
    data_dir_path = os.getcwd()
    os.chdir("../")
    print(os.getcwd())

    if os.path.isdir("./temp"):
        shutil.rmtree("./temp")

    if not os.path.isdir("./temp"):
        os.makedirs(os.getcwd() + "/temp")

    os.chdir('temp')
    temp_dir = os.getcwd()
    print("parent dir:", parent_dir_path)
    print("data dir:", data_dir_path)
    di = DataImport(__file__)
    di.image_data_from_folders(parent_dir_path, data_dir_path, temp_dir)

# read folder of images

# first preprocess in high resolution, apply filters , normalize etc

# read all images and resize it maintaining aspect ratio

# save them with the same name as before in new directory hierarchy same as before and then read them again while
# training

# this newly created folder should not be deleted since it is going to be used time and again for multiple training
# sessions

# temp folder hierarchy should be maintained for saving plots, graphs and charts which may needs to be deleted after
# each run

# do logging for better tracing of errors and issues, try doing issue tracking

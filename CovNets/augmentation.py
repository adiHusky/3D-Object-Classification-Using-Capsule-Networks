from keras.utils import to_categorical, np_utils
import numpy as np


class Augmentation:
    """
    Augmentation class contains functions used to augment our image data
    Some functions include

    1. creating NumPy data
    2. Do one hot encoding
    3. Do one hot decoding (remaining to be done)
    4. Data reshaping

    """

    def __init__(self):
        pass

    @staticmethod
    def create_numpy_data(data):
        numpy_data = np.array(data)
        return numpy_data

    @staticmethod
    def do_one_hot_encoding(just_labels):
        one_hot_encoded_labels = to_categorical(just_labels)

        return one_hot_encoded_labels

    @staticmethod
    def one_hot_encode_labels(y_train, y_test):
        """

        :return: returns one hot encoded values of labels. One hot encoding helps in converting multi-categorical labels
        into a vector of 1's and 0's
        """
        # one hot encode outputs
        y_train = np_utils.to_categorical(y_train)
        y_test = np_utils.to_categorical(y_test)

        return y_train, y_test

    @staticmethod
    def data_reshape(data, labels, colormap, image_depth):
        images = data

        # Find the unique numbers from the train labels
        classes = np.unique(labels)
        n_classes = len(classes)
        print('Total number of outputs : ', n_classes)
        print('Output classes : ', classes)

        if "GRAY" in colormap:
            n_rows, n_cols = images.shape[1:]
            depth = 1
        else:
            n_rows, n_cols, depth = images.shape[1:]

        print(n_rows, n_cols, images.shape[0], depth)
        images = images.reshape(images.shape[0], n_rows, n_cols, image_depth)
        input_shape = (n_rows, n_cols, image_depth)

        return input_shape, images, classes, n_classes

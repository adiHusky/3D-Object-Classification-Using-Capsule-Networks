
import matplotlib.pyplot as plt
import cv2
import numpy as np


class Processing:
    """
    Processing class contains functions for for performing image processing

    Functions include:
    1. Display image
    2. Read Image
    3. Image Resize with Aspect Ratio
    4. Resize images (wrapper function for above function)
    5. Change image datatype
    6. Normalize Images

    """

    def __init__(self):

        pass

    # function to display image
    @staticmethod
    def display_image(image):
        plt.imshow(image)
        plt.show()

    @staticmethod
    def read_image(image_path, color_space=None):

        color_map = {'BGR2RGBA': cv2.COLOR_BGR2RGBA,
                     'BGR2GRAY': cv2.COLOR_BGR2GRAY,
                     'BGR2RGB': cv2.COLOR_BGR2RGB,
                     'BGR2BGRA': cv2.COLOR_BGR2BGRA,
                     'ORIGINAL': cv2.IMREAD_COLOR
                     }

        # read the input image and convert it from BGR to BGRA
        img = cv2.imread(image_path, color_map['ORIGINAL'])  # read the color image

        if color_space != 'ORIGINAL':
            # convert from 3 channel BGR to RGBA taking into consideration alpha
            img = cv2.cvtColor(img, color_map[color_space])

        return img

    @staticmethod
    def image_resize_with_aspect(height, width, img_path, fit_style, temp_path, color_map, padding=True, debug=False):

        if isinstance(img_path, np.ndarray):
            img = img_path
        else:
            img = Processing.read_image(img_path, color_map)

        if debug:
            Processing.display_image(img)

        # get the shape of the image
        if "GRAY" in color_map:
            img_h, img_w = img.shape
            depth = 1
        else:
            img_h, img_w, depth = img.shape  # returns (height, width, depth)

        # find the aspect ratio of the actual image and the desired image
        image_aspect = float(img_w / img_h)
        desired_aspect = float(width / height)
        print("original image height, width and depth:", img_h, img_w, depth)

        # resizing the image maintaining the aspect ratio. This is a function to resize it to a square
        if fit_style == "square":

            if image_aspect > desired_aspect:
                img_h = int(width / image_aspect)
                img_w = width
            elif image_aspect < desired_aspect:
                img_w = int(height * image_aspect)
                img_h = height
            else:
                img_w = width
                img_h = height

        print("new width and height: ", img_w, img_h)

        # resizing the image and displaying it.
        new_img = cv2.resize(img, (int(img_w), int(img_h)), interpolation=cv2.INTER_AREA)
        if debug:
            Processing.display_image(new_img)

        if padding is not None:
            # TIP: 0, 1 and border extension logic
            # create a black image using numpy and the alpha channel
            black = np.ones((height, width, 4), np.float32) * 255
            cv2.imwrite(temp_path + "/image.png", black)
            black_img = Processing.read_image(temp_path + "/image.png", color_map)

            # based on the resized image shapes, paste the original image on the black canvas with relevant offsets
            if img_w == width:
                mid_y = int(height / 2) - int(img_h / 2)
                black_img[mid_y:mid_y + img_h, :] = new_img
            elif img_h == height:
                mid_x = int(width / 2) - int(img_w / 2)
                black_img[:, mid_x:mid_x + img_w] = new_img
            else:
                black_img = new_img
        else:
            black_img = new_img

        if debug:
            Processing.display_image(black_img)

        return black_img

    @staticmethod
    def resize_images(x_size, y_size, image, colormap, temp_path):

        if isinstance(image, list):
            image_matrix = list()
            for img in image:
                resized_image = Processing.image_resize_with_aspect(y_size, x_size, img, "square", temp_path, colormap,
                                                                    False, False)
                # resized_image = cv2.resize(img, (x_size, y_size))
                image_matrix.append(resized_image)
            return image_matrix
        else:
            resized_image = Processing.image_resize_with_aspect(y_size, x_size, image, "square", temp_path, colormap,
                                                                False, False)
            return resized_image

    @staticmethod
    def change_datatype(data, dataType):
        new_data = data.astype(dataType)
        return new_data

    @staticmethod
    def scale_images(data, factor):
        data = data / factor
        return data

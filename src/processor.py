import cv2
import numpy as np
import os

# utility class meant to be used internally
class helper:
    _supported_types = ()
    def __init__(self):
        self._supported_types = ('.jpg', '.png')

    def supported_types(self):
        return self._supported_types

    def get_images_in_dir(self, folder_path):
        filepaths = []
        extensions = self._supported_types
        for filename_str in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename_str)) and filename_str.lower().endswith(extensions):
                filepaths.append(folder_path + '/' + filename_str)
        return filepaths
    
# wraps an OpenCV image object returned by cv2.imread()
class image_file:
    filepath = ""
    _image = None
    _helper = helper()

    def __init__(self, filepath = ""):
        if os.path.isfile(filepath) and filepath.lower().endswith(self._helper._supported_types):
            self._image = cv2.imread(filepath)
            self.filepath = filepath
        else:
            # The data is assumed to be set later if filepath is left empty
            if not filepath == "":
                 print("File at " + filepath + " could not be loaded.")

    def get_image(self):
        if self._image is None:
            print("Tried to call image_file.get() without an image being loaded!")
        return self._image
    
    def set_image(self, image_data, filepath = ""):
        self._image = image_data
        if not filepath == self.filepath:
            self.filepath = filepath
    
    def write(self, outpath):
        result = cv2.imwrite(outpath, self._image)
        if not result:
            print("Could not save file: " + outpath + ". No image data to write or issue with filepath?")
        if not self.filepath == outpath:
             self.filepath = outpath

# contains public API definitions for various image manipulation functions
def flip_image(image, flip_code):
        result_image = image_file()
        result_image.set_image(cv2.flip(image.get_image(), flip_code), "")

        return result_image
    
def scale_image(image, ratio):
        width = int(image.get_image().shape[1] * ratio)
        height = int (image.get_image().shape[0] * ratio)
        
        result_image = image_file()
        result_image.set_image(cv2.resize(image.get_image(), (width, height)), "")

        return result_image
    
def rotate_image(image, angle):
        height, width = image.get_image().shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        
        result_image = image_file()
        result_image.set_image(cv2.warpAffine(image.get_image(), rotation_matrix, (width, height)), "")

        return result_image

def add_gaussian_noise(image, mean, std_dev):
    image_data = image.get_image()
    noise = np.random.normal(mean, std_dev, image_data.shape).astype(np.uint8)
    noisy_image = cv2.add(image_data, noise)

    result_image = image_file()
    result_image.set_image(noisy_image)

    return result_image

def sharpen_image(image):
    image_data = image.get_image()
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image_data, -1, kernel)

    result_image = image_file()
    result_image.set_image(sharpened_image)

    return result_image


"""

import cv2
import random
import time
import os
import tensorflow as tf
import numpy as np
from keras.models import load_model
from matplotlib import pyplot as plt


# import the file Threshold_Values to use its functions
import Threshold_Values

# Prepare the Model
new_model = load_model('models/fireDetector.h5')

threshold_values_list = []  # => [temp,humidity,{1 if above threshold . otherwise 0} , image name]


def Start_Sensing():
    i = 0  # counter for knowing the number of rounds
    # Start the process
    while True:
        print("-----------------------------------------------")
        print("round {}".format(i + 1))
        print("-----------------------------------------------")
        # getting the result from the function thresholdForFire()
        threshold_values_list = Threshold_Values.thresholdForFire()

        print("List is {} ".format(threshold_values_list))

        # Check Values
        if threshold_values_list[2] == 1:
            # print("Temp {}".format(threshold_values_list[0]))
            # print("Humidity {}".format(threshold_values_list[1]))
            # print("result {}".format(threshold_values_list[2]))
            # Open Camera
            camera = cv2.VideoCapture(0)
            success, frame = camera.read()
            # save the image
            cv2.imwrite(
                "static/images/FireTest.jpg",
                frame)
            # close the camera
            camera.release()

            # Use the Model the classify the Camera
            img = cv2.imread("static/images/FireTest.jpg")

            imagename = "FireTest"
            imagename = imagename + ".jpg"
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            resize = tf.image.resize(img2, (256, 256))

            # Passing the image to the model and save the result in predict variable
            predict = new_model.predict(np.expand_dims(resize / 255, 0))
            # Printing thr result
            print(predict)
            if predict > 0.5:
                print(f'There is No Fire')
                threshold_values_list[2] = 0
                threshold_values_list.append(imagename)
            else:
                threshold_values_list[2] = 1
                threshold_values_list.append(imagename)
                print(f'Fire Detected :) !')

        # clearing the list
        threshold_values_list.clear()


if __name__ == "__main__":
    Start_Sensing()

"""
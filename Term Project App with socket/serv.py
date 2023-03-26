import socket
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

#IP = "127.0.0.1"

IP = "192.168.0.105"
PORT = 8047

# Create a socket and bind it to the IP and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))

# Listen for incoming connections
server_socket.listen()
print("Server Listening >> ")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()


print(f"[+] Connection from {client_address} has been established.")

print("--------------------------------------------------------")


fire_detection_flag = 0
list_of_values = []

print("Loading the model .....")
new_model = load_model('models/fireDetector.h5')

while True :

    # number  or image or fire flag
    client_request = client_socket.recv(1024).decode()


    if client_request == "image":
        print("from client received >> {} request ".format(client_request))

        # Take a picture using the default camera
        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        cap.release()

        # Encode the image as JPEG and send it to the client
        _, img_encoded = cv2.imencode('.jpg', frame)
        client_socket.sendall(img_encoded.tobytes())

        #Save the image
        cv2.imwrite(
            "Serverimages/FireTest.jpg",
            frame)

    elif client_request == "number":
        print("from client received >> {} request ".format(client_request))
        # get the values
        list_of_values = Threshold_Values.thresholdForFire()



        # [hum,temp,above_or_not]
        hum = str(list_of_values[0])
        temp = str(list_of_values[1])
        above_threshold = str(list_of_values[2])
        #above_threshold = str(0)




        #Now prepare the values in one string

        Values_for_client = hum + ";" + temp + ";" + above_threshold

        print("Threshold Values >>" , Values_for_client)

        # send the threshold values
        client_socket.send(Values_for_client.encode())

    elif client_request == "fireflag":
        print("from client received >> {} request ".format(client_request))

        # Read the image
        img = cv2.imread("Serverimages/FireTest.jpg")

        # prepare the image for the model
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resize = tf.image.resize(img2, (256, 256))

        # Passing the image to the model and save the result in predict variable
        predict = new_model.predict(np.expand_dims(resize / 255, 0))

        # Printing thr result
        if predict > 0.5:
            print("Non fire")
            fire_detection_flag = 0
        else:
            print("fire")
            fire_detection_flag = 1


        fireflag_encoded = str(fire_detection_flag)
        fireflag_encoded = fireflag_encoded.encode()

        print("Fire flag encoded >> ", fireflag_encoded)
        client_socket.send(fireflag_encoded)

    else:
        pass


# Close the sockets

client_socket.close()
server_socket.close()

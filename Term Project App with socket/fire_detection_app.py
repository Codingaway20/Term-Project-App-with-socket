
from flask import Flask, render_template, redirect, jsonify, url_for
import numpy as np
import random
from socket import *
import cv2
# __name__ referring local python file that you are working on
app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 7000


@app.route('/')
def initial():
    return redirect('/main')

@app.route('/main')
def home_page():
    return render_template('main.html')


@app.route('/start_sensing')
def makeCommunication():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    return redirect(url_for("information_page"))



# first data is image name. The image will be send here when fire is detected.
# image_name - fire notification
# Data Order: fire_notification - sensor_id - raspberrypi_id - location - temperature - humidity - light
random_decimals = []

list_of_values = []
fire_flag = -1

image_name = "FireTest.jpg"


@app.route('/update_decimal', methods=['POST'])
def updatedecimal():


    #send number
    s.send("number".encode())
    list_of_values = (s.recv(1024).decode()).split(";")



    # If above threshold
    if int(list_of_values[2]) == 1:
        # request image
        s.send("image".encode())

        # Receive the image from the server and decode it
        img_encoded = s.recv(9000000)
        img_decoded = cv2.imdecode(np.frombuffer(img_encoded, np.uint8), -1)
        # Save the image to the disk
        cv2.imwrite("static/images/FireTest.jpg", img_decoded)

        # request fire flag
        s.send("fireflag".encode())
        fire_flag_string = s.recv(1024).decode()
        fire_flag = int(fire_flag_string)

    else:
        fire_flag = 0



    # the data coming from server as a string.
    # I convert them to integer in order to send it correctly to javascript
    random_decimal = int(list_of_values[0]) # temp
    random_decimal2 = int(list_of_values[1]) # humidity
    random_decimal3 = 33 # light
    random_decimal4 = round(np.random.rand()+23, 2)
    random_decimal5 = round(np.random.rand()+77, 2)
    random_decimal6 = round(np.random.rand()+69, 2)
    random_decimal7 = round(np.random.rand()+30, 2)
    random_decimal8 = round(np.random.rand()+43, 2)
    random_decimal9 = round(np.random.rand()+55, 2)
    random_decimal10 = round(np.random.rand()+23, 2)
    random_decimal11 = round(np.random.rand()+77, 2)
    random_decimal12 = round(np.random.rand()+69, 2)
    random_decimal13 = round(np.random.rand()+30, 2)
    random_decimal14 = round(np.random.rand()+43, 2)
    random_decimal15 = round(np.random.rand()+55, 2)
    random_decimal16 = round(np.random.rand()+23, 2)
    random_decimal17 = round(np.random.rand()+77, 2)
    random_decimal18 = round(np.random.rand()+69, 2)

    images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg", "image8.jpg", "image9.jpg",
              "image10.jpg", "image11.jpg", "image12.jpg", "image13.jpg", "image14.jpg", "image15.jpg", "image16.jpg", "image17.jpg", "image18.jpg"]

    image_number = random.randint(0, 17)

    fire_notification = [fire_flag, 0, 0]

    fire_notification_str = ""
    for i in fire_notification:
        fire_notification_str += str(i) + ";"
    fire_notification_str = fire_notification_str[:-1]

    received_image_data = ["FireTest.jpg",
                           images[image_number], images[image_number]]
    fire_images_str = ""
    for i in received_image_data:
        fire_images_str += i + ";"
    fire_images_str = fire_images_str[:-1]

    random_decimals = [fire_images_str, [fire_notification_str],
                       1, 1, "Kalkanli", random_decimal, random_decimal2, random_decimal3,
                       2, 1, "Kalkanli", random_decimal4, random_decimal5, random_decimal6,
                       1, 2, "Kutahya", random_decimal7, random_decimal8, random_decimal9,
                       2, 2, "Kutahya", random_decimal10, random_decimal11, random_decimal12,
                       1, 3, "Kyrenia", random_decimal13, random_decimal14, random_decimal15,
                       2, 3, "Kyrenia", random_decimal16, random_decimal17, random_decimal18]

    for i in range(0, len(random_decimals)-2):
        if (i % 6 == 0):
            sensor_id = random_decimals[i+2]
        elif (i % 6 == 1):
            rasp_id = random_decimals[i+2]
        elif (i % 6 == 3):
            index1 = i+2
        elif (i % 6 == 4):
            index2 = i+2
        elif (i % 6 == 5):
            index3 = i+2
            saveFile(random_decimals, rasp_id,
                     sensor_id, index1, index2, index3)

    return jsonify('', render_template('random_decimal_model.html', x=random_decimals))


@app.route('/information')
def information_page():
    return render_template('information.html', x=random_decimals)

@app.route('/stop_sensing')
def stop_sensing():
    s.send("!DISCONNECT".encode())
    return redirect(url_for("home_page"))

@app.route('/fire_image')
def display_image_page():
    return render_template('display_image.html', x=random_decimals)

def saveFile(random_decimals, rasp_id, sensor_id, index1, index2, index3):
    filename = "raspberrypi_" + \
        str(rasp_id) + "_sensor_" + str(sensor_id) + ".txt"

    file = open(filename, "a")

    line = str(random_decimals[index1]) + (9-len(str(random_decimals[index1]))) * " " + str(
        random_decimals[index2]) + (9-len(str(random_decimals[index2]))) * " " + str(random_decimals[index3]) + (9-len(str(random_decimals[index3]))) * " " + "\n"
    file.writelines(line)

    file.close()

app.run(debug=True)

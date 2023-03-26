#!C:\Users\iiha7\anaconda3\python.exe
import time
from socket import *
import cv2
import numpy as np
import threading as thread
import sched
import schedule



HOST="192.168.0.105"
PORT=8047
j=0
clientSocket= socket(AF_INET,SOCK_STREAM)
clientSocket.connect((HOST,PORT))


def printHeader(title):
    print(("Content-type: text/html"))
    print("")
    print("<html><head><title>{}</title>".format(title))
    print("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous>")
    print("<script src='https://code.jquery.com/jquery-3.5.1.slim.min.js' integrity='sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj' crossorigin='anonymous'></script>")
    print("<script src='https://cdn.jsdelivr.net/npm/[email protected]/dist/js/bootstrap.bundle.min.js' integrity='sha384-LtrjvnR4Twt/qOuYxE721u19sVFLVSA4hf/rRt6PrZTmiPltdZcI7q7PXQBYTKyf' crossorigin='anonymous'></script>")
    print("<script src='show.js'>")
    print("</script>")
    print("</head><body>")

def printFooter():
    print("</body></html>")


def generateDate():
    return time.strftime("%X")


def tableCreation():

    global clientSocket
    global new_model

    date=generateDate()
    #;

    isThereFire=0
    temperature=1
    humidity=2
    light=3
    firePrediction="Picture not taken!"
    img=""
    fireFlagStr ="Picture not taken!"
    fire_detection_flag=0


    clientSocket.send("number".encode())
    listOfValues=(clientSocket.recv(1024).decode()).split(";")

    if(listOfValues[2] == "1"):
        clientSocket.send("image".encode())
        image=clientSocket.recv(9000000)
        image=cv2.imdecode(np.frombuffer(image,np.uint8),-1)
        cv2.imwrite("fireImages/FireTest.jpg",image)
    
        clientSocket.send("fireflag".encode())
        fireFlagStr=clientSocket.recv(1024).decode()


    temperature=int(listOfValues[0])
    humidity=int(listOfValues[1])
    

    img=""

    if fireFlagStr=="0":
        img="fireImages/nofire.png"
        firePrediction="NoFire!"
        
    elif fireFlagStr =="1":
        img="fireImages/FireTest.jpg"
        firePrediction="FireDetected!"

    else:
        img="fireImages/nofire.png"
        firePrediction="PictureNotTaken!"

    rpid1=1
    sid1=1

    rpid2=2
    sid2=3



    

    newLine=str(rpid1)+" "+str(sid1)+" "+str(temperature)+" "+str(humidity)+" "+str(light)+" "+str(date)+" "+str(firePrediction)
    newLine1=str(rpid2)+" "+str(sid2)+" "+str(temperature)+" "+str(humidity)+" "+str(light)+" "+str(date)+" "+str(firePrediction)

    with open("data.txt","a") as file:
        file.write(newLine+"\n")
        file.write(newLine1+"\n")

        
    
    print("<div class='d-flex justify-content-center'>")
    print("<table id='table' class='table table-striped' style='display:block'>")
    print("<thead>")
    print("<tr>")
    print("<th>Raspberry Pi Id</th>")
    print("<th>Sensor Id</th>")
    print("<th>Temperature</th>")
    print("<th>Humditiy</th>")
    print("<th>Light</th>")
    print("<th>Sensed Time</th>")
    print("<th>Prediction</th>")
    print("<th>Picture</th>")
    print("</tr>")
    print("</thead>")
    print("<tbody>")
    print("<tr>")
    print("<td>{}</td>".format(rpid1))
    print("<td>{}</td>".format(sid1))
    print("<td>{}</td>".format(temperature))
    print("<td>{}</td>".format(humidity))
    print("<td>{}</td>".format(light))
    print("<td>{}</td>".format(date))
    print("<td>{}</td>".format(firePrediction))
    print("<td><img src={} width='300' ></td>".format(img))
    print("</tr>")
    print("<tr>")
    print("<td>{}</td>".format(rpid2))
    print("<td>{}</td>".format(sid2))
    print("<td>{}</td>".format(temperature))
    print("<td>{}</td>".format(humidity))
    print("<td>{}</td>".format(light))
    print("<td>{}</td>".format(date))
    print("<td>{}</td>".format(firePrediction))
    print("<td><img src={} width='300' ></td>".format(img))
    print("</tr>")
    print("</tbody>")
    print("</table>")
    print("</div>")
    

if __name__ == '__main__':
    printHeader("An Automated Sensor-based Fire Detection System")
    tableCreation()
    printFooter()
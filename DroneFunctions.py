import threading
import socket
import tkinter as tk
import sys
import time
import cv2
import keyboard
# variables for working with the class
port = 9000
currentMovableDist = 50

statButtonPressed = False
isRunning = True
gui_instance = None

host = socket.gethostbyname(socket.gethostname())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localedir = (host, port)
tello_address = ('192.168.10.1', 8889)

sock.bind(localedir)


# *************************
def recv():
    global gui_instance
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            receivedData =(data.decode(encoding="utf-8"))
            gui_instance.update_data_label(receivedData)

        except Exception:
            break


# receiving thread for the commands
recvThread = threading.Thread(target=recv)
recvThread.start()


# *************************
def ReceiveVideo():
    cap = cv2.VideoCapture(f'udp://@{host}:{port}')
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (500, 300))
            cv2.imshow('Tello Stream', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()


# thread for streaming video from the drone and the call function
# for the activation
video_thread = threading.Thread(target=ReceiveVideo)


def CallVideoThread():
    video_thread.start()


# *************************

def SocketSending(msg: str):
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)

    # def ControlDrone(): # will be changed to buttonEvent when interface is added
    #   while isRunning:
    #      SocketSending(MoveByKey())


def ChangeDistance(change):  # addit function for the incoming interface
    return currentMovableDist + change


def MoveDistance():
    return currentMovableDist


def MoveByKey(symbol: str):
    if keyboard.is_pressed('a') is True | (symbol == 'a') is True:
        return f'left {MoveDistance()}'
    elif keyboard.is_pressed('s') is True | (symbol == 's') is True:
        return f'back{MoveDistance()}'
    elif keyboard.is_pressed('d') is True | (symbol == 'd') is True:
        return f'right {MoveDistance()}'
    elif keyboard.is_pressed('w') is True | (symbol == 'w') is True:
        return f'forward {MoveDistance()}'
    elif keyboard.is_pressed('q') is True | (symbol == 'q') is True:
        return f'up {MoveDistance()}'
    elif keyboard.is_pressed('e') is True | (symbol == 'e') is True:
        return f'down{MoveDistance()}'
    elif keyboard.is_pressed('r') is True | (symbol == 'r') is True:
        return f'cw {MoveDistance()}'
    elif keyboard.is_pressed('z') is True | (symbol == 'z') is True:
        Stats()
    elif keyboard.is_pressed('v') is True | (symbol == 'v') is True:
        return f'streamon'
    elif keyboard.is_pressed('Esc') is True:
        global isRunning
        isRunning = False
        SocketSending('land')
    else:
        return 'stop'


def Stats():
    global label_data
    global statButtonPressed
    if not statButtonPressed:
        SocketSending('mon')
        data, server = sock.recvfrom(1518)
        statButtonPressed = True
        msg = (data.decode(encoding="utf-8"))
        label_data.configure(text=msg)
    else:
        SocketSending('moff')

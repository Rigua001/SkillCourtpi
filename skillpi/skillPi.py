import socket
import RPi.GPIO as GPIO
import time
import sys
import os
from subprocess import Popen

# hit=0
# miss=0

GPIO.setmode(GPIO.BCM)
# LED = 18
hSensor = 11
# Initialize pins
# GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(hSensor, GPIO.IN)

sock = socket.socket()

host = socket.gethostname()
port = 23
sock.bind((host, port))

sock.listen(5)
while True:
    con, addr = sock.accept()
    print('Got connection from', addr)
    print(con.recv(1024))
    os.system('cd /home/pi/SkillCourtStand')
    # if the ball hits while led signal is 0
    if con.recv(1024) == '0' and GPIO.input(hSensor) == True:
        os.system('killall omxplayer.bin')
        os.system('omxplayer -l hit.mp3')
        # hit+=1
    # if ball hits while led signal is 1
    elif con.rcv(1024) == '1' and GPIO.input(hSensor) == True:
        os.system('killall omxplayer.bin')
        os.system('omxplayer -l miss.mp3')
        # miss+=1
    elif con.rcv(1024) == '4':
        sock.close()



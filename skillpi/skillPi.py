import socket
import RPi.GPIO as GPIO
import time
import sys
import os
from subprocess import Popen

# hit=0
# miss=0
mode = 15 #15 hit mode, 16 song mode, 17 listen mode
runcount = 0
GPIO.setmode(GPIO.BCM)
# LED = 18
hSensor = 11
# Initialize pins
# GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(hSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sock = socket.socket()

host = '0.0.0.0'#socket.gethostname()
port = 5000
sock.bind((host, port))

sock.listen(5)
#check modes and make fuctions for modes?
try:
    while True:
    con, addr = sock.accept()
    print('Got connection from', addr)
    msg = con.recv(1024)
    mode = msg.decode('')
    song= con.recv(1024)
    songinfo = song.decode('')


    while mode == '15': #normal hit miss
        msg = con.recv(1024)
        dmsg = msg.decode('')
        # if the ball hits while led signal is 0
        if dmsg == '0' and GPIO.input(hSensor) == True:
            os.system('killall omxplayer.bin')
            os.system('omxplayer -l hit.mp3')
            # hit+=1
        # if ball hits while led signal is 1
        elif dmsg == '1' and GPIO.input(hSensor) == True:
            os.system('killall omxplayer.bin')
            os.system('omxplayer -l miss.mp3')
            # miss+=1
        elif dmsg == '-1':
            mode == '0'
    while mode == '16': #sound game
        if runcount == 0:
            os.system('mpsyt')
            time.sleep(10)
            os.system('search' + songinfo)
            time.sleep(10)
            os.system('1')
            runcount = 1

        msg = con.recv(1024)
        dmsg = msg.decode('')
        # if the ball hits while led signal is 0 if hit is good, green
        if dmsg == '0' and GPIO.input(hSensor) == True:
            #os.system('killall omxplayer.bin')
            os.system('+')
            # hit+=1
        # if ball hits while led signal is 1, if hit is bad, red
        elif dmsg == '1' and GPIO.input(hSensor) == True:
            #os.system('killall omxplayer.bin')
            os.system('-')
            # miss+=1
        elif dmsg == '-1':
            mode == '0'
finally:
    sock.close()





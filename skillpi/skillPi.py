#!/usr/bin/env python3
import socket
import subprocess


sock = socket.socket()

host = '0.0.0.0'
port = 9997
sock.bind((host, port))

sock.listen(5)
try:
    while True:
        con, addr = sock.accept()
        print('Got connection from', addr)
        song = con.recv(4096)
        songinfo = str(song,'utf-8')
        song = songinfo[2:]
        print(song)
        outf, errf = open('out.txt', 'w'), open('err.txt', 'w')
        mp = subprocess.Popen('mpsyt .' + song, universal_newlines=True, shell=True, stdin=subprocess.PIPE, stdout=outf,
                              stderr=errf)
        mp.communicate(input='1')
        outf.close()
        errf.close()
finally:
    sock.close()

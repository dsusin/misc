import zmq
import random
import time
import sys

port="5556"
context=zmq.Context()
socket=context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
	msg=socket.recv()
	print msg
	socket.send("client message to server1")
	socket.send("client message to server2")
	time.sleep(1)

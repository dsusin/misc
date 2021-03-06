import zmq
import sys
import time

port="5556"
if len(sys.argv)>1:
    port=sys.argv[1]
    int(port)

context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    message=socket.recv()
    print "Received request: ", message
    time.sleep(1)
    socket.send("World from %s" % port)

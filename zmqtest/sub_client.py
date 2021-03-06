import zmq
import sys

port="5556"
if len(sys.argv)>1:
	port=sys.argv[1]
	int(port)

if len(sys.argv)>2:
	port1=sys.argv[2]
	int(port1)

context=zmq.Context()
socket=context.socket(zmq.SUB)

print "Collecting updates from weather server..."
socket.connect("tcp://localhost:%s" % port)
if len(sys.argv)>2:
	socket.connect("tcp://localhost:%s" % port1)

#subscribe to zipcode 10001
topicfilter="10001"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

#process 5 updates
total_value=0
for update_nbr in range(5):
	string=socket.recv()
	topic, messagedata=string.split()
	total_value+=int(messagedata)
	print topic, messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value/5)

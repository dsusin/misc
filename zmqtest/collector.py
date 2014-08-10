import time
import zmq
import pprint

def collector():
	context=zmq.Context()
	results_receiver=context.socket(zmq.PULL)
	results_receiver.bind("tcp://127.0.0.1:5558")
	collector_data={}
	for x in xrange(1000):
		result=results_receiver.recv_json()
		if collector_data.has_key(result['consumer']):
			collector_data[result['consumer']]+=1
		else:
			collector_data[result['consumer']]=1

		if x==999:
			pprint.pprint(collector_data)

collector()

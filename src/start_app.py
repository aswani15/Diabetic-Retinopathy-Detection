import argparse
import atexit
import time
from subprocess import Popen
import sys
def cleanup():
     timeout_sec = 5
     for p in all_processes: # list of your processes
         p_sec = 0
         for second in range(timeout_sec):
             if p.poll() == None:
                 time.sleep(1)
                 p_sec += 1
         if p_sec >= timeout_sec:
             p.kill() # supported from python 3.6
     print('client and server processes cleaned up!')


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--client-port", nargs=1, help="specify client port", type=int, default=[8000])
	parser.add_argument("--server-port", nargs=1, help="specify server_port", type=int, default=[5000])
	args = parser.parse_args()
	client_port = args.client_port[0]
	server_port = args.server_port[0]

	# start the client
	print("starting client on port ", client_port)
	client = Popen(["python","-m","http.server", str(client_port)], shell=True, cwd="client")

	# start the server
	print("starting the server on port ", server_port)
	server = Popen(["python","app.py", str(server_port)], shell=True, cwd="server")

	# on exit listener
	all_processes = [client, server]
	atexit.register(cleanup)
	while(True):
		time.sleep(1)


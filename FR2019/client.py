import socket
import signal
import sys
import datetime
import psutil
from time import sleep

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:

    try: 
        message = ("[Timestamp: %s, CPU: %5.2f%%, MEM: %5.2f%%]" %(datetime.datetime.now().strftime("%H:%M:%S"), 
            psutil.cpu_percent(interval = 1), psutil.virtual_memory()[2])).encode()
        sleep(15)

        if len(message) > 0:
            sock.send(message)
            response = sock.recv(4096).decode()
            print('Server response: {}'.format(response))

    except(socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)


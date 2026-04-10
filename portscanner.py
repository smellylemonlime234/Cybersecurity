#This script scans a device for open ports at a rate of 250ports/second. Then writes the listening ports to the file 'openports.txt'
import socket
from concurrent.futures import ThreadPoolExecutor
import sys 

if len(sys.argv) != 2:
    print("Please give a host to scan")
    exit(1) 
else:
    host = sys.argv[1]

def scan(port):
    print(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        write_to_file(port)
    else:
          return None

def write_to_file(port):
     with open("openports.txt", "a") as f:
        f.write(f"{host}:Port {port} is listening\n")
        f.flush()

def scan_all():
    with ThreadPoolExecutor(max_workers=250) as executor:
        executor.map(scan, range(1,49152))

scan_all()

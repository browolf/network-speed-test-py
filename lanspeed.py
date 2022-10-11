import requests
import time
import os
import sys
import socket
from datetime import datetime

#setup log file 
user = os.environ['USERNAME']
#store the output on a private network share
output = f"\\\\server\\share$\\lantest\\logs\\{user.lower()}.txt"
if not os.path.exists(output):
    open(output,'w').close()

def write_log_file(data):
    f = open(output, 'a')
    f.write(f"[{gettime()}] {data}")
    f.close()       

#figure out path, different if executable
if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
    #print(f" * Executable Path = {path}")
else:
    path = os.path.dirname(__file__)


server_ip = input('Enter server ip address: ')
url = f"http://{server_ip}:50500/"
LOCALFILE = "file.iso"

#test that the server is available
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
location = (server_ip, 50500)
result_of_check = sock.connect_ex(location)

def gettime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")    

if result_of_check == 0:
    print("Server Ready")

    
    while True: 

        #test server is available
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = (server_ip, 50500)
        result_of_check = sock.connect_ex(location)

        if result_of_check == 0:
            #print("Server Ready")
            start = time.perf_counter()

            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(LOCALFILE, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            download_time = round(time.perf_counter() - start,2)
            #find out file size
            file_size = round((os.path.getsize(path + "\\file.iso")/1048576),2)
            os.remove(path + '\\file.iso')

            average_speed = round((file_size/download_time)*8,2)
            print(f"[{gettime()}] Filesize={file_size}MB Time={download_time}secs Avg Speed={average_speed}Mbit")
            write_log_file(f"Filesize={file_size}MB Time={download_time}secs Avg Speed={average_speed}Mbit\n")

        else:
            now = datetime.now()
            datestr = now.strftime("%Y-%m-%d %H:%M")
            print(f"[{gettime()}] Server {server_ip} offline")
            write_log_file(f"Filesize={file_size}MB Time={download_time}secs Avg Speed={average_speed}Mbit\n")

        time.sleep(300)
else:
    print("Server not found")

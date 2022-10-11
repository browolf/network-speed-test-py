from flask import Flask, send_file, request
import socket
import os
import sys

server_ip_address = socket.gethostbyname(socket.gethostname())
PORT = 50500

if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
    #print(f" * Executable Path = {path}")
else:
    path = os.path.dirname(__file__)

app = Flask(__name__)
app.debug = True

@app.route('/') 
def static_download():
    try:        
        print(f"Connection from {request.remote_addr}")               
        return send_file(path + "\\files\\file.iso", download_name='file.iso')
    except Exception as e:
        print(f"{str(e)}")    


if __name__ == '__main__':
    app.run(host=server_ip_address, port=PORT)

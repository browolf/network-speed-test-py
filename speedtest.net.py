import speedtest
from datetime import datetime
import time
import sys
from socket import gethostname
import os

#computer = gethostname()
user = os.environ['USERNAME']
#Output log file to shared folder. username as name, 
output = f"\\\\server\\share0$\\speedtest\\{user.lower()}.txt"
if not os.path.exists(output):
    open(output,'w').close()

st = speedtest.Speedtest()
st.get_best_server()

def test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res['server']["lat"]

'''
{'download': 463249671.9717738, 'upload': 277831614.2919091, 'ping': 9.807, 
'server': {'url': 'http://speedtest2.lightningfibre.net.uk:8080/speedtest/upload.php', 
'lat': '51.5171', 'lon': '-0.1062', 'name': 'London', 'country': 'United Kingdom', 
'cc': 'GB', 'sponsor': 'Lightning Fibre Ltd', 'id': '34931', 'host': 'speedtest2.lightningfibre.net.uk:8080', 
'd': 2.560290148248664, 'latency': 9.807}, 'timestamp': '2022-06-22T13:35:45.322736Z', 'bytes_sent': 151519232, 
'bytes_received': 409373932, 'share': None, 'client': {'ip': '195.80.27.86', 'lat': '51.4964', 'lon': '-0.1224', 
'isp': 'Club Communications Ltd', 'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0', 'country': 'GB'}}
'''



while True:
    d, u, p = test()
    now = datetime.now()
    datestr = now.strftime("%Y-%m-%d %H:%M")
    f = open(output, 'a')   
    try:
        print (f"[{datestr}]Download: {round(d/1048576,1)}MB Upload: {round(u/1048576,1)}MB Latency: {p}")
        f.write(f"[{datestr}]Download: {round(d/1048576,1)}MB Upload: {round(u/1048576,1)}MB Latency: {p}\n")
    except Exception as ex:
        print (f"[{datestr}]An exception of {type(ex)} occurred, {ex.args}")
        f.write(f"[{datestr}]An exception of {type(ex)} occurred, {ex.args}\n")
        pass

    f.close()    
    time.sleep(300)

# Python Applications for testing Networks

## Speedtest.net.py

Runs a internet speedtest every 5 mins and stores the results in a text file stored on a private network share. 

Uses https://pypi.org/project/speedtest-cli/

Note: if you  miss off -cli you'll get a different thing and the script won't work. 

You need to edit the network share location in the script. 

## Lantest

- lanserver.py
- lanspeed.py

a client server application that tests the network speed between 2 locations. 

A large iso is hosted on a webserver and another program fetches it and records the speed. The webserver can be run on a laptop plugged in the network or a virtual server. 

The client script asks for the ip of the webserver host. 

The webserver uses Flask : [pypi.org/project/Flask/](https://pypi.org/project/Flask/)

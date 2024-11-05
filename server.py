import waitress
import socket
import flask
from flask import *

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class Waitress(flask.Flask):
    def waitress_serve(self,*,host="0.0.0.0",port=8080):
        self.waitress_server = waitress.server.create_server(self,host=host,port=port)
        print("Serving flask app with waitress")
        print(f"Listening on: http://{host}:{port}")
        print(f"Listening on http://{get_ip()}:{port}")
        self.waitress_server.run()
        
        
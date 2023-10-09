from flask import Flask, jsonify, render_template, Response, json, request, redirect, url_for

from time import sleep

import socket, json, requests

app = Flask(__name__)

def host_ip():
    try:
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((ipaddress, 80))
        ip = sock.getsockname()[0]
        print('IP address:', ip)

    finally:
        sock.close()

    return ip 

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/book_services')
def book_services():
    return render_template('book_services.html')

@app.route('/heat_pump')
def heat_pump():
    return render_template('heat_pump.html')    


if __name__ == '__main__':
    ip = host_ip()
    app.run(host=ip, port=9980, debug=True)
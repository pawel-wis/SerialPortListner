import serial
import requests
from datetime import datetime

def log_before():
    try:
        f = open('log.txt', 'a')
        f.write('Sending data to API')
        f.write(datetime.now())
        f.write('################')
        f.close()
    except IOError:
        print("Error -> Can't open file log.txt")


def log_after(res):
    try:
        f = open('log.txt', 'a')
        f.write("Response: {}".format(res))
        f.write(datetime.now())
        f.write('################\n\n')
        f.close()
    except IOError:
        print("Error -> Can't open file log.txt")

if __name__ == '__main__':
    ser = serial.Serial('', 9600)
    secret = '1234'
    URL = 'localhost:8000/api/room/'
    while True:
        msg = str(ser.readline())
        data = msg.split(':')
        temp = data[0]
        hum = data[1]

        req = {
            'temperature': temp,
            'humidity': hum,
            'secret': secret
        }

        log_before()
        r = requests.post(url=URL, data=req)
        log_after(r)

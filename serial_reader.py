import serial
import requests
from datetime import datetime

def log_before():
    try:
        f = open('log.txt', 'a')
        f.write('Sending data to API\n')
        f.write(str(datetime.now()))
        f.write('\n')
        f.write('################\n')
        f.close()
    except IOError:
        print("Error -> Can't open file log.txt")


def log_after(res):
    try:
        f = open('log.txt', 'a')
        f.write("Response: {}\n".format(res.text))
        f.write(str(datetime.now()))
        f.write('\n')
        f.write('################\n\n')
        f.close()
    except IOError:
        print("Error -> Can't open file log.txt")

if __name__ == '__main__':
    port = '/dev/ttyACM0'
    ser = serial.Serial(port, 9600)
    secret = '1234'
    URL = 'http://localhost:8000/api/room/'
    while True:
        msg = ser.readline().decode('ascii')
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

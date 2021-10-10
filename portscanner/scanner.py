# coding=utf-8
import socket
import sys


def scan(start, finish, ip):
    try:
        for port in range(start, finish):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("Process interupted")
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
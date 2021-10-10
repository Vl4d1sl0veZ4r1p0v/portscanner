# coding=utf-8
import argparse
import socket
from utils import print_banner
from scanner import scan


def get_args():
    parser = argparse.ArgumentParser(description="portscanner")
    parser.add_argument("-t", "--host",
                        help="host address to check (192.168.0.1)")
    parser.add_argument("-r", "--range",
                        default="1-1024",
                        help='the interval of ports to check, is set '
                             'as a start-end, for example, 20-1000')
    return parser.parse_args()


def main():
    args = get_args()
    remoteServer = args.host
    remoteServerIP = socket.gethostbyname(remoteServer)
    range_ = tuple(map(int, args.range.split('-')))

    print_banner(remoteServerIP)

    scan(range_[0], range_[1], remoteServerIP)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

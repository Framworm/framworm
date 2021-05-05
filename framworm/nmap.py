#Imports
from .config   import IP_TO_SCAN, PORTS_TO_SCAN
from socket    import socket, SOCK_STREAM, AF_INET

def nmap():
    ret = {}
    for IP_TO_SCAN
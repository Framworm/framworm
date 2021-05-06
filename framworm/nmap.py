#Imports
from .config   import IP_TO_SCAN, PORTS_TO_SCAN, NMAP_PORT_TIMEOUT
from socket    import socket, timeout, SOCK_STREAM, AF_INET

def nmap():
    """
    :return: Un dictionnaire de type {ip : [port1, port2, ...], ...}
    """
    ret = {}
    for ip in IP_TO_SCAN:
        ports = []
        for port in PORTS_TO_SCAN:
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(NMAP_PORT_TIMEOUT)
                try:
                    s.connect((str(ip), port))
                    ports.append(port)
                except timeout:
                    pass
        if ports != []:
            ret[ip] = ports
    
    return ret
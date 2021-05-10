#Imports
from .config   import IP_TO_SCAN, PORTS_TO_SCAN, NMAP_PORT_TIMEOUT
from .utils    import formatLog, ping
from socket    import socket, timeout, SOCK_STREAM, AF_INET
from base64    import b64encode

def nmap(inst):
    """
    :param inst: Référence de la classe Event
    :return: Un dictionnaire de type {ip : [port1, port2, ...], ...}
    """
    ips = []
    ret = {}
    for ip in IP_TO_SCAN:
        print(ip)
        if ping(ip) == True:
            ips.append(ip)

    for ip in ips:
        ports = []
        for port in PORTS_TO_SCAN:
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(NMAP_PORT_TIMEOUT)
                try:
                    s.connect((str(ip), port))
                    ports.append(port)
                except timeout:
                    pass
                except Exception as e:
                    inst.logGeneraux.put_nowait(formatLog("error", b64encode(str(e).encode())))

        if ports != []:
            ret[ip] = ports
    
    return ret
#Imports
from .config   import IP_TO_SCAN, PORTS_TO_SCAN, NMAP_PORT_TIMEOUT
from .utils    import formatLog, ping
from socket    import socket, timeout, SOCK_STREAM, AF_INET
from base64    import b64encode

def nmap(inst):
    """
    :param inst: Référence de la classe Event
    :return: Un tuple (host, port)
    """
    for ip in IP_TO_SCAN:
        if ping(ip, NMAP_PORT_TIMEOUT) == False:
            continue
        for port in PORTS_TO_SCAN:
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(NMAP_PORT_TIMEOUT)
                try:
                    s.connect((str(ip), port))
                    yield (ip, port)
                except timeout:
                    pass
                except Exception as e:
                    inst.logGeneraux.put_nowait(formatLog("error", b64encode(str(e).encode())))

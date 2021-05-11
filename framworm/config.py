#Imports
from .utils    import getIp, getMask
from ipaddress import ip_network

#Range d'ip à scanner
IP_TO_SCAN    = ip_network(f"{getIp()}/{getMask(getIp())}", strict=False)
#Range de ports à scanner
PORTS_TO_SCAN = [20, 21, 22, 53, 80, 443, 8080]
#Nombre de secondes avant de considerer qu'une connection est impossible
NMAP_PORT_TIMEOUT = 0.5
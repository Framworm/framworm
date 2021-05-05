#Imports
from .utils    import getIp, getMask
from ipaddress import ip_network

#Range d'ip à scanner
IP_TO_SCAN    = ip_network(f"{getIp()}/{getMask(getIp())}")
#Range de ports à scanner
PORTS_TO_SCAN = range(1024)
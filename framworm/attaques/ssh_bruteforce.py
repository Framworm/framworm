from .abstract import Abstract
import socket

class Attaque(Abstract):
    def __init__(self, cibles, ref):
        for ip,ports in cibles.items():
            self.addresses = addresses
            self.ports = ports 

        Abstract.__init__(cibles, ref)
    
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with open("../files/wordlists/rockworm.txt") as wordlist:
            words = wordlist.readline()
            for address in addresses:
                for port in self.ports:
                    for word in words:
                        s.connect((address,port))
                        
                
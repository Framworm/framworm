#Imports
from datetime   import datetime
from socket     import getfqdn, socket, AF_INET, SOCK_STREAM
from sys        import exit
from subprocess import run, TimeoutExpired
from platform   import system as osname

#Fonctions
def formatLog(severite, data):
    """
    Retourne un log au format : '<SEVERITE> TIMESTAMP HOSTORIP DATA'
    :param severite: Niveau de severite du log
    :param data:     La donnée du log
    """
    date     = str(datetime.now()).replace(" ", "_")
    hostorip = getfqdn()
    return f"<{severite}> {date} {hostorip} {data}"

endOfProgramm = lambda: exit(0)

def getIp():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(("8.8.8.8", 53))
        return s.getsockname()[0]
    
def getMask(ip):
    pre = int(ip.split(".")[0])
    if pre < 128:
        return 8
    elif pre < 192:
        return 16
    else:
        return 24

def queueToList(q):
    """
    Transforme une queue en liste
    """
    ret = []
    while True:
        try:
            ret.append(q.get_nowait())
        except:
            return ret

def ping(ip, timeout):
    """
    :param ip: L'ip à ping
    :return:   True si accessible, sinon False
    """
    commande = f"ping {'-n 1' if osname() == 'Windows' else '-c 1'} {ip}".split()

    try:
        proc = run(commande, timeout=timeout, capture_output=True)
    except TimeoutExpired:
        return False

    if proc.returncode == 0:
        return True
    else:
        return False
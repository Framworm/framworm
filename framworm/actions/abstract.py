#Fichier contenant la classe abstraite permettant de lancer une Action
#Lorsque vous codez votre Action, appelez votre classe Action
"""
from .abstract import Abstract

class Action(Abstract):
    def __init__(self, ref):
        Abstract.__init__(cibles, ref)
    
    def run(self):
        pass
"""
#Imports
from ..utils import formatLog

#Classes
class Abstract():
    """
    Classe à hériter
    """
    def __init__(self, refLoop, host, port):
        """
        Constructeur
        :param refLoop: Référence vers la classe contenant la boucle d'éxecution
        :param host:    L'hôte sur lequel effectuer notre run
        :param port:    Le port
        """
        self.refLoop = refLoop
        self.host    = host
        self.port    = port
        self.cibles  = self.refLoop.cibles
        self.logs    = self.refLoop.logsAction
    
    def log(self, severite, data):
        """
        Génère un log
        :param severite: La séverité choisie
        :param data:     La donnée
        """
        log = formatLog(severite, data)
        self.logs.put(log)

    def info(self, data):
        """
        Génère un log d'info
        :param data: La donnée
        """
        self.log("info", data)

    def warn(self, data):
        """
        Génère un log d'avertissement
        :param data: La donnée
        """
        self.log("warn", data)

    def error(self, data):
        """
        Génère un log d'erreur
        :param data: La donnée
        """
        self.log("error", data)

    def crit(self, data):
        """
        Génère un log critique
        :param data: La donnée
        """
        self.log("crit", data)

    def bilan(self, data):
        """
        Génère un log bilan
        :param data: La donnée
        """
        self.log("bilan", data)

    def run(self):
        """
        Méthode à surcharger pour éxecuter notre action
        :return: True si a réussi, sinon False
        """
        pass
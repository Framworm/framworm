#Fichier contenant la classe abstraite permettant de lancer une Dissimulation
#Lorsque vous codez votre Dissimulation, appelez votre classe Dissimulation
"""
from .abstract import Abstract

class Dissimulation(Abstract):
    def __init__(self, ref):
        Abstract.__init__(cibles, ref)
    
    def run(self):
        pass
"""
#Imports
from base64  import b64encode
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
    
    def log(self, severite, data):
        """
        Génère un log
        :param severite: La séverité choisie
        :param data:     La donnée
        """
        log = formatLog("dissimulation", severite, b64encode(data.encode()).hex())
        self.refLoop.logs.put_nowait(log)

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
        Méthode à surcharger pour éxecuter notre dissimulation
        :return: True si a réussi, sinon False
        """
        pass
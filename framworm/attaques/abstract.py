#Fichier contenant la classe abstraite permettant de lancer une attaque
#Imports
from ..utils import formatLog

#Classes
class Abstract():
    """
    Classe à hériter
    """
    def __init__(self, refLoop):
        """
        Constructeur
        :param refLoop: Référence vers la classe contenant la boucle d'éxecution
        """
        self.refLoop = refLoop
        self.logs    = self.refLoop.logsAttaque
    
    def info(self, data):
        """
        Génère un log d'info
        :param data: La donnée
        """
        log = formatLog("info", data)
        self.logs.put(log)

    def warn(self, data):
        """
        Génère un log d'avertissement
        :param data: La donnée
        """
        log = formatLog("warn", data)
        self.logs.put(log)

    def error(self, data):
        """
        Génère un log d'erreur
        :param data: La donnée
        """
        log = formatLog("error", data)
        self.logs.put(log)

    def crit(self, data):
        """
        Génère un log critique
        :param data: La donnée
        """
        log = formatLog("crit", data)
        self.logs.put(log)

    def run(self):
        """
        Méthode à surcharger pour éxecuter notre attaque
        :return: True si a réussi, sinon False
        """
        pass
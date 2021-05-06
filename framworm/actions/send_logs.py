#Imports
from ..utils   import queueToList
from .abstract import Abstract
from requests  import put

### Configuration du module ###
URL_TO_PUT = "http://127.0.0.1/putLogs"
###############################

#Classes
class Action(Abstract):
    """
    Classe permettant d'envoyer les logs au serveur
    """
    def __init__(self, ref):
        Abstract.__init__(cibles, ref)
    
    def run(self):
        #Send attack logs
        put(
            URL_TO_PUT, 
            data = {
                "attaque" : queueToList(self.refLoop.logsAttaque)      
            } 
        )
        #Send action logs
        put(
            URL_TO_PUT, 
            data = {
                "action" : queueToList(self.refLoop.logsAction)       
            } 
        )
        #Send dissimulation logs
        put(
            URL_TO_PUT, 
            data = {
                "dissimulation" : queueToList(self.refLoop.logsDissimulation)
            } 
        )

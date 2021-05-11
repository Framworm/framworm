#Imports
from ..utils        import queueToList
from .abstract      import Abstract
from urllib.request import Request, urlopen
from json           import dumps

### Configuration du module ###
URL_TO_POST = "http://localhost:8000/"
###############################

#Classes
class Action(Abstract):
    """
    Classe permettant d'envoyer les logs au serveur
    """
    def __init__(self, ref, host, port):
        Abstract.__init__(self, ref, host, port)
    
    def post(self, url, data):
        req = Request(url, data=dumps(data).encode(), method="POST")
        urlopen(req)

    def run(self):
        try:
            #Send attack logs
            self.post(
                URL_TO_POST, 
                data = {
                    "attaque" : queueToList(self.refLoop.logsAttaque),
                    "action" : queueToList(self.refLoop.logsAction),
                    "dissimulation" : queueToList(self.refLoop.logsDissimulation)      
                } 
            )
        except Exception as e:
            print(e)

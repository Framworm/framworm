#Imports
from ..utils        import queueToList
from .abstract      import Abstract
from urllib.request import Request, urlopen
from json           import dumps
from base64         import b64encode

### Configuration du module ###
URL_TO_POST = "http://localhost:8000/get"
###############################

#Classes
class Action(Abstract):
    """
    Classe permettant d'envoyer les logs au serveur
    """
    def __init__(self, ref, host, port):
        Abstract.__init__(self, ref, host, port)
    
    def post(self, url, data):
        req = Request(url, data=b64encode(dumps(data).encode()), method="POST")
        urlopen(req)

    def run(self):
        try:
            #Send attack logs
            self.post(
                URL_TO_POST, 
                data = queueToList(self.refLoop.logs) 
            )
        except Exception as e:
            print(e)

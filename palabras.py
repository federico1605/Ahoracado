class Palabra:
    def __init__(self,palabra):
        self.__palabra = palabra
        self.__activo = True
        self.__longitud = len(palabra)
        
    #Getters
    def getPalabra(self):
        return self.__palabra
    
    def getActivo(self):
        return self.__activo
    
    def getLongitud(self):
        return self.__longitud
    
    #Setters
    def setActivo(self,activo):
        self.__activo = activo
        
list = [Palabra("besties"),Palabra("hamburguesa"),Palabra("esternocleidomastoideo"),Palabra("federico"),Palabra("software"),Palabra("loco")]

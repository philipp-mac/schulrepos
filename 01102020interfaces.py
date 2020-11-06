import abc

class Motorisiert(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def motorStarten(self):
        pass
    
    @abc.abstractmethod
    def tanken(self, treibstoff: str):
        pass
    
    @abc.abstractmethod
    def ladungAufnehmen(self, anzahl: int):
        pass
    
    @abc.abstractmethod
    def hupen(self):
        pass
    
    
class Auto(Motorisiert):
    def __init__(self):
        self.tankfüllung = 100.0
        self.treibstoffArt = "benzin"
        self.kapazitaet = 5
        super().__init__()
        
    def motorStarten(self):
        self.tankfüllung -= 5.0
        print("motor laeuft, noch im tank :", self.tankfüllung, " %") 
                
    def tanken(self, treibstoff):
        if treibstoff == self.treibstoffArt:
            print("richtiger treibstoff: ", self.treibstoffArt)
            self.tankfüllung = 100.0
        return self.tankfüllung

    
    def ladungAufnehmen(self, anzahl):
        if anzahl <= self.kapazitaet:
            print("ladung aufgenommen")
            return True
        else:
            print("ladung nicht aufgenommen")
            return False
        
    def hupen(self):
        print("hup")
        
class Fahrer():
    def __init__(self):
        self.auto = Auto()
        super().__init__()

    def fahren(self):
        self.auto.motorStarten()
        #self.auto.hupen()
        
    def boxStop(self):
        self.auto.tanken("benzin")
        self.auto.ladungAufnehmen(2)
                
    
# auto = Auto()
# auto.motorStarten()
# auto.motorStarten()
# print(auto.ladungAufnehmen(5))
# print(auto.tanken("benzin"))
# print(auto.tanken("gas"))

print("-----------")

fahrer = Fahrer()
fahrer.fahren()
fahrer.auto.hupen()
fahrer.boxStop()
import Bilgisayarlar
import Okullar

class VeriKaynagi():
    def __init__(self):
        pass

    def bilgisayarListesiAl(self):    #Mevcut bilgisayarların listesi alınır.
        self.bilgisayarListesi=[]
        self.bilgisayarListesi.append(Bilgisayarlar.bilgisayar1)
        self.bilgisayarListesi.append(Bilgisayarlar.bilgisayar2)
        return self.bilgisayarListesi


    def okulListesiAl(self):          #Mevcut okulların listesi alınır.
        self.okulListesi = []
        self.okulListesi.append(Okullar.okul1)
        self.okulListesi.append(Okullar.okul2)
        return self.okulListesi




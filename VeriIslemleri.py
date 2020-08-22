from Bilgisayarlar import Bilgisayarlar
from Okullar import Okullar
class VeriIslemleri(Bilgisayarlar):
    def __init__(self):
        pass

    def bilgisayarListele(self,bilgisayarListesi,flag):
        self.list1 = bilgisayarListesi
        if flag==True:                          #Güncelleme durumunda kullanılır
            return self.list1
        else:                                   #Bilgisayarların listesi yazdırılır ve liste döndürülür
            for i in range(len(self.list1)):
                print("İd: ",self.list1[i].id)
                print("Marka: ",self.list1[i].marka)
                print("Ram: ",self.list1[i].ram)
                print("Fiyat: ",self.list1[i].fiyat)
                print("\n")
            return self.list1

    def okulListele(self,okulListesi,flag):
        self.list2 = okulListesi
        if flag==True:                           #Güncelleme durumunda kullanılır
            return self.list2
        else:                                    #Okulların listesi yazdırılır ve liste döndürülür
            for i in range(len(self.list2)):
                print("İd: ",self.list2[i].id)
                print("Konum: ",self.list2[i].konum)
                print("Derece: ",self.list2[i].derece)
                print("Ögrenciler: ",self.list2[i].ogrenciSayisi)
                print("\n")
            return self.list2

    def bilgisayarAra(self,liste1,id):    #Fonksiyona gönderilen id ile listedeki bilgisayarların id'leri karşılaştırılır.
        self.liste1 = liste1
        self.id=id
        for i in range(len(self.liste1)):
            if self.liste1[i].id == self.id:
                return self.id

    def okulAra(self,liste2,id):         #Fonksiyona gönderilen id ile listedeki okulların id'leri karşılaştırılır.
        self.liste2 = liste2
        self.id = id
        for i in range(len(self.liste2)):
            if self.liste2[i].id == self.id:
                return self.id

    def bilgisayarGuncelle(self,bulunanBilgisayar,yeniBilgisayar,liste1,yeniBilgisayarID):   #Bulunan bilgisayar ile yeni bilgisayar yer değiştirir.
        self.bulunanBilgisayar=bulunanBilgisayar
        self.yeniBilgisayar=yeniBilgisayar
        self.temp=self.bulunanBilgisayar
        self.bulunanBilgisayar=self.yeniBilgisayar
        self.yeniBilgisayar=self.temp
        self.subclass=VeriIslemleri()
        self.nesne=self.subclass.bilgisayarListele(liste1,True)
        self.nesne[yeniBilgisayarID-1]=self.bulunanBilgisayar


    def okulGuncelle(self,bulunanOkul,yeniOkul,liste2,yeniOkulID):              #Bulunan okul ile yeni bilgisayar yer değiştirir.
        self.bulunanOkul = bulunanOkul
        self.yeniOkul = yeniOkul
        self.temp = self.bulunanOkul
        self.bulunanOkul = self.yeniOkul
        self.yeniOkul = self.temp
        self.subclass = VeriIslemleri()
        self.nesne = self.subclass.bilgisayarListele(liste2, True)
        self.nesne[yeniOkulID-1] = self.bulunanOkul



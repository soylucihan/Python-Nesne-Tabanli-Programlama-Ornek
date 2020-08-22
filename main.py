import Bilgisayarlar
import Okullar
import VeriKaynagi
import VeriIslemleri
















print("\n")
"""Bilgisayarlar"""
bilgisayarListesi=VeriKaynagi.VeriKaynagi()     #Tüm bilgisayarların listesi alındı.
liste1=bilgisayarListesi.bilgisayarListesiAl()

print("Güncellemeden Önce")
liste_sıralama=VeriIslemleri.VeriIslemleri()    #Liste yazdırıldı.
liste_sıralama.bilgisayarListele(liste1,False)

bulunanBilgisayar=VeriIslemleri.VeriIslemleri()    #İstenilen ID numarısında bir bilgisayar arandı.
bulunan=bulunanBilgisayar.bilgisayarAra(liste1,3)

yeniBilgisayarID=3
yeniBilgisayar=Bilgisayarlar.Bilgisayarlar(yeniBilgisayarID,"Lenovo",8,5700)   #Yeni bir bilgisayar eklendi.

if bulunan!= None:                                #Arama yapılan ID zaten mevcut ise silinir ve yeni eklenen bilgisayar yerine alınır.
    yeniNesne=VeriIslemleri.VeriIslemleri()
    yeniNesne.bilgisayarGuncelle(bulunan,yeniBilgisayar,liste1,yeniBilgisayarID)
else:
    liste1.append(yeniBilgisayar)       #Arama yapılan ID mevcut değilse yeni bilgisayarda listeye eklenir.

print("Güncellemeden Sonra")                #Yeni liste yazdırılır.
yeniListe1=VeriIslemleri.VeriIslemleri()
yeniListe1.bilgisayarListele(liste1,False)





"""Okullar"""               #Bilgisayar kısmında yapılan işlemlerin aynısı yapılır.

okulListesi=VeriKaynagi.VeriKaynagi()
liste2=okulListesi.okulListesiAl()

print("Güncellemeden Önce")
liste_sıralama2=VeriIslemleri.VeriIslemleri()
liste_sıralama2.okulListele(liste2,False)

bulunanOkul=VeriIslemleri.VeriIslemleri()
bulunan2=bulunanOkul.okulAra(liste2,3)

yeniOkulID=3
yeniOkul=Okullar.Okullar(yeniOkulID,"England",93,17000)

if bulunan2!= None:
    yeniNesne2 = VeriIslemleri.VeriIslemleri()
    yeniNesne2.okulGuncelle(bulunan,yeniOkul,liste2,yeniOkulID)
else:
    liste2.append(yeniOkul)

print("Güncellemeden Sonra")
yeniListe2=VeriIslemleri.VeriIslemleri()
yeniListe2.okulListele(liste2,False)



















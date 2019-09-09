import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanallar=["TRT"],kanal="TRT"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanallar=kanallar
        self.kanal=kanal

    def tv_ac(self):

        if self.tv_durum=="Açık":
            print("Televizyon Zaten Açık.....")

        else:
            print("Televizyon Açılıyor.....")

            self.tv_durum="Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı.....")

        else:
            print("Televizyon Kapanıyor.....")

            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:

            ayar=input("Ses İşaretin Giriniz...")


            if ayar==">":
                if self.tv_ses != 31:

                    self.tv_ses+=1

                    print("Ses :",self.tv_ses)

            elif ayar=="<":
                if self.tv_ses !=0:
                    self.tv_ses-=1
                    print("Ses :", self.tv_ses)
            if ayar=="q":
                print("Ses Güncellendi :",self.tv_ses)
                break

    def kanal_ekle(self,kanal):
        print("Kanal Ekleniyor...")
        time.sleep(1)


        self.kanallar.append(kanal)

        print("Kanal Eklendi")


    def kanal_sil(self,sil):
        print("Kanal Siliniyor...")
        time.sleep(1)

        self.kanallar.remove(sil)

        print("Kanal Silindi")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanallar)-1)

        self.kanal=self.kanallar[rastgele]
        print("Şu anki kanal :",self.kanal)
    def __len__(self):
        return len(self.kanallar)

    def __str__(self):

        return "TV DURUMU : {} \nTV SES : {} \nTV'de BULUNAN KANALLAR : {} \nAÇIK OLAN KANAL : {} ".format(self.tv_durum,self.tv_ses,self.kanallar,self.kanal)

kumanda=Kumanda()
print("""
Televizyon Uygulaması

1.TV AÇ
2.TV KAPAT
3.SES AYARLARI
4.KANAL EKLE 
5.KANAL SAYISI
6.RASTGELE KANAL DEĞİŞTİRME
7.TV BİLGİLERİ
8.KANAL SİLME
""")

while True:
    islem=input("İstediğiniz işlemi giriniz : ")
    if islem=="q":
        print("Program Sonlandırılıyor....")
        break
    islem=int(islem)

    if islem==1:
        kumanda.tv_ac()
    elif islem==2:
        kumanda.tv_kapat()
    elif islem == 3:
        kumanda.ses_ayarlari()
    elif islem == 4:
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak giriniz")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == 5:
        print("Kanal Sayısı:",len(kumanda))

    elif islem == 6:
        kumanda.rastgele_kanal()

    elif islem == 7:
        print(kumanda)

    elif islem==8:
        ksil=input("Silmek istediğiniz kanalı giriniz")
        for i in kumanda.kanallar:
            if ksil==i:
                kumanda.kanal_sil(ksil)

        if kumanda.kanallar==[]:
            kumanda.kanal="Kanal Yok"




    else:
        print("Gecersiz İşlem")

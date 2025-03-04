#1.1 Bir sayı dizisinin ortalamasını hesaplayan bir fonksiyon yazın.
listem=[1,5,44,23,45,22]
toplam=0
uzunluk=len(listem)
for i in listem:
    toplam+=i
print(toplam/uzunluk)
print('************************************************')

#1.2 Girilen iki sayının en büyüğünü döndüren bir fonksiyon oluşturun.
def enBuyuk(s1,s2):
    if s1>s2:
        return(s1)
    elif s2>s1:
        return(s2)
    else:
        return('these two are equal')
print(enBuyuk(6,8))
print('************************************************')

#1.3Bir metin içindeki kelimeleri sayan bir fonksiyon yazın.
def kelimeSayaci(message):
    kelimeSayisi=message.split()
    print(kelimeSayisi)
    return len(kelimeSayisi)
print("Metindeki kelime sayısı: ",kelimeSayaci('ulen acaba cidden sayabilecek mi bakalım.'))

print('************************************************')

#2.1 Bir liste içindeki tek sayıların karesini alan bir map fonksiyonu yazın
def tekMi(sayi):
    return sayi % 2 != 0

def karesiniAl(sayi):
    return sayi ** 2

def tekSayilarinKaresi(liste):
    return list(map(karesiniAl, filter(tekMi, liste)))

sayilar = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Fonksiyonlarla tek sayıların kareleri:", tekSayilarinKaresi(sayilar))
print('************************************************')

# 0-50 arasında yer alan çift sayıları filtrelemek için bir filter fonksiyonu  kullanın.
def filter(a,b):
    for sayi in range(a,b+1):
        if sayi%2==0:
            print(sayi)
filter(0,50)
print('************************************************')

#Lambda kullanarak, verilen iki sayı arasındaki tüm tam sayıların toplamını 
#hesaplayan bir fonksiyon oluşturun.
sumThese = lambda a, b: sum(range(a, b + 1))
print(sumThese(4,33))
print('************************************************')

#Global ve yerel değişkenlerle çalışan bir uygulama yazın. Örneğin, bir 
#global sayacın fonksiyon içinde artırıldığı bir uygulama geliştirin.
x=10
def Func():
    global x
    x+=1
    return x
Func()
print(x)
print('************************************************')

# Bir Hesap Makinesi sınıfı oluşturun. Bu sınıf toplama, çıkarma, çarpma ve 
# bölme işlemlerini gerçekleştirsin.
class HesapMakinesi:
   def toplamak(self,p,j): return p+j
   def cikarma(self,a,b): return a-b
   def carpma(self,c,d):return c*d
   def bolme(self, m, n): return m / n if n != 0 else "Tanımsız"

  
meow=HesapMakinesi()
print(meow.toplamak(50,20))
print('************************************************')

#  Bir Öğrenci sınıfı oluşturun. Öğrencinin adı, notları ve sınıfını tutan 
# özellikler ekleyin. Ortalama not hesaplayan bir metot yazın.
class Ogrenci:
    def __init__(self,name,grades,year):
     self.name=name
     self.grades=grades
     self.year=year
    def ortalamaNot(self):
         return sum(self.grades) / len(self.grades)
    
    def ogrenciyiyazdir(self):
        print(f"Ad: {self.name}")
        print(f"Notlar: {self.grades}")
        print(f"Sınıf: {self.year}")      
        print(f"Ortalama: {self.ortalamaNot():.2f}")
ogrenci1= Ogrenci("Polat Alemdar",[50,33,100],2)     
ogrenci2= Ogrenci("Memati",[22,59,90],4)
ogrenci1.ogrenciyiyazdir()
ogrenci2.ogrenciyiyazdir()
print('************************************************')
#  Bir Hayvan sınıfı yazın ve bu sınıftan Kedi ve Köpek alt sınıflarını türetin. 
# Her alt sınıf için farklı ses çıkaran bir metot ekleyin.
class Hayvan:
     def __init__(self, name):
         self.name = name
     def ses():
         pass

class Kedi(Hayvan):
    def ses(self):
         return f"{self.name}: Miyav!"

class Kopek(Hayvan):
    def ses(self):
        return f"{self.name}: Hav Hav!"

kedi=Kedi("Balım")
kopek=Kopek("Gofret")
print(kedi.ses())
print(kopek.ses())

print('************************************************')
#  Bir Araba sınıfından türeyen bir Elektrikli Araba sınıfı oluşturun. Elektrikli 
# araba sınıfına pil seviyesi ve şarj metotları ekleyin.
class Araba:
    def __init__(self,marka,yil):
        self.marka=marka
        self.yil=yil
    
class ElektrikliAraba(Araba):
     def __init__(self,marka,yil,pil):
          super().__init__(marka,yil)
          self.pil=pil
        
     def sarj(self):
          print(f"{self.marka} şarj oldu.")
          self.pil=100
     def pilSeviyesi(self):
         print(f"{self.marka} pil seviyesi: %{self.pil}")
      
tofas=ElektrikliAraba("Elektrikli Tofaş",2026,54)    
tofas.pilSeviyesi()
tofas.sarj()
tofas.pilSeviyesi()

print('************************************************')
#  İki vektörü toplayan özel bir 
# __add__ metodu tanımlayın.
class Vektor:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def __add__(self, ikinci):
        
        toplamX = self.x + ikinci.x
        toplamY = self.y + ikinci.y
        return Vektor(toplamX, toplamY)  

    def vektorGoster(self):
        print(f"Vektör: {self.x,self.y}")
v1 = Vektor(2, 4)
v2 = Vektor(5, 2)

v3 = v1 + v2 
v3.vektorGoster()
print('************************************************')
#  Bir sınıfta nesnenin açıklamasını veren bir 
# __str__ metodu yazın.
class Character:
    def __init__(self,name,eyeColour,height,weight,superPower):
        self.name=name
        self.eyeColour=eyeColour
        self.height=height
        self.weight=weight
        self.superPower=superPower
    def __str__(self):
        return f"My characters name is: {self.name} \nEye colour is:{self.eyeColour} \nHeight and weight is:{self.height},{self.weight}\nSuperpower is:{self.superPower}"
myCharacter=Character("Yuri","Hazel","1.62 m",50,"sleeping")
print(myCharacter.__str__())

print('************************************************')
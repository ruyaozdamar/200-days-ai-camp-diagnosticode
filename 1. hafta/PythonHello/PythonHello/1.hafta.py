print("Merhaba Yapay Zeka!")

isim = input("Lütfen isminizi giriniz: ")
print(f"Merhaba, {isim}! Python öğrenmeye hoş geldin.")

ad="rüya"  
yaş=55
para=50000.0
cinsiyet=True 
print(yaş+para) #sonucu float olarak verdi

#kullanıcıdan 2sayı alıp dört işlem yapma
x= input("Lütfen birinci sayıyı giriniz: ")
y= input("Lütfen ikinci sayıyı giriniz: ")
z= int(x)+int(y)
m= int(x)-int(y)
n= int(x)*int(y)
k= int(x)/int(y)
print(f"bu sayıların toplamları:{z} ", f"farkları:{y} ", f"çarpımları:{n} ", f"birbirlerine bölümleri:{k}")

print(float(yaş)+para) #en az iki türü birbirine dönüştürme
print(str(yaş)+ad)

metin = input("Büyük harflerle tekrar yazdıracağınız bir cümle girin: ")
print(metin.upper())

#alışveriş listemiz
listemiz = ["muz", "süt", "bal"]

listemiz.append("balık")
listemiz.append("yumurta")

listemiz.remove("süt")  

print("Alışveriş listesinin son hali:", listemiz)

#ehliyet test
kullaniciYasi= input("Lütfen yaşınızı giriniz: ")
if int(kullaniciYasi)>=18:
    print("Ehliyet alabilirsiniz.")
else: 
    print("Ehliyet almak için yaşınız tutmuyor.")

   #import random
    # rastgele_sayi = random.randint(1, 10)
    # while True:
    #         tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
    #         if tahmin < 1 or tahmin > 10:
    #             print("Lütfen 1 ile 10 arasında bir sayı girin.")
    #             continue
    #         if tahmin == rastgele_sayi:
    #             print("Tebrikler! Doğru tahmin ettiniz.")
    #             break
    #         else:
    #             print("Yanlış tahmin! Tekrar deneyin.")
   
   
import random
sayi = random.randint(1, 10)
can=int(input('kaç hakkınız olsun?: '))
hak=can
sayac=0
  
while hak>0:
  hak-=1
  sayac+=1
  tahmin=int(input('1 ile 10 arasında bir sayı tahmin edin: '))
  if tahmin<1 or tahmin>10:
    print('Sayınız 1-10 arasında değil!')
  if tahmin==sayi:
    print(f'Tebrikler! {sayac}. defada Bildiniz.Toplam puanınız: {100-(100/can)*(sayac-1)}')
    break
  elif tahmin<sayi:
    print('YUKARI')
    
  else: 
    print('AŞAĞI')
  if hak==0:
      print('hakkınız bitti.')
       
satır=4
sütun=3
x= int(input('Lütfen gemi tahmininizin satırını giriniz(1-5): '))
if(x<1 or x>5):
        print('Geçersiz satır tahmini.1-5 arası giriniz.')
y= int(input('Lütfen gemi tahmininizin sütununu giriniz(1-5): '))
if(y<1 or y>5):
        print('Geçersiz sütun tahmini.1-5 arası giriniz.')
if (x==satır and y==sütun):
        print('Tebrikler! Gemiyi vurdunuz.')
else:
        print('OOPS! Yanlış tahmin.')



#Girilen iki sayıdan hangisi büyüktür
# a=int(input('sayı1:'))
# b=int(input('sayi2:'))
# result=(a>b)
# print(f'a:{a} b:{b} den büyüktür:{result}')


#kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız.
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# vize1=float(input('1.vizeyi giriniz'))
# vize2=float(input('2.vizeyi girin'))
# final=float(input('final notunu girin'))
# ortalama=((vize1+vize2))/2*0.6+final*0.4
# print(f'ortalamanız:{ortalama} ve dersten geçme durumunuz:{ortalama>=50}')



# #Girilen bir sayının tek mi çift mi olduğunu yazdırınız.
# a=int(input('sayı girin '))
# result=a%2
# print(f'girdiğiniz sayı {a} çifttir.{result==0}')



# #Girilen bir sayının  pozitif mi negatif mi
# a=int(input('sayı girin '))
# print(f'girdiğiniz sayı {a} pozitiftir.{a>0}')



#Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#(email:email@sadikturan.com parola:abc123)
email='email@sadikturan.com'
parola='abc123'

email1=input('email adresini yazınız: ')
parola1=input('parolayı yazınız: ')
isEmail=(email==email1)
isPassword=(parola==parola1)
print(f'Email bilgisi doğru mu:{isEmail} ve Parola doğru mu:{isPassword}')
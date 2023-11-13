#Bmw,Mercedes,Opel, Mazda elemanlarına sahip bir liste oluşturun



cars=['Bmw','Mercedes','Opel','Mazda']
result=len(cars)

# result=cars[0]#ilk eleman
# result=cars[-1]#son eleman
# print(result)

# cars[-1]='Toyota'
# print(cars)  mazdayı toyotayla değiş

# mercedes listenin elemanı mı
# result='Mercedes' in cars
# print(result)


# # listenin -2 index elemanı ne
# result=cars[-2]
# print(result)

#listenin ilk 3 elemanı ne
# result=cars[0:3]
# print(result)

# #listenin son 2 elemanı yerine Toyota renault koy
# cars[-2:]=['Toyota','Renault']
# print(cars)

# # #Listenin üzerine Audi ne Nissan ekle
# # result=cars+['Audi','Nissan']
# # print(result)

# #Listenin son elemanını sil
# cars.pop()
# print(cars)

# #tersten yazdır
# result=cars[::-1]
# print(result)


#Aşağıdaki verileri bir liste içinde saklayınız

#studentA:Yiğit Bilgi 2010,(70,60,70)
#studentB:Sena Turan  1999,(80,80,70)
#studentC:Ahmet Turan  1998,(80,70,90)
studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

#liste elemanlarını ekrana yazdır.
result=studentA[0]
result=studentB[1]
result=studentC[3][1]
print(result)

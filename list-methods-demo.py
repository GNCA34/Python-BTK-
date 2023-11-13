names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

# #Cenk listenin sonuna ekle
# names.append('Cenk')
# print(names)

# #sena yı listenin başına ekle
# names.insert(0,'Sena')
# print(names)

# #denizi sil
# names.remove('Deniz')
# print(names)

#denizin indexi nedir
index=names.index('Deniz')
print(index)
#ali listenin elemanı mı
result='Ali' in names
result=names.index('Ali')
print(result)

# #listeyi ters çevir
# names.reverse()
# print(names)

# #alfabetik sırala
# names.sort()
# print(names)

#kullanıcıdan aldığın 3 tane markayı listeye ekle

markalar=[]
marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)
print(markalar)

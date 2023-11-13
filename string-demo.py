
website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# #'course' karakter dizisinde kaç karakter bulunmaktadır
# result=len(course)
# print(result)

# #'website' içinden www karakterlerini alın
# result=website[7:10]
# print(result)

# #website içinden com karakterlerini alın
# result=website[22:25]
# print(result)

# #course içinden ilk 15 ve son 15 karakterlerini alın.

# result=course[0:15]
# cumle=course[15:]
# print(result)
# print(cumle)


# #course ifadesindeki karakterleri tersten yazınız
# result=course[::1]
# print(result)

# s='12345'*5 # 5 kere tekrar eder
# print(s)
# print(s[::5])


# name,surname,age,job='Bora','Yılmaz',32,'Mühendis'
# #Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
# # Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim Mühendis
# result="Benim adım "+name+" "+surname+", Yaşım "+str(age)+" ve mesleğim "+job
# print(result)
# son='Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}'.format(name,surname,age,job)
# print(son)

# #Hello world ifadesindeki w harfini W ile değiştirin.
# s='Hello world'
# s=s[0:6]+'W'+s[-4:]
# print(s)
# s.replace('w','W')
# print(s)

#abc ifadesini yan yana 3 defa yazdırın
result='abc '*3
print(result)
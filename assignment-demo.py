from cgitb import reset
from traceback import print_tb
from unittest import result


x,y,z=2,5,10

numbers=1,5,7,10,6
#1-Kullanıcıdan aldığınız  2 sayının çarpımı ile x,y,z,toplamının farkı nedir

########1.########
# a=int(input('a değerini girin '))
# b=int(input('b değerini girin '))
# result=(a*b)-(x+y+z)

# print(result)

########2.########
#2-y'nin x'kalansız bölümünü hesaplayınız
# result=y//x
# print(result)
# #3-(x,y,z) toplamının mod 3 ü ne
# result=(x+y+z)%3
# print(result)
# #y^^nin x. kuvvetini hesapla
# result=y**x kuvvet alırken
# print(result)


# #x,*y, z=numbers işlemine göre z'nin küpü kaç
# x,*y,z=numbers
# result=z**3
# print(result)


#x,*y,z=numbers işlemine göre ynin değerleri toplamı kaçtır
x,*y,z=numbers
result=y[0]+y[1]+y[2]
print(result)
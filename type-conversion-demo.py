"""
Daire Alanı:pi.r^2
Daire Cevresi:2.pi.r

Yarıçapı verilen bir dairenin alanı ve cevresini hesapla
"""

pi=3.14

r=float(input('yarıçap:'))

alan=pi*r**2
cevre=2*pi*r
print("alan: "+str(alan )+" cevre: "+str(cevre))

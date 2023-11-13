'''
ogrenciler={
    '120':{
        'ad':'Ali',
        'soyad':'Yılmaz',
        'telefon':'123 345 23 23',

    },
    '125':{
        'ad':'Can',
        'soyad':'Korkmaz',
        'telefon':'345 345 43 34'
        },
    '128':{
        'ad':'Volkan',
        'soyad':'Yükselen',
        'telefon':'234 345 65 89',
    },
    }
1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle diztionary içinde saklayınız.
2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.




'''

ogrenciler={}
number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyad: ")
phone=input("öğrenci telefon: ")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }

ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone,
    }
})
print(ogrenciler)


ogrNo=input('öğrenci no:')
ogrenci =ogrenciler[number]
print(ogrenci)
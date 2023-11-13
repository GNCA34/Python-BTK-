# #key-value
# #Bir bilgiye ulaşmak için key kullanıyoruz

# #41 => kocaeli 34=> istanbul

# sehirler=['kocaeli','istanbul']
# plakalar=[41,34]
# print(plakalar[sehirler.index('istanbul')])

# #plakalar={'key':value}
# plakalar={'kocaeli':41,'istanbul':34}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])
# plakalar['ankara']=6
# plakalar['kocaeli']='new value'#değeri değiştirir
# print(plakalar)


# users={
#     'sadikturan':36,
#     'cinarturan':2
# }
# print(users['cinarturan'])

users={
'sadikturan':{
    'age':36,
    'roles':['user'],
    'email':'sadik@gmail.com',
    'address':'kocaeli',
    'phone':'12312312'
},
'cinarturan':{
    'age':46,
    'roles':['admin','user'],
    'email':'turan@gmail.com',
    'address':'istanbul',
    'phone':'45809312'
}
}

print(users['sadikturan']['age'])
print(users['sadikturan']['email'])
print(users['cinarturan']['phone'])
print(users['cinarturan']['roles'])
print(users['sadikturan']['roles'])
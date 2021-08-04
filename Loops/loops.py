age = 13
if age > 20:
    print ('Как-то вы староваты')

age = 8
if age == 12:
    print ("свинья шлепнулась в грязь")
else:
    print ("тсс, это секрет")

if age == 10 or age == 11 or age == 12 or age == 13:
    print ('13 + 49 + 84 + 155 = 97:что получится')
else:
    print ("что-что")

age = '10'
converted_age = int (age)
if converted_age == 10:
    print ("как лучше общаться?")
    print ("издалека")

for x in range (0, 5):
    print ('привет %s' % x)
    
twinkies = 50
if twinkies < 100 or twinkies > 500:
    print ("слишком мало")
else:
    print ("слишком много")

money = 200
if money > 100 and money < 500:
    print ("соответствует")

ninjas = 70
if ninjas < 50:
    print ("их слишком много")
elif ninjas < 30:
    print ("будет непросто, но я с ними разделаюсь")
elif ninjas > 60:
    print ("я одолею этих ниндзя")


ninjas = 5
if ninjas < 50 and ninjas < 30 and ninjas < 10:
    print ("я одолею ниндзя")

# использование цикла for

for x in range (0, 5):
    print ("привет")

for x in range (0, 5):
    print ("привет %s" % x)

wizard_list = ['карандаш', 'тетрадь', 'ручка']
for i in wizard_list:
    print (i)
    
x = 2
while x < 20:
    x = x + 2
    print (x)

for x in range (0, 20):
    print ('привет %s' % x)
    if x < 9:
        break

ingredients = ['хлеб', 'молоко', 'масло']
for a in ingredients:
    print(a)


ingredients = ['хлеб', 'молоко', 'масло']
for index, xyz in enumerate (ingredients):
    print (f'{index + 1} {xyz}')
    



weight = 46
for year in range (1, 16):
    moon_weight = weight * 0.165 
    print (year, moon_weight)
    weight += 1 

from chapter_7 import variable_test

print(variable_test())












      






    








    













    











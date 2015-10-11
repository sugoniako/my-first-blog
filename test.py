#print 'hello world'

#v = 2
#t = 8

#if v > t:
#    print v
#else: 
#    print t



#m1 = {'name':'Vasya', 'apple':3}
#m2 = {'name':'Petya', 'apple':5}

#if m1['apple'] > m2['apple']:
#    print m1['name']
#else: 
#    print m2['name']



#for a in range(0,10):
#    print a

#c = [23, 56, 43, 87, 13, 5, 61]

#for l in c:
#    print l+1



#def trp (name):
#  print 'Hello,'+' '+ name

#name = 'Artur'
#trp (name)

class Animal():
    lapu = 4
    hvost = True
    usu = 33

    def eat (self, food):
        print 'energy'

    def scratche (self):
        print 'pleusur'

class Cat(Animal):
    usu = 20

class Dog (Animal):
    usu = 4
    hvost = False

dog1 = Dog()

animal1 = Animal()

cat1 = Cat()

print cat1.usu
print cat1.lapu

cat1.scratche ()
















    









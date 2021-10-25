# class point:
#     def __init__(self,x,y):
#         self._x=float(x)
#         self._y=float(y)

#     def move(self,a,b):
#         self._x=a
#         self._y=b


#     def reset(self):
#         self._x=0
#         self._y=0
        

#     def getx(self):
    
#         return self._x



#     def getx(self):
#         return self._y


#     def setx(self,newvalue):
#         self._x  = float(newvalue)


   
#     def sety(self,newvalue):
#         self._y  = float(newvalue)
             

class Person:
    def __init__(self, FodelseDatum):
        self._fodelsedatum = int(FodelseDatum)
        self._namn = ""
        self._gatuadress = ""
        self._postnummer = ""
        self._postort = ""
        self._kön= ''

    def setkön(self,nykön):
        self._kön = nykön  

    def getkön(self):
        return self._kön          
    def setName(self, nyVarde):
        self._namn = nyVarde.capitalize()

    def getNamn(self):
        return self._namn

    def setAdress(self, Gata):
        self._gatuadress = Gata.lower()
    def getAdress(self):
        return self._gatuadress

    def moveAdress(self, changeAdress):
        self._gatuadress = changeAdress.lower()

person1 = Person(2001)
person2 = Person(1997)

person1.setName("Danijel")
person2.setName("Ahmad")

person = person2.getNamn()
print(person)



person1.setAdress("Kihlmansgatan 3B")
person2.setAdress("Västermovägen 26B")

person1.moveAdress("Västermovägen 26B")
# person2.moveAdress("Kihlmansgatan 3B")

gataPerson1= person1.getAdress()
gataPerson2= person2.getAdress()
print(f"Ahmad bor i gatan: {gataPerson2} \noch Danijel bor i gatan: {gataPerson1} ")
namnPerson1= person1.getNamn()
print(namnPerson1)
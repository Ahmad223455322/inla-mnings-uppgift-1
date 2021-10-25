#from point import point


# a= point(10,20)

# # a.reset()

# # a.move(2,4)
# # b.move(4,4)


# a.setx(12)
# a.sety(111)

# # a.x="dfgfdgfg"
# # a.x ="dfgedfegsdf"
# # print(a.getx())
# # print(a.get.y())


# # a=123

# print(a.x)
# print(a.y)
# #b= point()


from point import Person
person1 = Person(2001)
person2 = Person(1997)

person1.setName("Danijel")
person2.setName("Ahmad")

person1.setkön("Man")
person2.setkön("Man")

a= person1.getkön()
print(a)

person = person2.getNamn()
print(person)



person1.setAdress("Kihlmansgatan 3B")
person2.setAdress("Västermovägen 26B")

person1.moveAdress("Västermovägen 26B")
# person2.moveAdress("Kihlmansgatan 3B")

gataPerson1= person1.getAdress()
gataPerson2= person2.getAdress()
print(f" bor i gatan: {gataPerson2} \noch Danijel bor i gatan: {gataPerson1} ")
namnPerson1= person1.getNamn()
print(namnPerson1)
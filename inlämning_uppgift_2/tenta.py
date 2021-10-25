# #fråga 7
# inmatning = int(input("Mata in ett tal"))
# första = inmatning * 2
# andra = inmatning * 3
# tredje = inmatning * 4
# print(f'{inmatning} * 2 = {första}')
# print(f'{inmatning} * 3 = {andra}')
# print(f'{inmatning} * 4 = {tredje}')

#fråga 4

# def rensa_dålgaord(text):
#     badWords = ["work", "job", "boss", "vegetables", "fish"]
#     for boksatv in badWords:
#         text = text.replace(boksatv, "****")    
#     return text
        

# x = input("Mata in en text")  
# print(rensa_dålgaord(x))    


# fråga 3
# def IsValidPassword(password):
#     passwordLength= len(password)
#     if passwordLength >= 8:
#         CanNotBeInclusive= ["hej","lösen","hopp"]
#         for word in CanNotBeInclusive:
#             if word in password:
#                 return False
#         NumberOfUpperCharacter = 0
#         NumberOfLowerCharacter = 0
#         NumberOfSymbols = 0 
#         Symbols = "@$!#&*%_"
#         for character in password:
#             if character.isupper() == True:
#                 NumberOfUpperCharacter += 1
#             if character.islower() == True:
#                 NumberOfLowerCharacter += 1
#             if character in Symbols:
#                 NumberOfSymbols += 1
#         if NumberOfUpperCharacter >= 2 and NumberOfLowerCharacter >= 2 and NumberOfSymbols >=1:
#             return True
#         return False
#     return False

# password = "JorDgubb_12"
# IsValidPassword(password)
     



#fråga 5


# def antalbostäver(cities):
#     x=""
#     for bokstav in cities:
#         x=x+bokstav
#     return len(x)
# cities = ["Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London"]    
# print(antalbostäver(cities))




#fråga 1
# class Present:
#     def __init__(self,namn, pris):
#         self._namn= namn
#         self._pris= pris
    
#     def get_price(self):
#         return self._pris

# class Person:
#     def __init__(self,namn):
#         self._namn = namn
#         self._julklapp =[]

#     def addjul_klappar(self,present:Present):
#         return self._julklapp.append(present)   

#     def räkna_total (self):
#         sum =0
#         for x in self._julklapp:
#             sum += x.getprice()
#         return sum    

# lista=[]

# person1 = Person ("Stefan")
# person2= Person("Fanny")
# person3= Person("Linn")

# present1 = Present("Klocka","4815")
# present2 = Present("kläning","112")
# present3 = Present("leksak","115")

# person1.addjul_klappar(present1)

# lista.append(person1)
# for pers in lista:
#     print(f'{pers.getnamn()}den ska har{pers.räkna_total()}')


# fråga 2
# Abc123
# abc12d
# def giltig(reg_nummer):
    
#     bokstavlista =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     siffror = ['1','2','3','4','5','6','7','8','9','0']
#     for x in range(0,3):
#         if reg_nummer[x] not in bokstavlista:
#             return "Nej"
#         else:
#             for x in range(3,5):
#                 if reg_nummer[x]  not in siffror:
#                     return "Nej"
#                 else:
#                     if reg_nummer[5] in bokstavlista or reg_nummer[5] in siffror:
#                         return "Ja"   

# a = input("mata in ")
# print(giltig(a))                        



#fråga 6
# import random
# totalpoints= 0
# listaMedPoints= []
# for domare in range(1,6):
#     pointsFromDomare = round(random.uniform(0,10),1)
#     print(f'Poäng från domare {domare} {pointsFromDomare}')
#     listaMedPoints.append(pointsFromDomare)

# largestpoint = max(listaMedPoints)
# lowestpoint = min(listaMedPoints)
# listaMedPoints.remove(largestpoint)
# listaMedPoints.remove(lowestpoint)

# for point in listaMedPoints:
#     totalpoints += point

# snittPoint = totalpoints / len(listaMedPoints)
# treDecimaler = format(snittPoint,".3f")
# print(treDecimaler)


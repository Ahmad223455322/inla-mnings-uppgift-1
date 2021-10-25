




# class member:

#     inte_tillängliga_namn=[ "bajs","ideot","loser"]

#     def __init__(self, förstnsmn, mellannamn, efternamn,kön):

#         self.fnamn= förstnsmn
#         self.mnamn= mellannamn
#         self.enamn= efternamn
#         self.ikön= kön
#     def full_namn(self):
#         if self.fnamn in member.inte_tillängliga_namn:
#             raise ValueError("Namn inte tillgänglig")
#         else:    
#             return f'{self.fnamn} {self.mnamn} {self.enamn}'
#     def namn_with_titel(self):
#         if self.kön == "man":
#             return f'Hej Mr  {self.fnamn}'   
#         elif self.kön == "kvinna":
#             return f'Hej miss {self.fnamn}'     
#     def få_all_info(self):
#         return f'{self.namn_with_titel()},ditt full namn är:{self.full_namn()}'        


# member_ett= member("Ahmad","byström","Zarzar", "man")
# member_två= member("Fanny","maritan","byströn", "kvinna")
# member_tre= member("Linn ","byström","Zarzar", "kvinna")
# member_fyra= member("bajs","fvv ","zarzar","man")



# # print(member_ett.full_namn ())
# # print(member_två.namn_with_titel())

# print(member_fyra.få_all_info())


#inhertens 

# class food:
#     def __init__(self,name, prise):
#         self.name=name
#         self.prise=prise

#         print(f"{self.name}food is created from bass  {self.prise}class")
#     def eat(self):
#         print("eat method from bass class") 
# class äpple(food): 
#     def __init__(self, name, prise):
#         super().__init__(name, prise)
    


#         print(f"{self.name}äpple is createde from derived class{self.prise} ")
# #foodett = food( "pizza") 
# foodtvå = äpple("pizza",150)  
# foodtvå.eat()                


# labb 2
# class Rektankeg:
#     def __init__(self, hjöd, bereden):
#         self._hjöd = float(hjöd)
#         self._bered= float(bereden)
#     def räkna_area (self):
#         return self._hjöd * self._bered





# rektangel1=Rektankeg (4,5)

# rekt =  rektangel1.räkna_area()
# print(f' Arean är {rekt}')


#labb 3

# class cirkel:
#     def __init__(self,radius):
#         self._radius= float(radius)

#     def räkna_area (self):
#         return self._radius * self._radius * 3.14   

#     def räkna_omkrets(self):
#         return 2 * self._radius  * 3.14


    

# cirkere_area1 = cirkel (4)        
# area= cirkere_area1.räkna_area()
# print(f' area är{area}cm')

# cirkere_omkrets1 = cirkel (4)        
# omkretss= cirkere_omkrets1.räkna_omkrets()
# print(f' omkretssen är{omkretss}cm')


# #labb 4 

# class person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age


    
#     def rovaspråk(self):
#         röv_text=""
#         vokallista =["a","e","i","o","U","ö","y","ä","å"," ","0","1","2","3","4","5","6","7","8","9"]
#         for bokstav in self._name:
#             if bokstav not in vokallista:
#                 röv_text += bokstav+"o"+ bokstav 
#             else:  
#                 röv_text+=bokstav
#         return röv_text.title()    
    
    
#     def ålder_gräns(self):
#       if self._age >= 18:
#         return True
#       return False    
    
# name=input("ange namn")
# age=int(input('ange ålder'))

# person1= person(name,age)


# print(person1.rovaspråk())
# print(person1.ålder_gräns())
 
    
#labb 1

# class Matträtt:
#     def __init__(self,namn,pris,typ,antalkalorier):
#         self._namn= namn
#         self._pris= pris
#         self._typ= typ
#         self._antalkalorier= antalkalorier

#     def Dangens_lunsh_meny(self):
#         return [self._namn,self._pris,self._typ,self._antalkalorier]



# maträt_ett = Matträtt("Kebab","110:-","kött","600 kalorier")
# maträt_två = Matträtt ("Lasange", "105:-","Vegetarisk","570 kalorier")
# maträtt_tre = Matträtt("Blomkåltacos","105:-","Vegansk","490 kalorier")


# print(f"****Dagans Lunch****\n{maträt_ett.Dangens_lunsh_meny()}\n{maträt_två.Dangens_lunsh_meny()}\n{maträtt_tre.Dangens_lunsh_meny()}")





# labb 3 




class kennel:
    
    def __init__(self,namn, ras, ålder , vikt):
        self._namn = namn
        self._ras = ras
        self._ålder= float(ålder)
        self._vikt= float(vikt)
        

    def registera(self):
        svans = self.getsvans()
        return [ self._namn,self._ras, self._ålder, self._vikt, svans]
        #return f"Hundnamn {self._namn}{self._ras} {self._vikt}kg {self._ålder}år svanslängd= {svans}\n"

    def printHundar(self):
        for hund in hundlista:
            print(f"Hundnamn {hund[0]} {hund[1]} {hund[2]}kg {hund[3]}år svanslängd= {hund[4]}\n")





    def getsvans(self):
        if self._ras != "tax":
            return self._ålder * self._vikt /10
        return 3.7

    def tabort_(self,namn):
        for hund in hundlista:
            if namn == hund[0]:
                hundlista.remove(hund)
                return f'{namn}bortagen' 
        return f'{namn}finns inte'        



    # def ta_bort_hund(self, hund):
    #     hundlista.remove(hund)

    # def om_den_finns(self,namn):
    #     for hund in hundlista:
    #         if self._namn == namn:
    #             return hund
    #     return None            



    # def ta_bort(self, hund):
    #     for x in range(len(hundlista)):
    #         if hund ==  hundlista[x][0]:
    #              del hundlista[x] 
    #     return

    # def ta_bort(self, x):
    #     for x in hundlista:
    #         if x == self._namn:
    #           del hundlista[hundlista.index(x)]
    #     return         




hundlista=[]
def minsta_svanslängde(minsta_svans):
        svansre=[]
        for x in range(0,len(hundlista)):
            if (hundlista[x][-1]>= minsta_svans): 
                svansre.append(hundlista[x][-1])  
        return svansre                 

                

                
            
while True:
    svar = input(f"****Meny****\n1.Registrera\n2.Lista\n3.Ta bort\n4.Avsluta\n")
    if svar == "1":
        dinhund = kennel(input("ange vilket namn"),input("ange vilken ras"),input("ange vilken ålder"),input("ange vilken vikt"))
        hundlista.append(dinhund.registera())
        
    elif svar == "2":
        dinhund.printHundar()
        minsta_svans =float(input("vad har ni för svans längd ->"))
        print(minsta_svanslängde(minsta_svans))

    elif svar == "3":
        hund_namn=input("ange vilket namn")
        bort = dinhund.tabort_(hund_namn)
        print(bort)
        dinhund.printHundar()
        # if s is None:
        #     print("Hund med det namnet fanns ej i registret")
        # else:
    
        
        
        
        
        
            
          
    # else svar == "4":
    #     print(*hundlista) 
        
        

    #     break
        break


# class Dog:
#     def __init__(self, namn, ras,alder,vikt):
#         self._namn = namn
#         self._ras = ras
#         self._alder = alder
#         self._vikt = vikt

#     def GetNamn(self):
#         return self._namn

#     def GetVikt(self):
#         return self._vikt

#     def GetRas(self):
#         return self._ras


#     def TailLength(self):
#         if self._ras == "tax":
#            return 3.7
#         return self._alder * self._vikt / 10.0

# class Kennel:
#     def __init__(self):
#         self._dogs = []

#     def AddDog(self, dog):
#         self._dogs.append(dog)

#     def ListDogs(self, length):
#         list = []
#         for d in self._dogs:
#             if d.GetTailLength() > length:
#                 list.append(d)
#         return list


#     def RemoveDog(self, dog):
#         self._dogs.remove(dog)

#     def DogExists(self, namn):
#         for dog in self._dogs:
#             if book.GetNamn() == namn:
#                 return dog
#         return None



# ourKennel = Kennel()
# while True:
#     print("1. Lägg till hund")
#     print("2. Lista")
#     print("3. Returnera bok")
#     s = input("Välj ->")
#     if s == "1":
#         print("Namn på hund")
#         namn = input("->")
#         print("Ras")
#         ras = input("->")
#         print("Ålder")
#         alder = int(input("->"))
#         print("Vikt")
#         vikt = float(input("->"))
#         ourKennel.AddDog(Dog(namn,ras,alder,vikt))
#     elif s == "2":
#         print("Minsta svanslängd")
#         lent = float(input("->"))
#         for dog in ourKennel.ListDogs(lent):
#             print(f"{dog.GetName()} {dog.GetRas()} {dog.GetVikt()} kg svans={dog.GetTailLength()}")
#     elif s == "3":
#         print("Namn hund att ta bort")
#         namn = input("->")
#         dog =  ourKennel.DogExists(namn)
#         if dog is None:
#             print("Hund med det namnet fanns ej i registret")
#         else:
#             ourKennel.RemoveDog(dog)
#     elif s == "4":
#         break
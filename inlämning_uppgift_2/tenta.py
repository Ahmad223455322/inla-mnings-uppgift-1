# #fråga 7
# inmatning = int(input("Mata in ett tal"))
# # första = inmatning * 2
# andra = inmatning * 3
# tredje = inmatning * 4

# print(f'{inmatning} * 2 = {fösta}')

# print(f'{inmatning} * 3 = {andra}')
# print(f'{inmatning} * 4 = {tredje}')


# ##anda lösnnig
# for x in range(2,5):
#     y =x * inmatning 
#     print(f'{inmatning} * {x} = {y}')
#fråga 4

# def rensa_dålgaord(text):
#     badWords = ["work", "job", "boss", "vegetables", "fish"]
#     for boksatv in badWords:
#         text = text.replace(boksatv, "****")    
#     return text
        

# x = input("Mata in en text")  
# print(rensa_dålgaord(x))    


# # fråga 3
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
        
#     return False

# password = "Jorfgubb&12hej"
# print(IsValidPassword(password))
     



#fråga 5


# def antalbostäver(lista):
#     x=""
#     for bokstav in lista:
#         x=x+bokstav
#     return len(x)
# cities = ["Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London"]    
# print(f'Antal bokstäver är {antalbostäver(cities)} ')




# # #fråga 1
# class Present:
#      def __init__(self,present_namn:str, pris:float):
#          self._namn= present_namn
#          self._pris= float(pris)
    
#      def get_price(self:float)->float:
#          return self._pris
    
  
# class Person:
#     def __init__(self,namn:str):
#         self._namn = namn
#         self._julklapp : list[Present]=[]

#     def addjul_klappar(self,present:Present):
#         return self._julklapp.append(present)   

#     def räkna_total (self):
#         sum = 0
#         for x in self._julklapp:
#             sum += x.get_price()
#         return sum    
    
#     def getnamn(self):
#         return self._namn    




# lista : list[Person] =[]

# person1 = Person ("Ahmad")
# person2= Person("Fanny")
# person3= Person("Linn")

# present1 = Present("Klocka","4815")
# present2 = Present("kläning","112")
# present3 = Present("leksak","115")

# person1.addjul_klappar(present1)
# person2.addjul_klappar(present2)
# person3.addjul_klappar(present3)

# lista.append(person1)
# lista.append(person2)
# lista.append(person3)
# for pers in lista:
#     print(f'{pers.getnamn()}ska få julklappar för totalt{pers.räkna_total()}')



# fråga 2
# Abc123
#abc12d
# def giltig(reg_nummer):
    
#     bokstavlista =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     siffror = ['1','2','3','4','5','6','7','8','9','0']
#     for x in range(0,3):
#         if x == 2:
#             for x in range(3,5):
#                 if reg_nummer[x]  not in siffror:
#                     return "Nej"
#                 else:
#                     if reg_nummer[5] in bokstavlista or reg_nummer[5] in siffror:
#                         return "Ja"   
#         if reg_nummer[x] not in bokstavlista:
#             return "Nej"
        

# a = input("mata in ")
# print(giltig(a))                        



#fråga 6

# totalpoints= 0
# listaMedPoints= []
# for domare in range(1,6):
#     pointsFromDomare =float(input(f'Poäng från domare {domare}'))
    
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


#***************************************************************
#STRING LABBAR FRÅN GAMMLA FÖRELÄSNINGAR

# def ta_bort_boktav(ord):
#     listamedbokstav=["a","b"]

#     # om man ska kalla något funktion inbygdd  i en funktion då måste man skapa en variabel in funktionen 
#     for bokstav in listamedbokstav:
#             ord = ord.replace(bokstav,"")
#             ord=ord.strip()
#     return ord       

# a= input("skriv")
# print(ta_bort_boktav(a) )   
# a = a.replace("xa","c")
# print(a)




# Be användare mata in ett ord eller en mening. Programmet skall kontrollera om det

# ordet är en palindrom dvs om ordet blir likadant om man läser framifrån och bakifrån.

# Exempel på palindrom är namn som ”anna” eller ”otto” eller en mening som ”ni talar

# bra latin”. Meddela användaren om det är en palindrom eller ej.

# def palindrom(ord):

#     ord = ord.replace(" ", "")

#     omvänt_ord= ""

#     ordlength = len(ord) +1

#     for bokstav_postion in range(-1,-ordlength,-1):
        
#         omvänt_ord += ord[bokstav_postion]

#     if ord == omvänt_ord:

#         return "Det är en palidrom"

   

#     return "Det är inte en palidrom"



# a=input("Mata in ett ord")

# print(palindrom(a))



#andralösninig
# temp=input("Skriv din mening här: ")

# temp=temp.split()

# temp="".join(temp)

# temp=list(temp)

# omvänt= temp[::-1]

# kontroll=True



# for i in range(len(temp)):

#     if temp[i] == omvänt[i]:

#         test=True

#     elif temp[i] != omvänt[i]:

#         test=False

#         print("Denna mening är inte palymdrom")

#         break

# if test==True:

#     print("Denna mening är palymdrom")





# Du har strängen string namn="kurt andersson";

# Skriv kod så att förnamn och efternamn i variabeln namn börjar med stora bokstäver.

# Resultatet skall bli så här "Kurt Andersson"

#första lösnig

# def byt_fösta_bokstav(namn):
#     namn = namn.title()
#     namn = namn.strip()
#     return namn

# a=input("ange namn")
# print(byt_fösta_bokstav(a))


# #andra lösnig
# def ändra_till_stor(namn):
#     nynamn=""
#     första_bokstav = True
#     första_bokstav_iefternamnet = False
#     for x in namn:
#         if första_bokstav == True or första_bokstav_iefternamnet == True:
#             nynamn+=x.upper()
#         else: 
#             nynamn+=x
#         första_bokstav =False
#         if x ==" ":
#             första_bokstav_iefternamnet=True
#         else:
#             första_bokstav_iefternamnet = False
#     return nynamn            
# a=input("ange namn")
# print(ändra_till_stor(a))







# Du har en sträng med texten ”Detta är en sträng som du skall ändra”. Ersätt via kod

# alla blanktecken i strängen med tecknet * . Räkna sedan ut via kod hur många

# förekomster det finns av tecknet * i strängen.


# def sjärn_teken(mennig):
#     count = 0
#     for x in mennig:
#         if x == " ":
#             mennig=mennig.replace(x,"*")
#             count+=1
            
#     return f'{mennig,count}'

# a=input("ange meninng")
# print(sjärn_teken(a))            






#  Gör ett program där användaren får mata in en mening t ex ”Detta är min text

# som jag matar in”. Programmet skall räkna ut hur många ord meningen består av

# och meddela användaren om detta.


# sträng = "Detta är min text som jag matar in"
# sträng = sträng.split()
# antal_ord=len(sträng)
# count = 0
# for ord in sträng:
#     count+=1
# print(count)    
    
    
# def ränka(x):

    
#     nman=""
#     for y in x:
#       nman+=y
#     return(len(nman)) 

# x=["Ahmad","Fanny"]

# print(ränka(x))       








# #Fråga 1
# from datetime import datetime

# class Bilannons:
#     def __init__(self,regnr:str,startdatum:datetime, slutdatum:datetime, pris:float):
#         self._regnr = regnr
#         self._startdatum =startdatum
#         self._slutdatum = slutdatum
#         self._pris= pris
#         self.blakfride = False


#     def setstartdatum(self,startdatum:datetime):
#         self._startdatum = startdatum
    
    
#     def setslutdatum(self,slutdatum:datetime):
#         self._slutdatum = slutdatum

#     def getregnr(self):
#         return  self._regnr  

#     def getstartdatum(self:datetime):
#         return self._startdatum  


#     def getslutdatum(self:datetime):
#         return self._slutdatum    

    
#     def getpris(self:float):
#         if self.blakfride:
#             if datetime.now() >= datetime(2021,11,4,0,0,0) and datetime.now() <= datetime(2021,11,28,23,59,59):
#                 return self._pris * 0.8 
#         return  self._pris  

#     def includ_black_friyd(self,inklude:bool):
#         self.blakfride= inklude



# annoser : list[Bilannons]=[]
# annoser.append(Bilannons("abc111",datetime(2021,11,27,0,0,0),
# datetime(2021,12,12,0,0,0),10000))  
# annoser.append(Bilannons("abc333",datetime(2021,11,1,0,0,0),
# datetime(2021,12,12,0,0,0),30000))  
# annoser.append(Bilannons("abc222",datetime(2021,11,1,0,0,0),
# datetime(2021,12,12,0,0,0),40000))
# annoser[0].setstartdatum(datetime(2021,10,20,12,20,13))
# annoser[0].setslutdatum(datetime(2021,10,23,13,25,13))
# annoser[0].includ_black_friyd(True)


# for annons in annoser:
#     print(f'{annons.getregnr()} {annons.getpris()} {annons.getstartdatum()} {annons.getslutdatum()}')
 









# def remov_negativa(inlista:list[int]) ->list[int]:
#     nylista =[]
#     for tal in inlista:
#         if tal >= 0:
#             nylista.append(tal)
#     return nylista        


# biggest=0
# lista = [1,345,-222,45,6669,0,21]
# for tal in lista:
#     if tal > biggest:
#         biggest = tal
# print(biggest)

# nylista = remov_negativa(lista)
# for tal in nylista:
#     print(tal)




# def SumAllDigitsIntext(text:str)->int:
#     taletavsumman =0
#     for tal in text:
#         if tal.isdigit():
#             taletavsumman += int(tal)
#     return taletavsumman



# a = input("mata n")
# print(SumAllDigitsIntext(a))











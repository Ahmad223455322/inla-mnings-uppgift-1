# while True:

#     x=int(input("mata in ett tal"))
#     y=int(input("mata in ett tal"))
#     sm = x +y
#     sel = input(f'summa är {sm} vill du fortsätta')
#     if sel == "J" or sel == "j":
#         continue
#     else:
#         break


# summa =0
# for i in range(10): 
#     x=int(input("mata in ett tal"))
#     summa +=x
# print(f' summan är {summa}')



# tal=int(input("mata in ett tal"))
# for x in range(tal,0,-1):
#     print(x)
   
# lista=[]
# störst = 0
# for x in range(4):
#     tal=int(input("mata in ett tal"))
#     lista.append(tal)
#     for t in lista:
#         if t > störst:
#             störst = t
#             minst = störst
#     for m in lista:
#         if m < minst:
#             minst = m        
            
# print(f"stösta talet är {störst}")            

# print(f"minsta talet är {minst}")            


# summa = 0
# lista=[1,2,4,5,4,3,4,5]
# for tal in lista:
#     summa=summa+tal
# print(summa)    

# cont= 0
# SampleList = ['abc', 'xyz', 'aba', '1221']
# for item in SampleList:
#     if len(item)>= 2 and item[0] == item[-1]:
#         cont = cont+1
# print(cont)        


# lita = [1,1,1,1,1,1,2,3,4,]
# nylista=[]
# for x in lita:
#     if x not in nylista:
#         nylista.append(x)
# for i in nylista:
#     print(i)        




# förstabostav=True
# bostavefteravstånd=False
# namn="kurt andersson"
# nynamn=""
# for bokstav in namn:
#     if förstabostav==True or bostavefteravstånd == True:
#         nynamn+=bokstav.upper()
#     else:
#         nynamn+=bokstav
#     förstabostav = False
#     if bokstav == " ":
#         bostavefteravstånd =True
#     else:
#         bostavefteravstånd =False

# print(nynamn)                    
        

# text ="Detta är en sträng som du skall ändra"
# nytext=""
# for x in text:
#     if x == " ":
#         nytext=nytext+x.replace(x,"*")
#     else:
#         nytext+=x
# print(nytext)                


# text ="Detta är en sträng som du skall ändra"
# cont = 0
# for x in text:
#     if x == " ":
#         text=text.replace(" ","*")
#         cont+=1
# print(text)
# print(cont)        
                

# text ="Detta är en sträng som du skall ändra"
# text=text.split()
# print(len(text))

# text ="Detta är en sträng som du skall ändra"
# print(len(text))


# while True:
#     x="@"
#     y="."
#     mail="ahmadzrzr97@gmailcom"
#     snabala=mail.find("@")
#     dot=mail.find(".")
#     leng= len(mail)
#     antalefter= 0
#     if x in mail and y in mail:
#         print("ok")
#     elif snabala == -1 or dot == -1 or antalefter <2 or antalefter >3:
#         print("inte ok")
#     break

            



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



# def räknabostav(lista):
#     text=""
#     for x in lista:
#         text+=x
#     return len(text)

# cities = [ "Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London"]
# print(räknabostav(cities))



# def rensaord(text):
#     badWords = ["work", "job", "boss", "vegetables", "fish"]
#     for bokstav in badWords:
#         text= text.replace(bokstav,"****")
#     return text

# a=input("mata in text")
# print(rensaord(a))        
        




# def isvalidpassword(lösnenord):
#         if len(lösnenord) >= 8:
#             CanNotBeInclusive= ["hej","lösen","hopp"]
#             for ord in CanNotBeInclusive:
#                 if ord in lösnenord:
#                     return False
#             antalstora=0
#             antalsmå = 0
#             antalsympols = 0
#             symols ="@$!#&*%_"
#             for x in lösnenord:
#                 if x.islower():
#                     antalsmå+=1
#                 if x.isupper():
#                     antalstora+=1
#                 if x in symols:
#                     antalsympols+=1

#             if antalsympols >=1 and antalstora >=2 and antalsmå >=2:
#                 return True
#         return False        
                                    

# password = "AHA_*mad"
# print(isvalidpassword(password))
     
    











# Skapa en klass ChristmasPresent. Den ska ha Name och ett
#  Price (vad den kostar) 
# Skapa en klass Person. Den ska ha Name och en lista med julklappar. 
# Gör också så att det går att lägga till julklappar, och räkna fram 
# totalen (vad alla personens julklappar kostar)
# Skapa nu (i main) tre personer.  Skapa några julklappar för varje 
# person och skriv en loop som går igenom alla personer,
# skriver ut dess namn och vad dess julklappar kostar.    OBS:
# #  tänk på god OOP.  
# Exempel på hur programmet ska se ut när man kör det:
# Stefan - ska få julklappar för totalt 4815kr
# Kerstin - ska få julklappar för totalt 15kr
# Oliver - ska få julklappar för totalt 1112 kr 


# class ChristmasPresent:
#     def __init__(self,namn:str,pris:int):
#         self._namn =namn
#         self._pris = pris


#     def getpris(self):
#         return self._pris




# class person:
#     def __init__(self,namn:str):
#         self._namn=namn
#         self._julklappar : list[ChristmasPresent]=[]


#     def addjulklapp(self,julklapp:str):
#        return self._julklappar.append(julklapp)            

#     def räknatotal(self):
#         summa = 0
#         for x in self._julklappar:
#             summa+= x.getpris()
#         return summa

#     def getnman(self):
#        return self._namn    

# lista : list[person] =[]

# antal=input("antal personer")
# i=0
# while i < int(antal):
#     person1=person(input("namn på person"))
#     presnt1=ChristmasPresent(input("nman på present"),int(input("pris")))
#     person1.addjulklapp(presnt1)
#     lista.append(person1)
#     i+=1


# total=0
# for per in lista:
#     julkla =per.räknatotal()
#     total+= julkla
#     print(f'{per.getnman()} - ska få julklappar för totalt {per.räknatotal()} totala alla är {total}')




# def translete(text:str)->str:
#     nytext=""
#     vokallista =["a","e","i","o","u","ö","y","ä","å", " "]
#     for bokstav in text:
#         if bokstav not in vokallista:
#             nytext=nytext+bokstav+"o"+bokstav
#         else:
#             nytext+=bokstav
#     return nytext


# a=input("mata")     
# print(translete(a))  


# def hitta(text)->str:
#     vokallista =["a","e","i","o","u","ö","y","ä","å"]
#     for bokstav in text:
#         if bokstav in vokallista:
#             return True
#         return False

# print(hitta("f"))            


# total=0
# poänglista =[]
# for rank in range(1,6):
#     poängfråndomare= float(input(f"poäng från domare: {rank}"))
#     poänglista.append(poängfråndomare)

    
# poänglista.remove(min(poänglista))
# poänglista.remove(max(poänglista))
# for tal in poänglista:
#     total+=tal
    
    

# snittPoint = total / len(poänglista)
# treDecimaler = format(snittPoint,".3f")
# print(treDecimaler)

# class Team:
#     def __init__(self,namn:str,antalvunna:int,atalforlorade:int,oavgjordematcher:int):
#         self._namn=namn
#         self._antalvunna=antalvunna
#         self._antalforlorade=atalforlorade
#         self._oavgjordematcher=oavgjordematcher



#     def poäng(self)->int:
#        poäng= self._antalvunna * 3 + self._oavgjordematcher
#        return poäng

#     def getnamn(self)->str:
#         return self._namn

#     def getantalvunna(self)->int:
#         return self._antalvunna

#     def getantalforlorade(self)->int:
#         return self._antalforlorade

#     def getoavgjordematch(self)->int:
#         return self._oavgjordematcher
        
   
# lista : list[Team] =[]
# for x in range(3):
#     team1=Team(input("namn på Team"),int(input("antal vunna")),int(input("antal vunna")),int(input("oavgjorda matcher")))
#     lista.append(team1)
# n=input("n")
# if n == "n" or n =="N":
#     for per in lista:
#         print(f'{per.getnamn()}, {per.getantalvunna()}, {per.getantalforlorade()}, {per.getoavgjordematch()}  ,{per.poäng()}')



# from datetime import datetime


# första= (input("mata in ett datum"))
# andra = (input("mata in ett till datum"))
# p_första = datetime.strptime(första, "%Y-%m-%d")
# p_andra = datetime.strptime(andra, "%Y-%m-%d")
# p_första = p_första.date()
# p_andra = p_andra.date()

# mella_skilnad= p_första - p_andra
# print(f"skilnad dagar mellan dessa datumen är{mella_skilnad.days} dagar")
       
        



    
# def removnegativa(lista:list)->list:
#     nylista=[]
#     for tal in lista:
#         if tal >= 0:
#             nylista.append(tal)
#     return nylista

# lista=[1,345,-222,45,6669,0,21]
# print(removnegativa(lista))  
# for x in removnegativa(lista):
#     print(x)              



# def sumalldigit(sträng:str)->int:
#     total=0
#     for tal in sträng:
#         if tal.isdigit():
#             total+=int(tal)
#     return total

# a=input("mata in ")
# print(sumalldigit(a))            


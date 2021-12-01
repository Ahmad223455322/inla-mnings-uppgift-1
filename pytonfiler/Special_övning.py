# # #Fråga 1
# class Team:

#     def __init__(self,namn,antal_vunna,antal_förlorade,avgojrda_match):

#         self._namn = namn

#         self._antalvunna = int(antal_vunna) #glöm ej lägga int om det är sifror som matas in 

#         self._antalförlorade = int(antal_förlorade)

#         self._avgjorda_match = int(avgojrda_match)



#     def Poäng(self):

#         resultat = self._antalvunna * 3 + self._avgjorda_match # Lägga alltid i en variabel för returnera om det är en beräkning 

#         return resultat
       
#     def skriv_ut (self):
#         poäng= self.Poäng()
#         utskrifta =  f'{self._namn},{self._antalvunna},{self._avgjorda_match},{self._antalförlorade},{poäng}'
#         utskrifta=utskrifta.split(",") # splitt gör definera varje item i en plats för splitt omvandlar sträng till list
#         return utskrifta
       

# lista_team= []
# while True:
# # om man vill ta input från class,
# # skapar man variabel med input och skriver in meddelande som användren ser,
# # sen det beror på hur många parametrar man har i classen, man skriver varibler till 
# # dessa parametrar och sen tilldela de till förta varibel_namnet.split() som skapdes med input
# # därefter skapar man förta objktet dvs = class () i paranteser skriver man
# # varibelna som man skapat till parameterna 
#     namn= input("Skriv in <Namn> <Antal vunna> <Antal förlorade> <Oavgjorda matcher>: ")
#     if namn == "N" or namn == "n":
#         for x in lista_team:
#             print(x)
#         break

#     namn_1 , antal_vunna,antal_förlorade,avgjorde_match = namn.split()
#     Fösta_team =Team(namn_1 , antal_vunna,antal_förlorade,avgjorde_match)
    
#     lista_team.append(Fösta_team.skriv_ut())
#     print(*lista_team)


#Fråga 2

# from datetime import date
# while True:
#     datum= input("Skriv in datum: <YYYY><MM><DD>")

#     datum=datum.split(" ")

#     år=int(datum[0])

#     månad=int(datum[1])

#     dag=int(datum[2])

# om man vill om vandla sträng till lista för underlätta och indexera 
# det man får från användaren om det är mer en variabel och en sträng
# då kan man göra på det sättet ovan på 


    # d0 = date(år, månad, dag)

    # d1 = date(år, 12, 20)



    # if dag > 20 and månad==12:

    #     d1=date(år+1, 12, 20)

    #     delta = d1-d0

    #     print(delta.days)

    # else:

    #     delta = d1 - d0

    #     print(delta.days)
    



#Fråga 3 

# kom ihåg att kolla på frågan ordentlig och läs igenom det.
# 

# def  filterContains(inlst,filter):
#     resultat=[]
#     for carakter in filter:
#         for ord in inlst:
#             if (carakter) in (ord):
#                 resultat.append(ord)
#     return (resultat)



# kontrollLista=["Herro", "234", "Namn", "hej på dig", "frukt"]

# filterLista=["rr","2"]
# print(filterContains(kontrollLista, filterLista))


#fråga 4

# import random


# lista=["Jag mår bra",

# "Lämna mig ifred",

# "Vad sa du?",

# "whatever",

# "Kanske det",

# "Ingen aning",

# "Ja vad bra",
# "du är ful"]

# def randdom_svar(lista):
#     x = random.choice(lista)
#     return x

# while True:
#     svar= input("Hur kan jag hjälpa dig")
#     print(f'chatbot: {randdom_svar(lista)}')  



#Fråga 5
lista=[12,44,5,-5,553]
lista.sort()
[print(x)for x in lista]
print(50 *"*")
lista.sort(reverse=True)
[print(x)for x in lista]                     



    
   


  # import random
# middag = ["pizza","taco", "tahi", "hamburgare", "pasta"]
# veckodag= ['måndag','tisdag','osndag','torsdag','fredag', 'lördag','söndag']
# for i in range (7):
#     print(veckodag[i]+ ':  '+ random.choice(middag))

# for i in range(10,0,-1):
#     print(i)




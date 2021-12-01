#Fråga 10




# inmatning = input("Mata un en text")
# inmatning=inmatning.split()
# längsta_ordet=""

# for ord in inmatning:
#     if len(ord) > len(längsta_ordet):
#         längsta_ordet=ord
# print(längsta_ordet)

# kortasteordet= längsta_ordet 
# for ord in inmatning:
#     if len(ord) < len(kortasteordet):
#         kortasteordet=ord

# print(kortasteordet)        
          

       
# inmatning =[1,2,10,3,5]
# störst = 0
# for tal in inmatning:
#     if tal > störst:
#         störst = tal
# print (störst)        
# minst = störst
# for t in inmatning:
#     if t < minst:
#         minst = t
# print(minst)        


            



# tal = [ 9, 3, 7, 2, 1, 3, 4, 4, 2, 5, 75, 4, 2, 67 ]
 

# Ta fram alla tal som är mellan 3 och 9 (EJ INKLUSIVE)   från denna lista och sortera talen i storleksordning med det största talet först. 

# Resultatet får INTE innehålla dubbletter. 

# Skriv också såklart en loop som skriver ut alla tal i den sorterade resultatlistan

 

# Klistra in all kod i textrutan nedan.  
# 

# tal_lista = [ 9, 3, 7, 2, 1, 3, 4, 4, 2, 5, 75, 4, 2, 67 ]
# ny_lista = []
# for tal in tal_lista:
#     if tal < 9 and  tal > 3:
#         print(tal)
# print(20*"*")        

# for siffra in tal_lista:
#     if siffra  not in ny_lista:
#         ny_lista.append(siffra)
# ny_lista.sort(reverse=True)
# for item in ny_lista:
#     print(item)    



# text = input("Mata ii en text")
# taletavsumman =0
# for tal in text:
#     if tal.isdigit():
#         taletavsumman += 1

# print(f'Resultatet är {taletavsumman}')



# Skapa en klass Person. Den ska ha Name och BirthDate.

# Skriv ett program som ber användaren mata in antal personer.

# Mata in namn och birthdate  - personerna läggs  sen i en lista. 

# Skriv sedan ut hur många hela dagar gammal respektive person är (samt dess namn naturligtvis).

# Samt skriv ut hur många hela dagar gamla de är tillsammans.

# Programmet ska vara dynamiskt, det vill säga kör man programmet i morgon med exakt samma datum så ska alla personer vara en dag äldre.

# Klistra in all kod för klasserna samt koden som skapar instanserna i textrutan nedan.

# Exempel på hur programmet ska se ut när man kör det:

 

# Antal personer? 3
# Namn person 1: Stefan
# Födelsedag person 1: 1972-08-03
# Namn person 2: Josefine
# Födelsedag person 2: 2002-03-30
# Namn person 3: oliver
# Födelsedag person 3: 2008-05-28
# Stefan är 16988 antal dagar gammal.
# Josefine är 5743 antal dagar gammal.
# Oliver är 12952 antal dagar gammal.
# De är tillsammans 35683 dagar gamla.


# from datetime import datetime


# class Person:
#     def __init__(self,namn:str,birthday:datetime):
#         self._namn = namn
#         self._birthday = birthday
    
 
#     def getnamn(self)->str:
#         return self._namn


#     def räkna_antal_dagar(self)->int:
       
#         nu_tid= datetime.now()
#         födelse =datetime.strptime(self._birthday,"%Y-%m-%d")
#         antaldagar= nu_tid - födelse
#         return antaldagar.days

    

# svar = int(input("antal personer"))
# i = 1

# personer_lista :list [Person] = []
# while i < svar+1:
 
#     person1 = Person (input(f"Namn på person {i}: "),input(f"Födelsedatum på person {i}:"))
#     personer_lista.append(person1)  
#     i =i+1
# toatal_dagar = 0
# for person in personer_lista:
#    antal_dagar = person.räkna_antal_dagar()
#    toatal_dagar+=antal_dagar
#    print(f'{person.getnamn()} är {antal_dagar}antal dagar gammal')
    
#    print(f'De är tillsammans {toatal_dagar} dagar gamla')   
   





# def något(x:int):
#     x=x+1
#     print(x,end=',')
# x=3
# print(x,end=',')
# något(x)
# print(x,end=',')



# Skriv ett program som slumpar fram djurnamn! 

# Skapa en funktion GetAnimalName( minChars, maxChars )

# funktionen ska slumpa fram ett djurnamn - av alla namn i listan nedan som matchar filtret minChars och maxChars.  

# Dvs GetAnimalName(7,9) - ska ge ett slumpmässigt namn av alla namn som består av 7-9 bokstäver

# PS: finns ingen alls som matchar så skall  "" (tom sträng) returneras

# (mellanslag räknas som ett tecken!)








# def GetAnimalName( minChars, maxChars ):
#     import random
#     lista = ["MacGyver","MacGonagall","MacDonald","Macahan","MacThurbo","Pascal","Pilot","PingPong", "Kristall","Pucko", "Prinsessa","Bubblan","Fjollan", "Filur", "Baron von Münchausen","Tiny Toledo","Zelda","Miss Maxina", "Zolita", "Oscar", "Leya",  "Tequila",  "Sunrise", "Bruce", "Lennart", "Greger", "Gunnar", "Gunnel","Blåbär","Billy","Bob","Sigbritt" ]
#     nylista=[]<
#     for animal in lista:
#         if len(animal) > int(minChars) and len(animal)  < int(maxChars):
#             nylista.append(animal)
#             slump=random.choice(nylista)
#             return slump

#     if len (nylista) == 0:
#           return " "
       
       
# while True:
  
#     a =input("mata in minChars") 
#     b= input("mata in  maxChars")
#     print(GetAnimalName(a,b))                














 # tal_lista = [ 9, 3, 7, 2, 1, 3, 4, 4, 2, 5, 75, 4, 2, 67 ]
# ny_lista = []
# for tal in tal_lista:
#     if tal < 9 and  tal > 3:
#         print(tal)
#         print(20*"*")        

#     for siffra in tal_lista:
#         if siffra not in ny_lista:
#             ny_lista.append(siffra)
# ny_lista.sort(reverse=True)
# for item in ny_lista:
#     print(item)    





# Tentamen 1

# Din identitet är dold under rättning.
# Status: Väntar på bearbetning av lärare

# Antal tillåtna försök: 1. Du håller på med försök 1

# Du har angivit rätt svar
# Rätt svar
# Du har angivit fel svar
# Fråga 1

# Skapa en klass Person. Den ska ha Name och BirthDate.

# Skriv ett program som ber användaren mata in antal personer.

# Mata in namn och birthdate  - personerna läggs  sen i en lista. 

# Skriv sedan ut hur många hela dagar gammal respektive person är (samt dess namn naturligtvis).

# Samt skriv ut hur många hela dagar gamla de är tillsammans.

# Programmet ska vara dynamiskt, det vill säga kör man programmet i morgon med exakt samma datum så ska alla personer vara en dag äldre.

# Klistra in all kod för klasserna samt koden som skapar instanserna i textrutan nedan.

# Exempel på hur programmet ska se ut när man kör det:

 

# Antal personer? 3
# Namn person 1: Stefan
# Födelsedag person 1: 1972-08-03
# Namn person 2: Josefine
# Födelsedag person 2: 2002-03-30
# Namn person 3: oliver
# Födelsedag person 3: 2008-05-28
# Stefan är 16988 antal dagar gammal.
# Josefine är 5743 antal dagar gammal.
# Oliver är 12952 antal dagar gammal.
# De är tillsammans 35683 dagar gamla.

# Maxpoäng: 3

# Fråga 2

# Skriv ett program som slumpar fram djurnamn! 

# Skapa en funktion GetAnimalName( minChars, maxChars )

# funktionen ska slumpa fram ett djurnamn - av alla namn i listan nedan som matchar filtret minChars och maxChars.  

# Dvs GetAnimalName(7,9) - ska ge ett slumpmässigt namn av alla namn som består av 7-9 bokstäver

# PS: finns ingen alls som matchar så skall  "" (tom sträng) returneras

# (mellanslag räknas som ett tecken!)

 

# Använd följande lista som bas:

# lista = [   "MacGyver",

#             "MacGonagall",

#             "MacDonald",

#             "Macahan",

#             "MacThurbo",

#             "Pascal",

#             "Pilot",

#             "PingPong",

#             "Kristall",

#             "Pucko",

#             "Prinsessa",

#             "Bubblan",

#             "Fjollan",

#             "Filur",

#             "Baron von Münchausen",

#             "Tiny Toledo",

#             "Zelda",

#             "Miss Maxina",

#             "Zolita",

#             "Oscar",

#             "Leya",

#             "Tequila",

#             "Sunrise",

#             "Bruce",

#             "Lennart",

#             "Greger",

#             "Gunnar",

#             "Gunnel",

#             "Blåbär",

#             "Billy",

#             "Bob",

#             "Sigbritt"

#          ]

 

 

# Klistra in all kod för klasserna samt koden som skapar instanserna i textrutan nedan.


# Maxpoäng: 3

# Fråga 3

# Vad skriver programmet ut när det körs?



 

 


# 3,4,5,

# 3,4,4,

# 3,3,4,

# 3,4,3,
 
# Poäng: 1 av 1

# Fråga 4

 
# Skriv ett program som ber användaren mata in en text. Kolla hur många SIFFROR det finns i den inmatade texten
 
# Dvs
 
# Hej jag är 49 år och jag har 2 ögon och 2 ben.
 
# Resultat:  4 siffror matades in
 

 


# Maxpoäng: 3

# Fråga 5

# Utgå från följande lista.

# tal = [ 9, 3, 7, 2, 1, 3, 4, 4, 2, 5, 75, 4, 2, 67 ]
 

# Ta fram alla tal som är mellan 3 och 9 (EJ INKLUSIVE)   från denna lista och sortera talen i storleksordning med det största talet först. 

# Resultatet får INTE innehålla dubbletter. 

# Skriv också såklart en loop som skriver ut alla tal i den sorterade resultatlistan

 

# Klistra in all kod i textrutan nedan.


# Maxpoäng: 3

# Fråga 6

# Utgå från följande lista:

# cities = [ "Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London" ]
 

 

# Skriv en funktion som räknar ut totala antalet bokstäver i en lista som den ovan. Dvs summan av längden av alla element

 

# Klistra in all kod  nedan (skriv kod såklart som anropar funktionen också och skriver ut summan)


# Maxpoäng: 3

# Fråga 7

# Av vilken anledning körs Pythonprogram vanligen långsammare än ett C-program?


# I C lagras all data /variabler på stacken och blir därigenom inte utspridda i minnet
 

# python:s källkod består av fler filer än C-programmets dito

# python blir till assembler medan C-programmet blir maskinkod

# python är interpreterande medan C-programmet kompileras till maskinkod
 
# Poäng: 0 av 1

# Fråga 8

# Vad är sant gällande variabler i Python?


# en variabel är inte bunden till en viss datatyp utan typen för variabeln kan ändras när progranmmet körs
 

# när en variabel skapas så bestämmer man vilken datatyp hädanefter alltid ska lagras i den
 

# en variabel kan bara innehålla ett enda värde

# en variabel kan inte byta värde under programmets gång
# Poäng: 0 av 1





# Fråga 10

# Skriv ett program som matar in en text. För att förenkla kan vi säga att den ENDA separatorn mellan olika ord är mellanslag.

# Efter detta ska du  ta fram det längsta och det kortaste ordet och skriva ut. OBS: inte genom att använda inbyggda sorterings-rutiner utan genom en for-loop och gå igenom alla  värden

# Skriv ut resultatet, ex:

# Mata in text:

# hej vilken fin dag hoppas det blir roligt

# Längsta ordet var:vilken

# Kortaste ordet var:hej

# Klistra in kod i rutan nedan

 


# Maxpoäng: 3

# Fråga 11

# Vad anses som den stora fördel med s.k ENUMs av följande alternativ


# enums ger mer läsbar kod och fungerar dessutom som hjälp/dokumentation för utvecklaren så misstag kan undvikas
 

# enum är snabbare än strängar

# enum kommer ligga på den s.k heapen och är därför modifierbara från andra funktioner

# enums ger oss möjlighet till bättre variabelnamn och därigenom förbättrar kodkvaliteten och läsbarheten
 
# Poäng: 0 av 1




#######################################################


# 1. fråga hur många tal som ska matas in

# 2. matar in så många tal (ints) in i en lista

# 3. Nu ska du anropa en metod swap() som tar en  lista med tal och returnerar en ny lista med tak

# 4. Det som ska hända i den metoden är att alla tal ska byta plats med sin närmaste granne ex

# [0,4,11,45,2,67]

# Ska bli

# [4,0,45,11,67,2]

# Dvs pos 0 swappar med pos 1, pos 2 swappar med pos 3 osv osv

 

# Avsluta med att skriva ut varje tal på egen rad:

# Ex:

 

# Hur många tal:5

# Mata in ett tal:3

# Mata in ett tal:1

# Mata in ett tal:9

# Mata in ett tal:99

# Mata in ett tal:2

# 1

# 3

# 99

# 9

# 2
# def swep(lista):
#     nylista=[]
#     första_index = True
#     for i in lista:
#         if första_index == True:
#             udda = i
#             första_index =False

#         else:
#             nylista.append(i)
#             nylista.append(udda)
#             första_index = True
#     return nylista  
    
              
# lista = []

# inmatning = int(input("Hur månnga vill du mata in"))
# i = 0
# lista = []

# while i < inmatning: 
#     siffra = int(input("Mata in tal i lista"))
#     lista.append(siffra)
#     print(swep(lista))
#     i+=1

# for t in swep(lista):
#     print(t)   



def bytaplatspåord(lista:list)->list:
    nylista=[]
    firstord= True
    for ord in lista:
        if firstord== True:
            uddaindex= ord
            firstord = False
        else:
            nylista.append(ord) 
            nylista.append(uddaindex)
            firstord = True
    return nylista
lista=[]
while True:
    inmatning= input("mata ord i lista")
    lista.append(inmatning)
    print(bytaplatspåord(lista))








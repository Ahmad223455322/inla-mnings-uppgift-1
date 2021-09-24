# antalmjölk=int(input("mata in hur många mjölk finns det kvar"))
# if antalmjölk < 10:
#     print ("du behöve beställa 30 paket")
# elif antalmjölk >= 10 and antalmjölk <= 20:
#     print("fdvvvdfb b")
# else:
#     print("dfbdf")    

# tal1= int(input("mata in ett tal"))
# tal2= int(input("mata in ett tal"))
# if tal1 > tal2 :
#     störst = tal1
#     print(störst)
# elif tal2 > tal1:
#     störst = tal2
#     print(störst)    


# print("vuxen","student","pentioner")
# val = input("ange val")
# if val == "pentioner" or val == "student":
#     print("resan kostar 20 kr")
# elif val == "vuxen":
#     print("resan kostar 30 kr")    
# else:
#     print(" du gav felaktigt val försök att ange igen")    

# for x in range(11):
#     print(x)

# x = 0 
# while x != 11:
#     print(x)
#     x+=1



# tal1 =int(input("mata in ett tal"))
# tal2= int(input("mata in ett tal"))


# while tal1 < tal2 :
#     print(tal1)
#     tal1+=1

# while True:
#     tal1 =int(input("mata in ett tal"))
#     tal2= int(input("mata in ett tal"))
#     summma = int(tal1) + int(tal2)
#     print (summma)
#     val = input(" vill du fortsätta")
#     if val == "j" or val == "J":
#         continue
    

#     else:
#         break


# summa = 0
# for x in range(10):
#        tal1=(int(input("mata in ett tal")))
#        summa = summa + tal1
# print  (summa)

# tal = 0
# tal1=(int(input("mata in ett tal")))
# while tal1 > tal:
#     print(tal1)
#     tal1 = tal1-1


# listor

# minlista=[]
# for x in range (4):
#   tal= int(input("mata in ett tal"))
#   minlista.append(tal)

    
# störst = 0
# for i in minlista:
#     if i > störst:
#         störst = i
# print (störst)       


# summa=0
# tal=[4,3,3,34,5,]
# for x in tal:
#     summa= summa +x
# print(summa)

# resultat = []
# text =[3,5,5,5,3,2]
# for x in text:
#     if x not in resultat:
#         resultat.append(x)
        
# print (resultat)         

# resultat= 0
# lists=["abba", "224422", "1221","fddfvfdvdfvv","vfvvvffgh"]
# for x in lists:
#     if len(x) >= 2 and x[0]== x[-1]:
#         resultat+=1
# print(resultat)        


# minlista= ["2","2","3","3","2","1","5"]
# minnylista=[]
# for x in minlista:
#     if x not in minnylista:
#         minnylista.append(x)
# print(minnylista)        



# minlista=["aassd","ewsss","qww","wqqq"]
# minnylista =[]
# n =3
# for x in minlista:
#     if len(x)> n:
#         minnylista.append(x)
# print(minnylista)        


# st=[]
# for fråga in range (3):
#     fråga = input("mata in en sträng")
#     st.append(fråga)
   
# print(st[0])
# print(st[1])
# print(st[2])

# string = "Hello world"
# x = string.find("w")
# print (f"position bokstaven w har i strängen {x}")

# namn = "ahmad zarzar"
# forstaboksta = True
# andrabokstav = False
# nynamn = ""
# for x in namn:
#     if forstaboksta == True or andrabokstav == True:
#         nynamn+= x.upper() 
#     else:
#         nynamn+=x
#     forstaboksta =False
#     if andrabokstav == " ":
#         andrabokstav =True
#     else:
#         andrabokstav = False      

namn = "leif stefan holmberg" #Leif Stefan Holmberg
nyttNamn = ""
FirstLetter = True
LastLetterWasSpace = False

for bokstav in namn:
    if FirstLetter == True or LastLetterWasSpace == True:
        nyttNamn = nyttNamn + bokstav.upper()
    else:
        nyttNamn = nyttNamn + bokstav
    FirstLetter = False
    if bokstav == " ":
        LastLetterWasSpace = True
    else:
        LastLetterWasSpace = False
print(nyttNamn)        
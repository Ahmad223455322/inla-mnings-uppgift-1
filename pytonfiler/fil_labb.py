# for x in range(11):
#     print(x)

# i= 0
# while i < 11:
#     print(i)
#     i=i+1






# x = int(input("Mata in ett tal")) 
# y = int(input("Mata in ett tal")) 
# for i in range(x+1,y):
#     print(i)  

# x = int(input("Mata in ett tal")) 
# y = int(input("Mata in ett tal")) 

# i = x
# while i < y-1:
    
#     i=i+1
#     print(i)




# lista =["1.plusa","2.minska","3.upphjöd"]
# for item in lista:
#     print(item)
# while True:
#     sel = input("vad vill du göra")
#     x = int(input("Mata in ett tal")) 
#     y = int(input("Mata in ett tal"))
#     if sel == "1":
#         summa = x +y 
#         print (f' Summan är :{summa}')
#     elif sel == "2" :
#         subrta = x - y 
#         print (f' Summan är :{subrta}')
#     elif sel == "3":
#         upphj= x ** y
#         print (f' Summan är :{upphj}')   
#     svar = input("vill du fortsätta J/N?")
#     if svar == "j" or svar == "J":
#         continue
#     elif svar == "n" or svar == "N":
#         break





# summa = 0
# for i in range(10):
#     x = int(input("Mata in ett tal")) 
#     summa += x

#     print(summa)




# summa = 0
# x = 0
# while x < 10:
#     tal = int(input("Mata in ett tal")) 
#     summa += tal
#     x +=1
# print(summa)    





# tal = int(input("Mata in ett tal")) 
# for x in range(tal-1,0,-1):
#     print(x)





# import random
# while True:
#     x = random.randint(1,6)
#     y = random.randint(1,6)
#     print("Värdet är nedan")
#     print(x)
#     print(y)
#     svar = input("vill du rolla tärningar igen")
#     if svar == "y" or svar == "yes":
#        continue
#     else:
#         break




# tal_lista =[]
# störst = 0
# for x in range(4):
#     tal = int(input("Mata in ett tal"))
#     tal_lista.append(tal)
#     for item in tal_lista:
#         if item > störst:
#             störst=item
# print(f'stösta talet är{störst}')        





# tallist=[1,2,3,4,5,6,7]
# störst = 0
# summa = 0
# for x in tallist:
#     if x > störst:
#         störst = x
#     summa+=x
# print(summa)  
# print(störst)  
    



# SampleList = ['abc', 'xyz', 'aba', '1221',"zaz"] 
# count = 0
# for x in SampleList:
#     if len(x) >= 2 and x[0] == x[-1]:
#         count+=1
# print(f'Antalet är {count}')        
           




# tal_utan = []
# tal_lista_med_dubbel=[1,1,1,2,3,3,4,2]
# for x in tal_lista_med_dubbel:
#     if x not in tal_utan:
#         tal_utan.append(x)
# print(tal_utan)        





# ordlista = ["Ahmad","aa","www","rrr"]
# annan=[]
# n = 3
# for x in ordlista:
#     if len(x) > n:
#         annan.append(x)
# for i in annan:
#     print(i)        

    



# import sys
# from termcolor import colored
# board = []

# for i in range (8):
#     row = [' ' for i in range (8)]

#     board.append (row)
#     if i == 1:

#        b1=colored("'b'", color="red")

#        row = [b1 for i in range (8)]



#     elif i == 6:

#        b1=colored("'b'", color="green")

#        row = [b1 for i in range (8)]

   

#     elif i != 1 or i !=6:

#        row = ["' '" for i in range (8)]



#     print (("["+",".join(map(str, row)))+"]")   





# svar = input("mata in en sträng")
# svar2 = input("mata in en sträng")
# svar3= input("mata in en sträng")  

# print(f'{svar}  {svar2}  {svar3}')




# sträng="Hello, world"
# sträng = sträng.split()
# sträng="".join(sträng)
# for x in sträng:
#     if x == "w":
#         print(x)

# print(f'w har index nr {sträng.find("w")}' )
# # 
# # 
# 
#        

# namn = "ahmad zarzar"
# förstabokstav = True
# första_efter_avstånd = False
# nynamn =""
# for x in namn:
#     if förstabokstav == True or första_efter_avstånd == True:
#        nynamn+=x.upper()
#     else:
#         nynamn = nynamn+x
#     förstabokstav = False
#     if x == " ":
#         första_efter_avstånd = True

#     else:
#         första_efter_avstånd= False
# print(nynamn)




# Steäng ="Detta är en sträng som du skall ändra"
# count = 0
# for x in Steäng:
#     if x == " ":
#         Steäng=Steäng.replace(x,"*")
#         count+=1

# print(Steäng)
# print(count)        




# Steäng ="Detta är en sträng som du skall ändra"

# Steäng=Steäng.split()
# print(len(Steäng))



# myTuple = ("John", "Peter", "Vicky")

# x = "".join(myTuple)

# print(len(x))


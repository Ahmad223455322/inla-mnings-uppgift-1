# telregister ={}
# while True:
  
#   namn = input("vad har du för namn")
#   telnr = input(f"vilket telfonnummer har du {namn}" )
#   telregister[namn]= telnr 
     
#     if namn in telregister:
#          print (" fnns redan") 
#     else:
#                 telnr = input(f"vilket telfinnummer har du{namn}")
#                 telregister[namn]= telnr
#     if len(telregister)== 5:
#             break 

#     print ("Telregister lookup")
#     while True:

#      namn = input("Ange namn:"
#      if namn in dict:
#       telnr = telregister[namn]
#       print(f"Telnr:{telnr}")
#      else :
#          print("namet finns")
# inmatning={}
# menyA = ["1.Skapa konto", "2.logga in på konto", "3.Avsluta"]
# menyB = ["1.Ta ut pengar", "2.Sätt in pengar", "3.Visa saldo","4.Avsluta"] 

# while True:
#     print("****HUVUDMENY****")
#     for x in menyA:
#         print(x)
#     vala=input("Ange meny val") 
#     if vala == "1": 
#         kontonummer = int(input("Ange kontonummer"))
#         if kontonummer in inmatning:
#             print(" Kontot finns redan")
#         else:
#             inmatning[kontonummer] = 200
        
#     elif vala == "2":

#         kontonummer = int(input("Ange kontonummer"))
#         if kontonummer not in inmatning:
#             if kontonummer not in inmatning:
#                 print("Kontonummret hittades ej") 
#             continue        
#         while vala == "2":

#             print("****KONTOMENY****")
#             for x in menyB:
#                print(x)
#             valb=input("Ange meny val") 
#             if valb == "4":
#                 break 
#             if valb == "1":
#                 belopp = int(input("Ange belopp"))
#                 if belopp > inmatning[kontonummer]:
#                     print("Beloopet är större än saldot")
#                 else:
#                     inmatning[kontonummer] =  inmatning[kontonummer] - belopp
#                     fil= open('demo.txt',"a")
#                     fil.write(f"Tog ut {belopp}\n")
#                     fil.close()
#             if valb == "2":
#                 belopp = int(input("Ange belopp"))
#                 inmatning[kontonummer] =  inmatning[kontonummer] + belopp
#                 fil= open('demo.txt',"w")
#                 fil.write(f"satt in {belopp}")
#                 fil.close()
                
#             elif valb== "3":
        
#                 print(f"Saldo är{inmatning[kontonummer]}")
            
      

#     elif vala== "3":
#         break
#     else: 
#         print("Du har angett fel val, vänligen förs")


# Labb1 

# min_dic ={"namn":"Ahmad",
# "ålder": "24",
# "längden": "185"
# }

# keys=input("ange key")
# if keys in min_dic.keys():
#     print(" den är redan skapat")
# else:
#    print ("inte skapat")    

# print(min_dic)


#labb 2




# Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
# {"VIII":"S007"}]
# ny_sampel=[]

# for x in Sample_Data:
#     x_lista = list(x.values())
#     if x_lista not in ny_sampel:
#         ny_sampel.append(x_lista)
#     else:
#         continue    
        
   
   
# print(ny_sampel)


#labb 3 str1 = 
# str1='3srruwceeo' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)
  


#labb4



Sample_data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
val_list = list(Sample_data.values())
störst=0
min_lista=[]
störst2=0
for index in val_list:
    if index > störst:
        störst= index
        min_lista.append(störst)
      
print(störst)    

for index in val_list:
    if index > störst2:
        störst2= index
Sample_data.pop("item1")        

print(störst2)        
print(Sample_data)    


# störst = 0
# for i in minlista:
#     if i > störst:
#         störst = i
# print (störst)       

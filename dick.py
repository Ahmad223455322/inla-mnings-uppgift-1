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
inmatning={}
menyA = ["1.Skapa konto", "2.logga in på konto", "3.Avsluta"]
menyB = ["1.Ta ut pengar", "2.Sätt in pengar", "3.Visa saldo","4.Avsluta"] 

while True:
    print("****HUVUDMENY****")
    for x in menyA:
        print(x)
    vala=input("Ange meny val") 
    if vala == "1": 
        kontonummer = int(input("Ange kontonummer"))
        if kontonummer in inmatning:
            print(" Kontot finns redan")
        else:
            inmatning[kontonummer] = 200
        
    elif vala == "2":

        kontonummer = int(input("Ange kontonummer"))
        if kontonummer not in inmatning:
            if kontonummer not in inmatning:
                print("Kontonummret hittades ej") 
            continue        
        while vala == "2":

            print("****KONTOMENY****")
            for x in menyB:
               print(x)
            valb=input("Ange meny val") 
            if valb == "4":
                break 
            if valb == "1":
                belopp = int(input("Ange belopp"))
                if belopp > inmatning[kontonummer]:
                    print("Beloopet är större än saldot")
                else:
                    inmatning[kontonummer] =  inmatning[kontonummer] - belopp
                    fil= open('demo.txt',"a")
                    fil.write(f"Tog ut {belopp}\n")
                    fil.close()
            if valb == "2":
                belopp = int(input("Ange belopp"))
                inmatning[kontonummer] =  inmatning[kontonummer] + belopp
                fil= open('demo.txt',"w")
                fil.write(f"satt in {belopp}")
                fil.close()
                
            elif valb== "3":
        
                print(f"Saldo är{inmatning[kontonummer]}")
            
      

    elif vala== "3":
        break
    else: 
        print("Du har angett fel val, vänligen förs")


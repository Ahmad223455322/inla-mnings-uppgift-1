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
            inmatning[kontonummer] = 1000
        
    elif vala == "2":

        kontonummer = int(input("Ange kontonummer"))
        if kontonummer not in inmatning:
            print("Kontonummret hittades ej") 
            continue        
        while vala == "2":

            print(f"****KONTOMENY**** du är inloggad på kontot : {kontonummer}")
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
                    inmatning[kontonummer] -= belopp
                    
            if valb == "2":
                belopp = int(input("Ange belopp"))
                inmatning[kontonummer] += belopp
                
                
            elif valb== "3":
        
                print(f"Saldo är{inmatning[kontonummer]}")
            
    elif vala== "3":
        break
    else: 
        print("Du har angett fel val, vänligen försök igen")





    

    
        

    

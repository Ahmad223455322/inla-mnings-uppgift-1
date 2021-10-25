
# udda= False
# with open ("nman.txt","r")as Afil:
#     print(Afil)
    # for x in Afil:
    #     if udda ==False: 
    #       print(x)
    #       udda = True
    #     else:
    #           udda = False

            
#labb 1clösning 2
# udda = True    
# with open("Ahmad_fil.txt","r") as minfile:
#     for line in minfile:
#         if udda == True:
#             print(line)
#             udda=False
#         else:
#             udda= True    


#import os
# def deltet_(s):
#     if os.path.isfile(s):
#         os.remove(s)

# deltet_("Ahmad_4file.txt") 

# with open("Ahmad_2file.txt","w")as min_file:
#  with open("Ahmad_fil1234.txt","r")as forsta_fil:
#         #for line in min_file:
#            # forsta_fil.write(line)
#         with open("Ahmad_3file.txt","w")as båda_fil:
#          for line in forsta_fil:
#             båda_fil.write(line) 
#             # if os.path.isfile('Ahmad_3file.txt'):
#
#              #     os.remove     



# labb 3
# numm= 1
# with open ("Ahmad_resultatat.txt","w")as mottagen_fil:
#  with open ("Ahmad_fil.txt","r") as num_fil:
    
#     for line in num_fil:
#         mottagen_fil.write(f'{numm}- {line}')
#         numm +=1


# with open ("reultat_with_number.txt","w")as sista_data:
#   with open ("Ahmad_resultatat.txt","r")as mottagen_fil:
#     for lins in mottagen_fil:
#         sista_data.write(lins)


#labb2 lös1

# filenames = ['namn1.txt', 'namn2.txt']
# with open('namn3.txt', 'w') as a:
#     for names in filenames:
#         with open(names) as infile:
#             a.write(infile.read())
#         a.write("\n")'
# #labb2 lös2
# minafiler=['namn12.txt','namn21.txt']
# with open ('namn3.txt','w')as fil:
#     for namn in minafiler:
#         with open(namn) as inmatninig:
#             fil.write(inmatninig.read())
# #             fil.write('\n')

# with open('namn3.txt','a+') as fil:
#   for line in range:(4)
#   fil.write((line+1)%'sgfbfdbb %d\r\n' )
                

# with open("guru99.txt","w")as f:
#     f.write("This is line""\n")
#     f.write("This is line""\n")
#     f.write("This is line""\n")
#     f.write("This is line""\n")
#     f.write("This is line""\n")
#     f.write("This is line""\n")
     

# with open ("guru99.txt","r") as fs:
#     se = fs.read()
#     print(se)

# with open ("guru99.txt","a") as fk:
#     fk.write("7-Ahmadzarzar""\n")
#     print(fk)

# with open ("guru99.txt","r")as fs:
#     rad = fs.readline()
#     räkna = 1
#     while rad:
#          print("{}: {}".format(räkna,rad.strip())) 
#          rad = fs.readline()#
#          räkna+=1


# with open ("guru88.txt","w") as append:
#     for rad in fs:
#         rad = fs.readline()
   
# mail='@googel.se'

# with open ('guru99.txt', 'r')as fil:
#  with open ('ahmad.txt','w')as minamail:     
#     for rad in fil:
#        avstånd = rad.split(' ')
#        resultat=  avstånd[0]+'.'+avstånd[1].strip() + mail
#        resultat=resultat.lower()
#        print(resultat)
       
#        minamail.write(resultat+'\n')

# txt = "ditt kontonummer är: 239 och din saldo är: 200SEK."

# x = txt.find(":")
# print(x)
# #kontonummer_index=x+len("kontonummer är: ")
# #kontonummer=txt[kontonummer_index:(kontonummer_index+3)]
# #print(kontonummer)

# kontonummer_index = x
# konton




#labb 4
# minlsta=[]
# with open ("Ahmad_resultat.txt","w")as mottagen_fil:
#  with open ("Ahmad_data.txt","r")as data_fil:
#      minlsta=data_fil.readlines()
#      minlsta= sorted(minlsta,key=str.lower)
#      mottagen_fil.writelines(minlsta)
        

# labb 5
# min_dic={}
# meny =["1-logga in", "2-Registera nytt konto","3-Avsluta"]
# while True:
#     for val in meny:
#         print(val) 
#     sel = int(input("ange meny val")) 
#     if sel =="1" :
#         namn=input("Ange använderan namn") 
#         lösen= int(input("Ange lösenord"))
#     elif sel == "3":
#         break
#     elif sel == 2




import os

def GetUserLines():
    if not os.path.isfile("Lab5Users.txt"):
        return []
    with open("Lab5Users.txt", "r") as indataFile1:
        return indataFile1.readlines()


def UserExists(namn):
    for line in GetUserLines():
        parts = line.split("###")
        if len(parts) == 2:
            if parts[0].lower() == namn.lower():
                return True
    return False

def UserCorrectPassword(namn,pwd):
    for line in GetUserLines():
        parts = line.strip().split("###")
        if len(parts) == 2:
            if parts[0].lower() == namn.lower() and parts[1] == pwd:
                return True
    return False

def UserAdd(namn,pwd):
    with open("Lab5Users.txt", "a") as indataFile1:
        indataFile1.write(namn + "###" + pwd + "\n")

def Registrera():
    print("NY")

    while True:
        namn  = input("Ange användarnamn")
        if UserExists(namn):
            print("Redan taget")
            continue
        break

    pwd = input("Ange lösenord")
    UserAdd(namn,pwd)


def Login():
    print("Login")
    namn  = input("Ange användarnamn")
    pwd = input("Ange lösenord")
    if not UserExists(namn):
        return False
    if UserCorrectPassword(namn,pwd):
        return True
    return False


while True:
    print("Meny")
    print("a. Registrera")
    print("b. Logga in")
    sel= input("Välj->").lower()
    if sel == "a":
        Registrera()
    if sel == "b":
        if Login():
            print("Welcome")
        else:
            print("No access")
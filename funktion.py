
#labb 1
# def plusastringd(string1 , string2):
#     r = string1 +string2
#     return r
# a = "Ahmad"
# b= "Zarzar"
# resutat= plusastringd(a,b)

# print(resutat)
# #labb 2
# def räknamoms (momsvärde , priset):
#     summa= momsvärde * priset
#     return summa
# moms= float(input("Ange moms värde"))
# pris= int(input("ange priset"))
# momsvärd= räknamoms(moms,pris)
# print(f' momms ligger på {momsvärd}kr på denna varan')

#labb 3
# def IsMyndig(age):
#     if age >= 18:
#         return(f"Om du är {age} år du är myndig")
#     elif age < 18:
#         return(f"Om du är {age} år du är inte myndig")

# ålder = int(input("Ange ålder"))
# re= IsMyndig(ålder)
# print(re)

#labb 4
# def längst (ordlist):
#     längst = ""
#     for i in ordlist:
#         if len(i) > len(längst):
#           längst = i
#     return längst

# minlista= ["fvsdvv","sfvfdv","sdvrrrrr"]    
# print(längst(minlista))        


# papslista =[ "dfgfv","dfbdfbvv","gbfbdfvvfdvfvfd","zdfv"]
# print (längst(papslista))

#labb 5

# def CalculateTaxesOnSalary (lön):
#    if lön >= 30000:
#        return lön * 0.33
#    if lön < 15000:
#        return lön * 0.12
#    if lön < 30000:
#        return lön* 0.28
# resultat = CalculateTaxesOnSalary(16000)    
# print(resultat)           


# Skapa en metod som heter ToPercentage. Användaren skall mata in ett decimaltal mellan 1 och 0.
# Metoden omvandlar talet till procent tex skall 0.5 bli 50%.

#labb 6
# def tillprosent(inmatninig):
#     procent= inmatninig * 100

#     return procent 

# inmatninig = float(input("m,ata in ett tal"))
# svaret = tillprosent(inmatninig)
# print (svaret)


# Skapa en metod som tar en bokstav och returnerar true om det är en vokal och false annars.





#labb 7

# def vokal (vokallista):
#     for bokstav in text:
#         if bokstav not in vokallista:
#             print ("false")
#         else:
#             print("true") 

# text="tejnna"
# vokallista =["a","e","i","o","U","ö","y","ä","å"]  
# svar = vokal(vokallista)
# print(svar)        



#labb 8
   


# def IsVowel(letter):
#     vowels = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
#     return letter in vowels
# svar = IsVowel(letter) 
# print (svar)  





#test efter labbar



# def min_fun(*lista):
#     meny_list=["1Ta ut pengar", "2- Sätt in pengar", "3-Avsluta"]
#     for objekt in meny_list:
#       return lista
    
# resultar = min_fun(object)
# print(resultar)
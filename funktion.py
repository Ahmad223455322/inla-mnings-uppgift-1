# def plusastringd(string1 , string2):
#     r = string1 +string2
#     return r
# a = "Ahmad"
# b= "Zarzar"
# resutat= plusastringd(a,b)

# print(resutat)

# def räknamoms (momsvärde , priset):
#     summa= momsvärde * priset
#     return summa
# moms= float(input("Ange moms värde"))
# priset = int(input("ange priset"))
# momsvärde= räknamoms(moms,priset)
# print(momsvärde)

def IsMyndig(age):
    if age >= 18:
        return False
    elif age < 18:
        return True

age = int(input("Ange ålder"))
txt = "myndig"
if IsMyndig(age):
    txt = "ej " + txt
print(f"Om du är {age} år är du {txt}")


# def längst (ordlist):
#     längst = " "
#     for i in ordlist:
#         if len(i) > len(längst):
#           längst = i
#     return längst

# # minlista= ["fvsdvv","sfvfdv","sdvrrrrr"]    
# # print(längst(minlista))        


# papslista =[ "dfgfv","dfbdfbvv","gbfbdfvvfdvfvfd","zdfv"]
# print (längst(papslista))


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


# def tillprosent(inmatninig):
#     procent= inmatninig * 100

#     return procent 

# inmatninig = float(input("m,ata in ett tal"))
# svaret = tillprosent(inmatninig)
# print (svaret)


# Skapa en metod som tar en bokstav och returnerar true om det är en vokal och false annars.







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




   


# def IsVowel(letter):
#     vowels = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
#     return letter in vowels
# svar = IsVowel(letter) 
# print (svar)  

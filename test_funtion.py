# def ny_metod(metod1,metod2):
#     svar = metod1+metod2
#     return svar

# metod1="Ahmad"
# metod2= "Zarzar"
# print(ny_metod(metod1,metod2))



# def räkna_moms(tal1, tal2):
#     operation= tal1*tal2
#     return operation

# momsvärde= float(input('ange momms värde'))
# pristet= int (input("ange priset"))
# resultat=(räkna_moms(momsvärde,pristet))
# print(resultat)

# def ålder_gräns(ålder):
#     if ålder >= 18:
#         return True
#     return False    
    
# x= int(input("ange din ålder"))

# y = ålder_gräns(x)
# if y == True:
#     print(f"om du är{x} du är mndig")
# else:
#     print("du är ej myndig")    
            
# def längsta_ordet(ord):
#     längst= " "
#     for bokstav in ord:
#         if len(bokstav) > len(längst):
#             längst= bokstav
#     return längst
    
# min_lista =["fbvdfdffd","ffbf","svb","fvvv"]
# print(längsta_ordet(min_lista))


# def calculetr_sale(lön):
#     if lön >= 30000:
#         return(lön*0.33)
#     elif lön < 15000:
#        return (lön * 0.12)
#     elif lön < 30000:
#        return (lön * 0.28)

# din_lön= int(input("ange din lön"))
# print(calculetr_sale(din_lön))


# def till_procest(prosent_tal):
#     svar = prosent_tal * 100
#     return svar
# prosent= float(input("ange prosent ett decimaltal mellan ex )0-1) ")) 
# prosent= till_procest(prosent)
# print(f'{prosent}%')


# def hitta_bokstav(x):
#     for bokstav in x:
#         if bokstav  not in vokallista:
#             return(False)
#         else:
#             return(True)    

# x= input("ange ett ord med volkala bokstäver")
# vokallista =["a","e","i","o","U","ö","y","ä","å"]
# x= hitta_bokstav(x)
# print(x)




# def translete(text):
#     röv_text=""
#     vokallista =["a","e","i","o","U","ö","y","ä","å", " "]
#     for bokstav in text:
#         if bokstav not in vokallista:
#           röv_text += bokstav+"o"+ bokstav 
#         else:  
#             röv_text+=bokstav
#     return röv_text

# x= input("mata in sträng")
# print(translete(x))    






x=""
y = "a"
text = 'fannay'

for bokstav in text:
    if bokstav in y:
        text=text.replace(bokstav,"l")
    else:
        x+= bokstav
print(text)        


        

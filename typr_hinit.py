
# class Song:
#     def __init__ (self, rubrik:str, länngd_insekunder:int):
#         self._rubrik = rubrik
#         self._länngd_inskunnder = länngd_insekunder

#     def getlänngd_insekunder(self)-> int:
#         return self._länngd_inskunnder


#     def getrubrik(self)-> str:
#         return self._rubrik



#     def doesStartOnLetter(self, s:str) -> bool:
#         return self._rubrik.upper().startswith(s.upper())
#         # if self._title.upper().startswith(s.upper()): 
#         #     return True          
#         # return False

# class Album:
#     def __init__(self, album_rubrik:str):
#         self._album_rubrik= album_rubrik
#         self._song_list=[]

#     def getRubrik(self):
#         return self._album_rubrik

    
#     def addsong_to_album(self, song:Song):
#         return self._song_list.append(song)    

#     def total_längd_insekunder(self)->int:
#         summalängd=0
#         for sekund in self._song_list:
#             summalängd= summalängd + sekund.getlänngd_insekunder()
#             return summalängd 



# class Artist:
#     def __init__(self,namn:str):
#         self._namn=namn
#         self._artist_list= []


#     def add_album_to_artist(self,album:Album):
#        self._artist_list.append(album)
       
    
#     def get_album(self): 

#      return self._artist_list
     




# allsong= Album("My love")


# song1 = Song ("Love",123)
# allsong.addsong_to_album(song1)

# song2 = Song("Hert",34)
# allsong.addsong_to_album(song2)

# artist1= Artist("Ahmad")
# artist1.add_album_to_artist(allsong)
# for al in artist1.get_album():
#     print(al.getRubrik())





# a= song1.getlänngd_insekunder()
# b=song1.getrubrik()
# print(song1.getlänngd_insekunder())
# #### a b c e f 
# letter = "o"

# if song1.doesStartOnLetter(letter):
#     print(song1.getrubrik()) 
# print(a)
# print(b)


# print(allsong.total_längd_insekunder())




# from datetime import datetime


# class Time:
#     def __init__(self,timme:int,min:int,sec:int):
#         self._timme=""
#         self._min= ""
#         self._sec= ""

#     def settimme(self,timme:datetime):
#         self._timme = timme 

#     def gettime(self):
#         return self._timme  

#     def setmin(self,min)->int:
#         self._min = min

#     def getmin(self)->datetime:
#         return self._min

#     def setsec(self,sec):


# from datetime import datetime


# class Bil:
#     def __init__(self,namn:str,födelsedatum:datetime):
#         self._namn = namn
#         self._födelsedatum = födelsedatum
    

#     def getnamn(self)->str:
#         return self._namn

#     def räkna(self)->int:
#         nutid = datetime.now()
#         födelsedag = datetime.strptime(self._födelsedatum,"%Y-%m-%d") 
#         antaldagar = nutid - födelsedag
#         return antaldagar.days   





# bilarlista :list [Bil] = []
# svar = int(input("Antal bilar?")) 
# i = 1
# while i < svar+1:
#     bil1 = Bil(input(f"Namn på bil {i}"),input(f"Födelsedag på bil {i}"))
#     bilarlista.append(bil1)
#     i=i+1 
# total=0
# for bil in bilarlista:
#     antaldagar = bil.räkna()
#     total+= antaldagar
#     print(f'{bil.getnamn()} är {antaldagar}antal dagar gammal')
#     print(f'De är tillsammans {total} dagar gamla')   
   





    



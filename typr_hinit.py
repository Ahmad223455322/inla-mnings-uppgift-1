
class Song:
    def __init__ (self, rubrik:str, länngd_insekunder:int):
        self._rubrik = rubrik
        self._länngd_inskunnder = länngd_insekunder

    def getlänngd_insekunder(self)-> int:
        return self._länngd_inskunnder


    def getrubrik(self)-> str:
        return self._rubrik



    def doesStartOnLetter(self, s:str) -> bool:
        return self._rubrik.upper().startswith(s.upper())
        # if self._title.upper().startswith(s.upper()): 
        #     return True          
        # return False

class Album:
    def __init__(self, album_rubrik:str):
        self._album_rubrik= album_rubrik
        self._song_list=[]

    def getRubrik(self):
        return self._album_rubrik

    
    def addsong_to_album(self, song:Song):
        return self._song_list.append(song)    

    def total_längd_insekunder(self)->int:
        summalängd=0
        for sekund in self._song_list:
            summalängd= summalängd + sekund.getlänngd_insekunder()
            return summalängd 



class Artist:
    def __init__(self,namn:str):
        self._namn=namn
        self._artist_list= []


    def add_album_to_artist(self,album:Album):
       self._artist_list.append(album)
       
    
    def get_album(self): 

     return self._artist_list
     




allsong= Album("My love")


song1 = Song ("Love",123)
allsong.addsong_to_album(song1)

song2 = Song("Hert",34)
allsong.addsong_to_album(song2)

artist1= Artist("Ahmad")
artist1.add_album_to_artist(allsong)
for al in artist1.get_album():
    print(al.getRubrik())





a= song1.getlänngd_insekunder()
b=song1.getrubrik()
print(song1.getlänngd_insekunder())
#### a b c e f 
letter = "o"

if song1.doesStartOnLetter(letter):
    print(song1.getrubrik()) 
print(a)
print(b)


print(allsong.total_längd_insekunder())




# class Time:
#     def __init__(self,timme:int,min:int,sec:int):
#         self._timme=""
#         self._min= ""
#         self._sec= ""

#     def settimme(self,timme)->int:
#         self._timme = timme 

#     def gettime(self):
#         return self._timme  

#     def setmin(self,min)->int:
#         self._min = min

#     def getmin(self):
#         return self._min

#     def setsec(self,sec):






    



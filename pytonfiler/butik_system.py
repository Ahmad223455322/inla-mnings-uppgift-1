from datetime import datetime
class Produkt:
    total= []
    def __init__(self,produktId:int,produkt_antal:float):
        self._produktId = int(produktId)
        self._pris = ""
        self._pris_typ = ""
        self._produkt_namn =""
        self._antal = int(produkt_antal)
        self.set_produkt_id(produktId)
        
        
        
    def hämta_data_fil(self):
        with open("produkt2.txt","r")as fil:
            läs_fil = ""
            for x in fil:
                produkt = x.split()
                produkt_lista.append(produkt)
                läs_fil = läs_fil +x 
            return f'{läs_fil}'   
                   
    def registera(self):
        for x in produkt_lista:
            if x [0] == str(self._produktId):
                self._pris =float(x[1])
                self._pris_typ = x[2]
                self._produkt_namn = x[3]

        return (f'{self._produktId} {self._pris} {self._pris_typ} {self._produkt_namn}')
    
    def set_produkt_id(self,produkt_id):
        for x in produkt_lista:
            if produkt_id[0] not in x:
                return True
            return None 

    def rensa_total(self):
        self.total.clear()
    def getberäkna(self):
        pris =self._pris * self._antal 
        self.total.append(pris)
        return pris

    def gettotalsumma(self):
        slutsumma =0
        for x in self.total:
            slutsumma+=x
        return slutsumma    
    
    def skriv_ut_produkter(self):
        beräkningen=self.getberäkna()
        produktnamn = self.uppdatera_varan(beräkningen)
        if produktnamn != None:
            for x in kvitto_lista:
                if produktnamn[0] in x:
                    kvitto_lista.remove(x)
                    return produktnamn
        return(f'{self._produkt_namn} {self._antal} * {self._pris} = {beräkningen}')
    
    def uppdatera_varan(self,beräkningen):
        summa_av_produkter = beräkningen
        for vara in kvitto_lista:
            if self._produkt_namn in vara:
                varo_plats = kvitto_lista.index(vara)
                produkt= kvitto_lista[varo_plats]
                produkt = produkt.split()
                produkt_antal , plus_produkt_summa = int(produkt[1]), float(produkt[5])
                self._antal += produkt_antal
                summa_av_produkter += plus_produkt_summa
                till_gång_produkt = f'{self._produkt_namn} {self._antal} * {self._pris} = {summa_av_produkter}'
                return till_gång_produkt
        return None

        
    
def Kassa_meny():

    meny=["Kassa", "1.Ny kund", "0.Avsluta"]
    for alternativ in meny:
        print(alternativ)
    
    
kvitto_nummer= 0
while True:
    Kassa_meny()
    val = input("->")
    if val == "1":
        total=0
        nu_tid= datetime.now()
        tid_med_secunder= nu_tid.strftime("%Y-%m-%d-%X")
        Datuma_utan_s = nu_tid.strftime("%Y-%m-%d")
        produkt_lista =[]
        star= 50*"*"
        kvitto_lista = ["Kassa 1\n"f"Kvitto {kvitto_nummer}     {tid_med_secunder}",''] 
        a=Produkt(2,20.4) 
        a.hämta_data_fil()
        while val == "1":

            for vara in kvitto_lista:
                print(vara)
            print("Kommando:""\n""<produtId>" "  " "<antal>""\n""Pay") 
            while True:
                try:
                    kommand = input("Kommando")   
                    if  kommand.strip() == "Pay" or kommand.strip() == "pay":
                        with open(f"RECEIPT_{Datuma_utan_s}.txt","a")as fil:
                            fil.write(f'{star}\n')
                            for x in kvitto_lista:
                              fil.writelines(f'{x}\n')
                        val = "100"
                        nyproduct.rensa_total()
                        kvitto_nummer +=1
                        kvitto_lista[0]="Kassa 1\n"f"Kvitto{kvitto_nummer} "   f'{tid_med_secunder}'

                        break
                          
                    id , antal = kommand.split()
                    nyproduct=Produkt(id,antal)         
                    nyproduct.registera()
                    kvitto = nyproduct.skriv_ut_produkter()
                    kvitto_lista.insert(1,kvitto)
                    total=nyproduct.gettotalsumma()
                    kvitto_lista[-1]=f'Total: {total}'

                except:
                    print("***Produkt Id är ej tillgänglig***\n***Vill du återväna till huvudmenyn tryck på Pay***")
                      
                break     
    elif val == "0":
        break
    else: 
        print("Du har angett fel val, ange vänligen mellan (0-1) försök igen!")        
           
            
        
    
       
       

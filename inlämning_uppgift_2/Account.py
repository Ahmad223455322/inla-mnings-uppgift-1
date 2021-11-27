from enum import Enum
import unittest
class withdraw_resultat(Enum):
    ok =1
    interäker_saldo=2
    max_4000_perdag=3


class Deposit(Enum):
    ok = 1  
    max_10000_insätning_perdag= 2



class Account:
    def __init__(self,kontonummer:str):
        self._kontonummer= kontonummer
        self._saldo=0

    def Deposit(self,insätning:int):
        if insätning > 10000:
            return Deposit.max_10000_insätning_perdag
        self._saldo=self._saldo+insätning
        return Deposit.ok

    def withdraw(self,amount:int):
        if amount > 4000:
            return withdraw_resultat.max_4000_perdag
        if self._saldo<amount:
            return withdraw_resultat.interäker_saldo
        self._saldo=self._saldo -amount    
        return withdraw_resultat.ok   
    def getsaldo(self)->int:
        return self._saldo  

    def setsaldo(self,saldo):
        self.setsaldo =saldo
        return saldo
              
        
class account_tests(unittest.TestCase):
    def test_withdraw_too_mash_amount(self):
        target =Account("12345")
        belopp = target.getsaldo()
        resultat = target.withdraw(100)
        self.assertEqual(withdraw_resultat.interäker_saldo,resultat)
        self.assertEqual(belopp,target.getsaldo())

    def test_withdraw_more_than_4000(self):
        target =Account("12345")
        belopp = target.getsaldo()
        resultat = target.withdraw(4001)
        self.assertEqual(withdraw_resultat.max_4000_perdag,resultat)
        self.assertEqual(belopp,target.getsaldo())

    
    def test_insätning_more_10000_restun_fel(self):
        target =Account("12345")
        belopp = target.getsaldo()
        insätnig = target.Deposit(10001)
        self.assertEqual(Deposit.max_10000_insätning_perdag,insätnig)
        self.assertEqual(belopp,target.getsaldo())
        
    



if __name__=="__main__": 
    unittest.main()      
    
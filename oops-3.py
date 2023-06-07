class bank :
     
     def transaction(self) :
         print("total transaction value ")
    
     def account_opening(self):
        print("this will show you your account open status ")
        
     def deposite(self):
         print("this will show your deposit amount")
         
     def test(self):
         print("this is a test method from bank class")
         

class HDFC_BANK:
    def hdfc_to_icici(self):
        print("this will you all the transaction happened to icici through hdfc")
        
    def test(self):
         print("this is a test method from  hdfc bank")
         
         
class ineuron:
    def account_status_icici(self):
        print("print a account status in icici")
        
 
class icici(HDFC_BANK,bank,ineuron):
            pass
        
i=icici()
i.hdfc_to_icici()
i.transaction()
i.deposite()
i.test()
i.account_status_icici()
class bank :
     
     def transaction(self) :
         print("total transaction value ")
    
     def account_opening(self):
        print("this will show you your account open status ")
        
     def deposite(self):
         print("this will show your deposit amount")
         
         
         
class HDFC_BANK(bank):
    def hdfc_to_icici(self):
        print("this will you all the transaction happened to icici through hdfc")
        
        
class icici(HDFC_BANK):
    pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.account_opening()
         
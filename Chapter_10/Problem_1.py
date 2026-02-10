# Crete a class programmer and store some information of programmer working in the microsoft

class programmer():
    company = "Microsoft"
    
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        print("The details of the programmer who work at microsoft")

P = programmer("Ranjan","1,20,000",752054)
print(P.name,"\n",P.salary,"\n",P.pincode)
    
class ineuron:
    
    __students = "data science"
    
    def students(self):
        print("print the class of students" , ineuron.__students)
        
        
        
i = ineuron()
i.students()
i.__students() # unable to access private class
print(i._ineuron__students) #class name with (_) and variable name mentined while we extrat the data







class ineuron1:
    __students1 = "data science"
    
    
    def students2(self):
        print(ineuron1.__students1)
        
    i= ineuron1()
    i.students2()
        
        
        
list()        

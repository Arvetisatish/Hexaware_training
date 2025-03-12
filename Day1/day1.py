class car :
    def __init__(self , model , prize):
        self.model=model
        self.prize=prize
    def display(self):
        print(self.model , self.prize)
car1= car("toyoto" , 300)
car2=car("porshe" ,500)
car1.display()
car2.display()
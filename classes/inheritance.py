class person:
    def __init__(self,name, gender="female"):
        self.name=name
        self.gender= gender
    
    def show(self):    #self batata hai k wo show person class ko belong krta hai 
        print("My Details")
        print(f'Name : {self.name}')
        print(f'Gender : {self.gender}')

class student(person):
    def __init__(self, name, gender, klass,college,stream):
        super().__init__(name, gender)
        self.klass = klass
        self.college= college
        self.stream = stream
        
    def show_more(self):
        print("More Details")
        print(f'College:{self.college}')
        print(f'Class : {self.klass}')
        print(f'Stream : {self.stream}')
        
class Coder(student):
    def __init__(self, name, gender, klass, college, stream,prog_langs=[]):
        super().__init__(name, gender, klass, college, stream)
        self.prglangs= prog_langs
            
    def coding_experience(self):
        if len(self.prglangs) ==0:
            print(f'I,{self.name} dont know any programming language')
        else:
            print(f'I,{self.name} know the following programming languages')
            for lang in self.prglangs:
                print(f"=> {lang}")
            print('----' * 10)
        
    def add_language(self, lang):
        self.prglangs.append(lang)
        
        
        
if __name__=="__main__":
    
    p=person("John Cena",gender="male")
    p.show()
    
    std1= student('Ankit','male','Python class','Digipodium','Data science')
    std1.show()
    std1.show_more()    
        
    coder=Coder('Vijay','male','9Th','Colvin Taluqdar','PCM')
    coder.show()
    coder.show_more()
    coder.coding_experience()
    print("Ek Saal Baad")
    coder.add_language('Pyhton')
    coder.add_language('HTMl')
    coder.add_language('CSS')
    coder.coding_experience()
        
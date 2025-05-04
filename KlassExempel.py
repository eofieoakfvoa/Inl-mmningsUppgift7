class Person:
    def __init__(self, name : str, age : float, gender : int):
        self.Name = name
        self.Age = age
        self.Gender = gender
    def GetInformation(self):
        return (self.Name, self.Age, self.Gender)
    def IsOfAge(self):
        if self.Age >= 18: 
            return True
        return False

#test
egkjimsavd = Person("egkjimsavd", 132.5, "man")
print(egkjimsavd.GetInformation())
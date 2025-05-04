class Person:
    def __init__(self, name : str, age : float, gender : str):
        self.Name = name
        self.Age = age
        self.Gender = gender #skulle också gå att ha någon enum liknade så man slipper synonymer, t.ex dam och kvinna
    def GetInformation(self):
        return (self.Name, self.Age, self.Gender)
    def IsOfAge(self):
        return True if self.Age >= 18 else False #ternary operator, skulle nog också vara bra att ha en variabel som konstant är värdet på myndig, så man kan ändra lätt, och lite bättre readability

#test
egkjimsavd = Person("egkjimsavd", 132.5, "man")
egkjimsavdson = Person("egkjimsavdson", 2, "man")
print(egkjimsavd.GetInformation(), " är mynding? :", egkjimsavd.IsOfAge()) #('egkjimsavd', 132.5, 'man')  är mynding? : True
print(egkjimsavdson.GetInformation(), " är mynding? :", egkjimsavdson.IsOfAge()) #('egkjimsavdson', 2, 'man')  är mynding? : False

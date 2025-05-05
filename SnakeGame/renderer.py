import pygame

#hade hällre haft att renderID var inom renderer klassen eftersom inget ska kunna ändra på renderID förutom renderer
#finns inget sätt att ändra vilken layer på skärmen saken är på just nu, förutom att göra ordern på när man sätter in i rätt ordning
#där renderer ritar först det med renderID 1 sen 2, som gör så att det med 1 kommer se ut som att det är under et med 2.
#sen I draw metoden så hade det varit bättre ifall saker åtminstånde hade sin egna .draw metod i sin klass eller något, istället för att det måste vara draw.rect()

class Renderer():
    Display = None
    RenderDictionary = {}
    
    def __init__(self, display):
        self.Display = display

    def Add(self, Object):
        firstEmpty = self.FindFirstEmpty()
        self.RenderDictionary[firstEmpty] = Object
        Object.renderID = firstEmpty
    #del eftersom det var det som kom upp när jag googlade hur man tog bort en key från en dictionary eftersom jag vet inte ifall att sätta som "None" också fungerar eller att det skapar problem 
    #iallafall så är det ändå bra att helt tabort det från memory, eftersom det inte behövs längre     
    def Remove(self,Object):
        del self.RenderDictionary[Object.renderID] 

    #ett lätt sätt att göra detta lite bättre är att ha kanske 3 listor som fungerar som layers, där den ritar från först 1 sen 2 sen 3, dock så är det i det fallet bara bättre
    #ett bättre system för depth istället
    def Draw(self):
        for i in self.RenderDictionary:
            Entity = self.RenderDictionary[i]
            rectangleValue = [Entity.Position.x, Entity.Position.y, Entity.Size.x, Entity.Size.y]
            pygame.draw.rect(self.Display, Entity.Color, rectangleValue)

    def FindFirstEmpty(self):
        i = 0
        while self.RenderDictionary.get(i) is not None: #get eftersom hade den inte existerat är jag relativt säker på att det bara skulle krasha.
            i += 1
        return i
    
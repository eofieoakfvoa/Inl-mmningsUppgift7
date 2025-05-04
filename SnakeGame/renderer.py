import pygame
class Renderer():
    Display = None
    RenderDictionary = {}
    
    def __init__(self, display):
        self.Display = display

    def Add(self, Item):
        firstEmpty = self.FindFirstEmpty()
        self.RenderDictionary[firstEmpty] = Item
        Item.renderID = firstEmpty
    def FindFirstEmpty(self):
        i = 0
        while self.RenderDictionary.get(i) is not None:
            i += 1
        return i
    def Remove(self,renderID):
        del self.RenderDictionary[renderID]
    def Draw(self):
        for i in self.RenderDictionary:
            Entity = self.RenderDictionary[i]
            rectangleValue = [Entity.Position.x, Entity.Position.y, Entity.Size.x, Entity.Size.y]
            pygame.draw.rect(self.Display, Entity.Color, rectangleValue)
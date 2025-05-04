import pygame
class Renderer(self):
    Display = None
    def __init__(self, display):
        self.Display = display
    RenderDictionary = {}
    def Add(self, Item):
        firstEmpty = self.FindFirstEmpty()
        self.RenderDictionary[firstEmpty] = Item
        return firstEmpty
    def FindFirstEmpty(self):
        i = 0
        while not self.RenderDictionary[i] == None:
            i = i + 1
        return i
    def Draw(self):
        for i in self.RenderDictionary:
            Entity = self.RenderDictionary[i]
            rectangleValue = [Entity.Position.x, Entity.Position.y, Entity.Size.x, Entity.Size.y]
            pygame.draw.rect(self.Display, Entity.Color, )
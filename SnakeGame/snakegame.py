from player import *
from game import * 
class snakegame():
    def __init__(self):
         self.GameLoop()
    gameSystem = GameSystem()
    Player = Player()
    Player.SetSize(5, 5)
    Player.SetColor(gameSystem.Color.Red.value)
    PlayerID = gameSystem.AddObjectToRenderer(Player)

    def GameLoop(self):
        while self.gameSystem.IsRunning():
            self.EventHandler()
            self.gameSystem.Renderer.Draw()
            pygame.display.update()            
        pygame.quit()
        quit()

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.gameSystem.StopRunning()
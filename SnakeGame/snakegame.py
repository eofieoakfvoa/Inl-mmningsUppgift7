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
            print(self.Player.Direction)
            pygame.display.update()

            self.gameSystem.WaitForTick()            
        pygame.quit()
        quit()

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.gameSystem.StopRunning()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.Player.ChangeDirection(self.Player.DirectionList.Left)
                elif event.key == pygame.K_RIGHT:
                    self.Player.ChangeDirection(self.Player.DirectionList.Right)
                elif event.key == pygame.K_UP:
                    self.Player.ChangeDirection(self.Player.DirectionList.Up)
                elif event.key == pygame.K_DOWN:
                    self.Player.ChangeDirection(self.Player.DirectionList.Down)
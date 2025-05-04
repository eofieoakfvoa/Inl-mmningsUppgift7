from player import *
from game import * 
class snakegame():
    def __init__(self):
         self.GameLoop()
    gameSystem = GameSystem()
    Player = Player()
    Player.SetSize(15, 15)
    Player.SetColor(gameSystem.Color.Red.value)
    PlayerID = gameSystem.AddObjectToRenderer(Player)

    def GameLoop(self):
        while self.gameSystem.IsRunning():
            self.EventHandler()
            self.GameLogic()
            print(self.Player.Position)
            self.gameSystem.GameDisplay.fill(self.gameSystem.Color.White.value)
            self.gameSystem.Renderer.Draw()
            self.gameSystem.Update()            

        pygame.quit()
        quit()
    def GameLogic(self):
        self.Player.MovePlayer()
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
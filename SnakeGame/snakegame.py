from player import *
from game import * 
import random
class snakegame():
    def __init__(self):
         self.GameLoop()
    gameSystem = GameSystem()
    foodExists = False
    Player = Player(15,15, gameSystem.Color.Red, 10)
    Player.SetPosition(gameSystem.Resolution.x / 2, gameSystem.Resolution.y / 2)
    gameSystem.AddObjectToRenderer(Player)
    Food = None
    def GameLoop(self):
        while self.gameSystem.IsRunning():
            self.EventHandler()
            self.GameLogic()
            self.gameSystem.GameDisplay.fill(self.gameSystem.Color.White.value)
            self.gameSystem.Renderer.Draw()
            self.gameSystem.Update()            

        pygame.quit()
        quit()

    def GameLogic(self):
        if self.foodExists == False:
            self.AddFood()
        self.Player.MovePlayer()
        if self.Player.Position.x >= GameSystem.Resolution.x or self.Player.Position.x < 0 or self.Player.Position.y >= GameSystem.Resolution.y or self.Player.Position.y < 0:
            self.gameSystem.StopRunning()
        if self.Food.Position.x == self.Player.Position.x and self.Food.Position.y == self.Player.Position.y:
            print("WAAAAAAAAAAAH")
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

    def AddFood(self):
        NewFood = Food(15,15, GameSystem.Color.Black)
        foodX = round(random.randrange(0, int(GameSystem.Resolution.x) - 15) / 10.0) * 10.0
        foodY = round(random.randrange(0, int(GameSystem.Resolution.y) - 15) / 10.0) * 10.0
        NewFood.SetPosition(foodX, foodY)
        self.gameSystem.AddObjectToRenderer(NewFood)
        self.Food = NewFood
        self.foodExists = True
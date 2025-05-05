from player import *
from game import * 
import random
class snakegame():
    def __init__(self):
         self.GameLoop() 
    gameSystem = GameSystem(15, 400, 300, "Snake Game") #maxfps, screenwidth, screenheight, title

    Player = Player(15,15, Color.Red, 10)
    Player.SetPosition(gameSystem.Resolution.x / 2, gameSystem.Resolution.y / 2) #borde nog ha så att detta är i __init__ med kanske default values som är 0,0

    gameSystem.AddObjectToRenderer(Player) #lägger till att spelaren ska ritnas
    foodExists = False
    Food = None
    latestUpdatedBodyPartCount = 1 # bodypartcount dictionary räknar in huvudet som är på nummer 1
    Score = 0
    Scene = 1 # 1 = game 2 = meny

    def GameLoop(self):
        while self.gameSystem.IsRunning():
            self.EventHandler() #skulle vara bättre ifall det typ var scenes som var klasser, som som har typ overrite EventHandler GameLogic och Draw metod
            self.GameLogic()
            self.GameDraw()
            self.gameSystem.Update()            
        pygame.quit()
        quit()

    def GameLogic(self):
        if self.foodExists == False:
            self.AddFood()
        self.Player.MovePlayer()
        self.UpdatePlayerBodyPartCount()
        
        if self.Player.Position.x >= self.gameSystem.Resolution.x or self.Player.Position.x < 0 or self.Player.Position.y >= self.gameSystem.Resolution.y or self.Player.Position.y < 0:
            self.Scene = 2
    
        if self.Food.Position.x == self.Player.Position.x and self.Food.Position.y == self.Player.Position.y:
            self.Player.AddBodyPart()
            self.RemoveFood()
            self.Score = self.Score + 1
            self.AddFood()
    
        #kollar igenom alla delar ifall de har samma position som huvudet (player)
        for Key in list(self.Player.BodyDictionary.values())[:-1]:
            if Key == self.Player: continue #ifall keyn är huvudet kommer den ha samma position som den själv, därför skippar man bara den
            if Key.Position == self.Player.Position:
                self.Scene = 2

    def GameDraw(self):
        self.gameSystem.ClearScreen()   
        if self.Scene == 1:
            self.DisplayScore()
            self.gameSystem.Renderer.Draw()
        if self.Scene == 2:
            self.gameSystem.DisplayText("Klicka C för att spela igen")

    def DisplayScore(self):
        self.gameSystem.DisplayText(f"du har {self.Score} poäng", 100, 200, Color.Black)

    #kollar ifall en ny del har lags till i BodyPartCount, där en jämför antalet med den senaste den kollat, dock tror jag ett problem kan skapas ifall pånågot sätts 
    #2 styckna body.partcount samtidigt eftersom den kollar inte skillnaden den antar bara att det är +1, fast detta borde inte vara ett problem
    def UpdatePlayerBodyPartCount(self):
        if self.latestUpdatedBodyPartCount != self.Player.BodyPartCount: 
            self.gameSystem.AddObjectToRenderer(self.Player.BodyDictionary[self.Player.BodyPartCount])
            self.latestUpdatedBodyPartCount = self.Player.BodyPartCount 

    def EventHandler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.gameSystem.StopRunning()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.Player.ChangeDirection(DirectionList.Left)
                elif event.key == pygame.K_RIGHT:
                    self.Player.ChangeDirection(DirectionList.Right)
                elif event.key == pygame.K_UP:
                    self.Player.ChangeDirection(DirectionList.Up)
                elif event.key == pygame.K_DOWN:
                    self.Player.ChangeDirection(DirectionList.Down)

    def AddFood(self):
        NewFood = Food(15,15, Color.Black)
        foodX = round(random.randrange(0, int(self.gameSystem.Resolution.x) - 15) / 10.0) * 10.0
        foodY = round(random.randrange(0, int(self.gameSystem.Resolution.y) - 15) / 10.0) * 10.0
        NewFood.SetPosition(foodX, foodY)
        self.gameSystem.AddObjectToRenderer(NewFood)
        self.Food = NewFood
        self.foodExists = True

    def RemoveFood(self):
        self.gameSystem.RemoveObjectFromRenderer(self.Food)
        self.Food = None
    
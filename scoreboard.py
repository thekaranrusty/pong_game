from turtle import Turtle
FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.score_p1 = 0
         self.score_p2 = 0
         self.color("white")
         self.penup()
         self.goto(0, 240)
         self.write(f"{self.score_p1}         {self.score_p2}",
                    move=False, align="center", font=FONT)
         self.hideturtle()


     def score_refresh_p1(self):
         self.score_p1 += 1
         self.clear()
         self.write(f"{self.score_p1}         {self.score_p2}",
                    move=False, align="center", font=FONT)


     def score_refresh_p2(self):
         self.score_p2 += 1
         self.clear()
         self.write(f"{self.score_p1}         {self.score_p2}",
                    move=False, align="center", font=FONT)

     def game_over(self,player):
         self.goto(0, 0)
         self.write(f"Game Over, {player} Won", move=False, align="center",
                    font=("Courier", 14, "normal"))
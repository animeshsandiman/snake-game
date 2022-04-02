from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            h_score = file.read()
            self.high_score = int(h_score)

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()



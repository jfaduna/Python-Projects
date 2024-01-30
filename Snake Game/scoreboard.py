from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def get_high_score(self):
        high_score = 0
        with open("./Snake Game/data.txt") as data:
            high_score = int(data.read())
        return high_score

    def set_high_score(self):
        with open("./Snake Game/data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

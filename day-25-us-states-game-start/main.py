import turtle as t
import pandas as pd
screen = t.Screen()
screen.title("U.S. States Game")
image = "D:/python/learningbasicpy/day-25-us-states-game-start/blank_states_img.gif"
data = "D:/python/learningbasicpy/day-25-us-states-game-start/50_states.csv"
screen.addshape(image)

class textstate(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
    
    def guessed(self, x, y, state_name):
        
        self.goto(x,y)
        self.write(state_name,False,align="center", font=('Calibri', 18, 'normal'))

state = textstate()
   
score = 0
df = pd.read_csv(data)
guessed_list = []
not_guessed = []
t.shape(image)

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name")
    if answer_state is None:
        print("Game Cancelled")
        break
    
    for i in  df.state :
        if i.lower() == answer_state and i not in guessed_list:
            print(i)
            state_coor = df[df.state == i]
            x_cor = int(state_coor.x.item())
            y_cor = int(state_coor.y.item())
            state.guessed(x_cor,y_cor,i)
            guessed_list.append(i)
            score += 1
            break
    else:
        print("did not guess")

    if len(guessed_list) == 50:
        print("You guessed all of them CONGRATS!")
        is_game_on = False

for row in df.state:
    if row not in guessed_list:
        not_guessed.append(row)

export_data = pd.DataFrame(not_guessed)
export_data.to_csv("D:/python/learningbasicpy/day-25-us-states-game-start/notguessed.csv")

print(f"Guessed: {len(guessed_list)}")
print(f"Not Guessed: {len(not_guessed)}")
print("Exited the game")

t.mainloop()

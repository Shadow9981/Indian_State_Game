import turtle
import pandas

screen = turtle.Screen()
screen.title("State Game")
screen.bgcolor("black")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("29_states.csv")
all_states = data.state.tolist()
guessed_states = []
remaining_states = []

game_running = True

while game_running:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/28 States Guessed",
                                   prompt="What's another state name?").title()

    if answer_text == "Exit":
        for states in all_states:
            if states not in guessed_states:
                remaining_states.append(states)
        df = pandas.DataFrame(remaining_states)
        df.to_csv("remaining_states")
        break

    if answer_text in all_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.color("white")
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(arg=answer_text, font=('Arial', 10, 'bold'))

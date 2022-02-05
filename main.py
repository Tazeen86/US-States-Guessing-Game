import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")
image="blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states = []

while len(guessed_states) <= 50:
    answer_state= screen.textinput(f"{len(guessed_states)}/50 Guessed Correctly","Which state you want to add?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states=[state for state in all_states if( state not in guessed_states)]

        df=pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        row = data[data.state == answer_state]
        print(row.x,row.y)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(row.x),int(row.y))
        text.pendown()
        text.write(row.state.item())


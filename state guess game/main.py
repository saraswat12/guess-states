import turtle
from PIL import Image # an external image processing library
import pandas as pd

screen = turtle.Screen()
screen.title("INDIA States game")
#screen.screensize(1148, 1080)
image = r"D:\python_new projects\state guess game\map.gif"


resized_image_path = "resized_map.gif"
original_image = Image.open(image)
resized_image = original_image.resize((750, 650))
resized_image.save(resized_image_path)




screen.addshape(resized_image_path)
turtle.shape(resized_image_path)

data = pd.read_csv("states.csv")

all_states = data.States.to_list()



guess_states = []

while len(guess_states) < 30:
    answer = screen.textinput(title=f"{len(guess_states)}/30 States Guessed", prompt = "What's another state's name?").title()

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        #print(missing_states)
        break
    if answer in all_states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.States == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)   #state_data.States.item() instead of answer












#turtle.shapesize(stretch_wid=1, stretch_len=1)

#screen.exitonclick()
"""


#------  You get the coordinates of each states by clicking over them-------

def get_mouse_click_over(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_over)
turtle.mainloop()
"""
"""
def convert_coordinates(latitude, longitude, image_width, image_height):
    # Define the bounding box of your map (replace with actual values)
    min_latitude, max_latitude = 8.900372741, 34.29995933
    min_longitude, max_longitude = 72.63686717, 94.46665849

    # Calculate the normalized coordinates
    normalized_x = (longitude - min_longitude) / (max_longitude - min_longitude)
    normalized_y = (latitude - min_latitude) / (max_latitude - min_latitude)

    # Map the normalized coordinates to the screen coordinates
    screen_x = normalized_x * image_width
    screen_y = normalized_y * image_height

    return screen_x, screen_y    #lati -- x

"""



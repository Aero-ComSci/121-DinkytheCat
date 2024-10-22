# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand
spot_color = "pink"
#-----game configuration----
t.Turtle()

t.shape("classic")
t.shapesize(10)
t.fillcolor(spot_color)
    
#-----initialize turtle-----

def change_position():
    newx=(rand.randit(1,1000))
    newy=(rand.randit(1,1000))
    t.goto(newx,newy)
#-----game functions--------
def spot_clicked(x, y):
    print("Spot was clicked!")
    change_position
t.onclick(spot_clicked)

#-----events----------------
t.done()

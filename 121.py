
#-----import statements-----
import turtle as t
import random as rand

score = 0
spot_color = "pink"
font_setup=("Arial", 20, "normal")
timer = 30
counter_interval = 1000   
timer_up = False

#-----game configuration----

dot = t.Turtle()
dot.speed(0)
dot.shape("circle")
dot.shapesize(5)
dot.fillcolor(spot_color)

score_writer = t.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()  
score_writer.goto(0, 230)  
score_writer.write(score, font=font_setup)

counter =  t.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-45, 290)
counter.write(timer, font=font_setup)

#-----game functions--------



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    dot.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def count():
    global score 
    score += 1
    score_writer.clear() 
    score_writer.write(f"Score: {score}", align="center" ,font=font_setup)  

def change_position():
    newx = rand.randint(-200, 300) 
    newy = rand.randint(-200, 300)

    dot.penup() 
    dot.goto(newx, newy)

def spot_clicked(x, y):
    shapelist=["red","blue","green","purple","pink","yellow"]
    t.dot(rand.choice(shapelist))
    count()  
    change_position()  

dot.onclick(spot_clicked)
change_position()

#-----events----------------
wn = t.Screen()
wn.ontimer(countdown, counter_interval) 
t.done()

# Import turtle graphics library
import turtle
import random
#I can edit this
# set the players lives to 3
lives = 3
score = 0

# Set up player controls
def move_left():
    player.setx(player.xcor() - 10)
def move_right():
    player.setx(player.xcor() + 10)
def quit_game():
    screen.bye()
    
# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Asteroids")

# Set up lives counter
lives_writer = turtle.Turtle()
lives_writer.color("white")
lives_writer.penup()
lives_writer.goto(-380, 260)
lives_writer.write("Lives: {}".format(lives), align="left", font=("Courier", 18, "normal"))

# Set up score counter
score_writer = turtle.Turtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(380, 260)
score_writer.write("Score: {}".format(score), align="right", font=("Courier", 18, "normal"))

# set up game over text
game_over_writer = turtle.Turtle()
game_over_writer.hideturtle()
game_over_writer.penup()
game_over_writer.goto(0, 0)
game_over_writer.color("red")
game_over_writer.write("", align="center", font=("Courier", 24, "normal"))

# Set up player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)

#set up asetroids
asteroids = []
for i in range(20):
    asteroid = turtle.Turtle()
    asteroid.color("grey")
    asteroid.shape("circle")
    asteroid.penup()
    asteroid.speed(10)
    asteroid.goto(random.randint(-350, 350), random.randint(300, 600))
    asteroid.setheading(270)
    asteroids.append(asteroid)
    
# move projectile
projectiles = []
def fire_projectile():
    global lives
    global score
    
    # Set projectile turtle
    projectile = turtle.Turtle()
    projectile.speed(0)
    projectile.shape("square")
    projectile.color("blue")
    projectile.penup()
    projectile.setheading(90)
    projectile.shapesize(0.5, 0.5)
    projectile.goto(player.position())

    # add the projectile to the list of active projectiles
    projectiles.append(projectile)
    
    # Move projectile
    while projectile.ycor() < 300:
        projectile.forward(10)
        
        # check for collisions between the projectile and all the asteroids
        for asteroid in asteroids:
            if projectile.distance(asteroid) < 20:
                print("Collision!")
                # remove the projectile from the list of active projectiles
                if projectile in projectiles:
                    projectiles.remove(projectile)
                    projectile.hideturtle()
                # remove the asteroid from the screen
                if asteroid in asteroids:
                    asteroids.remove(asteroid)
                    asteroid.hideturtle()
                    # increment the score
                    score += 100
                    score_writer.clear()
                    score_writer.write("Score: {}".format(score), align="right", font=("Courier", 18, "normal"))
                break
        else:
            # if no collision occurred, check if the projectile is out of bounds
            if (projectile.ycor() > 300):
                if projectile in projectiles:
                    projectiles.remove(projectile)
                    projectile.hideturtle()
                    
    # if projectile reaches top of the screen, remove it from the list of active projectiles
    if projectile in projectiles:
        projectiles.remove(projectile)
        projectile.hideturtle()

# Define function to reset the game
def restart_game1():
    global lives
    global score
    global asteroids
    global asteroid
    game_over_writer.clear()
    game_over_writer.hideturtle()
    lives = 3
    score = 0
    lives_writer.clear()
    lives_writer.write("Lives: {}".format(lives), align="left", font=("Courier", 18, "normal"))
    score_writer.clear()
    score_writer.write("Score: {}".format(score), align="right", font=("Courier", 18, "normal"))
    player.color("white")
    player.goto(0, -250)
    player.showturtle()
    for asteroid in asteroids:
        asteroid.hideturtle()
    asteroids.clear()
    projectiles.clear()
    for i in range(20):
        asteroid = turtle.Turtle()
        asteroid.color("grey")
        asteroid.shape("circle")
        asteroid.penup()
        asteroid.speed(10)
        asteroid.goto(random.randint(-350, 350), random.randint(300, 600))
        asteroid.setheading(270)
        asteroids.append(asteroid)
    run_game()
def restart_game2():
    global lives
    global score
    global asteroids
    global asteroid
    game_over_writer.clear()
    game_over_writer.hideturtle()
    player.color("white")
    player.goto(0, -250)
    player.showturtle()
    for asteroid in asteroids:
        asteroid.hideturtle()
    asteroids.clear()
    projectiles.clear()
    for i in range(20):
        asteroid = turtle.Turtle()
        asteroid.color("grey")
        asteroid.shape("circle")
        asteroid.penup()
        asteroid.speed(10)
        asteroid.goto(random.randint(-350, 350), random.randint(300, 600))
        asteroid.setheading(270)
        asteroids.append(asteroid)
    run_game()
def game_over():
    player.color("red")
    player.hideturtle()
    game_over_writer.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
    game_over_writer.goto(0, -50)
    game_over_writer.write("Press 'r' to reset game or 'q' to quit", align="center", font=("Courier", 24, "normal"))

    screen.onkey(restart_game1, "r")

    screen.listen()
    screen.mainloop()
    
def run_game():
    global lives
    global score
    global asteroids
    global asteroid
    # Main game loop
    while True:
        # Move asteroids
        for asteroid in asteroids:
            asteroid.forward(4)
            # Check if an asteroid reached the bottom of the screen
            if asteroid.ycor() < -250:
                lives -= 1
                lives_writer.clear()
                lives_writer.write("Lives: {}".format(lives), align="left", font=("Courier", 18, "normal"))
                asteroid.hideturtle()
                asteroids.remove(asteroid)
                if lives == 0:
                    game_over()
        if len(asteroids) == 0:
            restart_game2()
        
        # Update screen
        screen.update()
        
#set up key bindings
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_projectile, "space")
screen.onkeypress(quit_game, "q")
screen.listen()
run_game()


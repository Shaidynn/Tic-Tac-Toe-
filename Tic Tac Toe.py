import turtle

# Initialize turtle
t = turtle.Pen()
t.speed(300)
t.penup()
t.goto(-150, -150)
t.pendown()

# Create canvas
canvas = turtle.Screen()
canvas.setup(800, 400)
canvas.title("Tic Tac Toe")

# Define a function to draw a square
def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)

# Define a function to draw the grid
def draw_grid():
    for i in range(3):
        draw_square()
        t.forward(100)

# Draw the grid
draw_grid()
t.penup()
t.goto(-150, -50)
t.pendown()
draw_grid()
t.penup()
t.goto(-150, 50)
t.pendown()
draw_grid()
t.hideturtle()

# Function to place Xs and Os on the grid
def place_x_and_o(choice, symbol):
    t.penup()
    grid_positions = {1: (-100, 100), 2: (0, 100), 3: (100, 100),
                      4: (-100, 0), 5: (0, 0), 6: (100, 0),
                      7: (-100, -100), 8: (0, -100), 9: (100, -100)}
    if choice in grid_positions:
        t.goto(grid_positions[choice])
        t.pendown()
        t.write(symbol, font=("Arial", 30, "bold"))

# List of available grid choices
grid_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Main game loop
while grid_choices:
    x = canvas.numinput("Player 1, choose a grid.", " ", 9, 1)
    while x not in grid_choices:
        x = canvas.numinput("Player 1, choose again.", " ", 9, 1)
    grid_choices.remove(x)
    place_x_and_o(x, "X")

    y = canvas.numinput("\nPlayer 2, choose a square.", " ", 9, 1)
    while y not in grid_choices:
        y = canvas.numinput("\nPlayer 2, choose a square.", " ", 9, 1)
    grid_choices.remove(y)
    place_x_and_o(y, "O")

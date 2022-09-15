from turtle import Screen
import time  # Time module to use time functions
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn turtle animation on/off

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# --- Code in this section listen to keypress and call methods based on the key binding.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# ---

game_is_on = True
while game_is_on:
    """Update screen only after following loop completes a cycle,
    so snake moves smoothly with all three boxes"""
    screen.update()
    time.sleep(0.1)  # Reduce the time of loop by tenth of a second.
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.snake[1:]:  # We used python slicing of list/tuple here
        """above line of code iterates through the list of objects,
        skipping the very first one, which is; '0' and loops through
        until the list is over"""
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

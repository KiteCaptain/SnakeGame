# from turtle import *
from random import randrange
# from freegames import square,vector
import pygame
from pygame.locals import *
import time
#
# food = vector(0,0)
# snake = [vector(10,0)]
# aim = vector(0,-10)
#
# def change(x,y):
#     aim.x = x
#     aim.y = y
#
# def inside(head):
#     return -200 < head.x < 190 and -200 < head.y < 190
#
# def move():
#     head = snake[-1].copy()
#     head.move(aim)
#
#
#     if not inside(head) or head in snake:
#         square(head.x, head.y, 9, 'red')
#         update()
#         return
#     snake.append(head)
#
#
#     if head == food:
#         print("snake ", len(snake))
#         food.x = randrange(-15,15)*10
#         food.y = randrange(-15,15)*10
#
#     else:
#         snake.pop(0)
#
#     clear()
#
#     for body in snake:
#         square(body.x, body.y, 9, "green")
#
#     square(food.x, food.y, 9, "red")
#     update()
#     ontimer((move, 100))
#
#     hideturtle()
#     tracer(False)
#     listen()
#     onkey(lambda:change(10,0),"Right")
#     onkey(lambda:change(-10,0),"left")
#     onkey(lambda:change(0,10),"Up")
#     onkey(lambda:change(0,-10),"Down")
#
#     move()
#     done()

# def draw_block():
#     block_x = 100
#     block_y = 100
#     pygame.draw.rect(surface, color, pygame.Rect(block_x, block_y,100,100))
#     pygame.display.flip()
class Snake:
    def __init__(self):
        # self.parent_screen = parent_screen
        self.x = 100
        self.y = 100
        self.block = pygame.Rect(100, 100, 20, 20)
        self.direction = 100

    def draw(self):
        color = (255, 0, 0)
        surface_size = (500, 500)

        self.surface = pygame.display.set_mode(surface_size)
        self.surface.fill(pygame.Color(0, 200, 0))
        pygame.draw.rect(self.surface, color, self.block)
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.x += 10
        self.draw()

    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        self.draw()


class Game:

    def __init__(self):
        pygame.init()
        surface_size = (500, 500)
        self.surface = pygame.display.set_mode(surface_size)
        self.surface.fill(pygame.Color(0, 200, 0))
        self.snake = Snake()
        self.snake.draw()

    def run(self):
        # moving_by_mouse = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
                # if event.type == QUIT:
                #     running = False
                # # moving with a mouse
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if self.snake.collidepoint(event.pos):
                #         moving_by_mouse = True
                # if event.type == pygame.MOUSEBUTTONUP:
                #     moving_by_mouse = False
                # if event.type == pygame.MOUSEMOTION and moving_by_mouse:
                #     self.snake.move_ip(event.rel)
            # self.snake.walk()
            # time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()





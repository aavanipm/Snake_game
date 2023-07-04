import time
import pygame
import random


class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + ":" + str(self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Snake:
    head = Position(0, 4)
    fruit = Position(2, 6)
    length = 3
    size = 15
    move = "right"
    history = []
    is_alive = 0
    first_fruit = 5
    score = 0

    def printing(self, display_text, point, font_size, sleep_time):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(display_text, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (point, point)
        face.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(sleep_time)

    def eat(self):
        if self.first_fruit == 5:
            pygame.draw.circle(face, (255, 255, 255), [self.fruit.x * self.size + self.size // 2, self.fruit.y * self.size + self.size // 2], self.size // 2, 0)
            self.first_fruit = 0
        elif self.fruit == self.head:
            self.random_fruit()
            pygame.draw.circle(face, (255, 255, 255), [self.fruit.x * self.size + self.size // 2, self.fruit.y * self.size + self.size // 2], self.size // 2, 0)
            self.length = self.length + 1
            self.score = self.score + 1
        pygame.draw.rect(face, (0, 0, 0), (5, 7, self.size, self.size))
        self.printing(str(self.score), 15, 15, 1)

    def random_fruit(self):
        self.fruit.x = random.randrange(screen_size)
        self.fruit.y = random.randrange(screen_size)
        for i in range(len(self.history)):
            if self.fruit.x == self.history[i].x and self.fruit.y == self.history[i].y:
                self.random_fruit()

    def draw(self):
        pygame.draw.rect(face, (0, 255, 0), (self.head.x * self.size, self.head.y * self.size, self.size, self.size))
        self.history.append(Position(self.head.x, self.head.y))
        # print(self.history)
        pygame.display.update()

    def hitted(self):
        for i in range(len(self.history)):
            if self.head.x == self.history[i].x and self.head.y == self.history[i].y:
                self.printing("Failed", screen_size * self.size // 2, 30, 2000)
                self.is_alive = 1

    def next(self):
        self.erase()
        if self.move == "right":
            self.head.x = self.head.x + 1
            if self.head.x == screen_size:
                self.head.x = 0
        elif self.move == "down":
            self.head.y = self.head.y + 1
            if self.head.y == screen_size:
                self.head.y = 0
        elif self.move == "left":
            self.head.x = self.head.x - 1
            if self.head.x == -1:
                self.head.x = screen_size - 1
        elif self.move == "up":
            self.head.y = self.head.y - 1
            if self.head.y == -1:
                self.head.y = screen_size - 1
        self.hitted()
        self.draw()

    def erase(self):
        if len(self.history) == 2 * self.length:
            first = self.history.pop(0)
            pygame.draw.rect(face, (0, 0, 0), (first.x * self.size, first.y * self.size, self.size, self.size))


pygame.init()
screen_size = 40
snake_object = Snake()
face = pygame.display.set_mode((screen_size * snake_object.size, screen_size * snake_object.size))

while snake_object.is_alive == 0:

    pygame.time.wait(150)
    snake_object.eat()
    snake_object.next()
    if snake_object.score == 50:
        snake_object.printing("You Win", screen_size * snake_object.size // 2, 30, 2000)
        snake_object.is_alive = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            snake_object.move = "down"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            snake_object.move = "up"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            snake_object.move = "right"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            snake_object.move = "left"

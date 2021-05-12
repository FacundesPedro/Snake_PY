import pygame,sys
import random

#Variables
red = (255,0,0)
blue = (50,100,213)
orange = (205,102,0)
size = (600,600)

xi = 200
yi = 200
dx = 0
dy = 0
x_food = 140
y_food = 460

position_list = [[xi,yi]]

snake = {
    "width":20,
    "height":20,
}

display = pygame.display.set_mode(size)
pygame.display.set_caption('Jogo da Cobrinha')
display.fill(blue)

clock = pygame.time.Clock()

#Functions
def draw_snake(snake_list):
    display.fill(blue)
    for position in snake_list:
        pygame.draw.rect(display,orange,[position[0],position[1],snake['height'],snake['width']])

def move_snake(snake_list,dx,dy):
  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = snake['height']
                dy = 0
            elif event.key == pygame.K_LEFT:
                dx = -snake['height']
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -snake['height']
            elif event.key == pygame.K_DOWN:
                dx = 0                
                dy = snake['height']        
        if event.type == pygame.QUIT: sys.exit()
    

    xf = snake_list[-1][0] + dx
    yf = snake_list[-1][1] + dy

    snake_list.append([xf,yf])
    del snake_list[0]

    return dx,dy

def selectFoodPosition():
    x_food = round(random.randrange(0,600 - snake['height']) /20) * 20
    y_food = round(random.randrange(0,600 - snake['height']) /20) * 20
    return x_food,y_food

def isEated(dx,dy,snake_list,x_food,y_food):
    head = snake_list[-1]

    xf = head[0] + dx
    yf = head[1] + dy
 
    if head[0] == x_food and head[1] == y_food:
        snake_list.append([xf,yf])
        x_food,y_food = selectFoodPosition() 
        
    return x_food,y_food,snake_list

def draw_food(x_food,y_food):
    pygame.draw.rect(display,red,[x_food,y_food,snake['height'],snake['height']])

def exist(snake_list):
    head = snake_list[-1]
    x_head = head[0]
    y_head = head[1]

    if x_head not in range(600) or y_head not in range(600):
        raise Exception

#Main Game Loop
while True:
    pygame.display.update()
    draw_snake(position_list)
    draw_food(x_food,y_food) 

    dx,dy = move_snake(position_list,dx,dy)

    #print(position_list)
    x_food,y_food,position_list = isEated(dx,dy,position_list,x_food,y_food)
    exist(position_list)
    clock.tick(10)

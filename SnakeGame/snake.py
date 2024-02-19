import pygame, sys, random
from pygame.math import Vector2
from pathlib import Path

global ABSOLUTE_PATH, GRAPHICS_PATH

ABSOLUTE_PATH = Path(__file__).parent
GRAPHICS_PATH = ABSOLUTE_PATH / Path('Graphics')


class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
        
        self.head_up = pygame.image.load(GRAPHICS_PATH / Path('head_up.png')).convert_alpha()
        self.head_down = pygame.image.load(GRAPHICS_PATH / Path('head_down.png')).convert_alpha()
        self.head_right = pygame.image.load(GRAPHICS_PATH / Path('head_right.png')).convert_alpha()
        self.head_left = pygame.image.load(GRAPHICS_PATH / Path ('head_left.png')).convert_alpha()
        
        self.tail_up = pygame.image.load(GRAPHICS_PATH / Path('tail_up.png')).convert_alpha()
        self.tail_down = pygame.image.load(GRAPHICS_PATH / Path('tail_down.png')).convert_alpha()
        self.tail_right = pygame.image.load(GRAPHICS_PATH / Path('tail_right.png')).convert_alpha()
        self.tail_left = pygame.image.load(GRAPHICS_PATH / Path('tail_left.png')).convert_alpha()
        
        self.body_vertical = pygame.image.load(GRAPHICS_PATH / Path('body_vertical.png')).convert_alpha()
        self.body_horizontal = pygame.image.load(GRAPHICS_PATH / Path('body_horizontal.png')).convert_alpha()
        
        self.body_tr = pygame.image.load(GRAPHICS_PATH / Path('body_topright.png')).convert_alpha()
        self.body_tl = pygame.image.load(GRAPHICS_PATH / Path('body_topleft.png')).convert_alpha()
        self.body_br = pygame.image.load(GRAPHICS_PATH / Path('body_bottomright.png')).convert_alpha()
        self.body_bl = pygame.image.load(GRAPHICS_PATH / Path('body_bottomleft.png')).convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound(ABSOLUTE_PATH / Path('Sound/eating-sound.mp3'))
        
    def draw_snake(self):
        for index,block in enumerate(self.body):
            #Cria o retângulo para posicionar a imagem
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            self.update_head_graphics()
            self.update_tail_graphics()
            #Coloca a imagem correta de acordo com a parte do corpo da cobra
            if index == 0: #index == 0 é a cabeça da cobra
                screen.blit(self.head,snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,snake_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,snake_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,snake_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,snake_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,snake_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,snake_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1] #Copia todos os elementos do vetor self.body menos o último
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:] #copia todos os elementos para o vetor self.body
        
    def add_block(self):
        body_copy = self.body[:]
        body_copy.insert(0,body_copy[0] + self.direction) # apenas copia todos os elementos e adiciona um novo bloco na primeira posição da cobra
        self.body = body_copy[:]
        self.crunch_sound.play()
    
    def update_head_graphics(self):
        head_direction = self.body[1] - self.body[0]
        if head_direction == Vector2(1,0) : self.head = self.head_left
        elif head_direction == Vector2(-1,0) : self.head = self.head_right
        elif head_direction == Vector2(0,1) : self.head = self.head_up
        elif head_direction == Vector2(0,-1) : self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_direction = self.body[len(self.body) - 2] - self.body[len(self.body) - 1]
        if tail_direction == Vector2(1,0) : self.tail = self.tail_left
        elif tail_direction == Vector2(-1,0) : self.tail = self.tail_right
        elif tail_direction == Vector2(0,1) : self.tail = self.tail_up
        elif tail_direction == Vector2(0,-1) : self.tail = self.tail_down
    
    def reset(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
        
class FRUIT:
    def __init__(self):
        self.create_fruit()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(255,0,0),fruit_rect)
    
    def create_fruit(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def screen_update(self):
        self.snake.move_snake()
        self.check_collisions()
        self.check_game_over()
        
    def draw_elements(self):
        self.draw_grass()
        self.draw_score()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
    
    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.create_fruit()
            self.snake.add_block()
            
    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0  <= self.snake.body[0].y < cell_number:
            self.snake.reset()
        
        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.snake.reset()
                
    def draw_grass(self):
        grass_color =(167,209,61)
        
        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col%2 == 0:
                        rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_x = cell_number * cell_size - 60
        score_y = cell_number * cell_size - 40
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6, apple_rect.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
                
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init() #Inicializa os módulos (som, gráficos, etc...) do pygame
cell_size = 40 #Tamanho de cada célula do tabuleiro
cell_number = 15 #Número de células do tabuleiro
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) # Display

clock = pygame.time.Clock() #Variável que controla a taxa de quadros do jogo
apple = pygame.image.load(GRAPHICS_PATH / Path('apple.png')).convert_alpha()
apple = pygame.transform.scale(apple,(cell_size,cell_size))
game_font = pygame.font.Font(GRAPHICS_PATH / Path('Golden.ttf'), 25)
main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#Laço principal do jogo, onde desenharemos todos os elementos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == SCREEN_UPDATE:
            main_game.screen_update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)        
    
    
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #O while rodará 60 vezes por segundo (60 fps)
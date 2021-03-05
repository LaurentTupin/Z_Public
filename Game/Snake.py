import random, math
import pygame
import tkinter as tk



class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes = False):
        pass
    
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        pass
    
    def move(self):
        pass
    
    
    
    
    
    
    
    
    def reset(self):
        pass
    
    def addcube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        # Add Tail after Tail
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail. pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail. pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail. pos[1] - 1)))
        elif dx == 0 and dy == - 1:
            self.body.append(cube((tail.pos[0], tail. pos[1] + 1)))
        # Place right the Tail
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  c.draw(surface, True)
            else:       c.draw(surface)
              
            
            
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(surface, (255,255,255), (x, 0), (x, w))
        pygame.draw.line(surface, (255,255,255), (0, y), (w, y))
        
def redrawWindow(surface):
    global width, rows, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
    
    
def randomSnack(rows, item):
    position = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x, y), position))) > 0:
            continue
        else: break
    return (x,y)
    
def message_box(subject, content):
    pass
    
def main():
    global width, rows, s, snack
    width = 500
    rows = 10
    win = pygame.display.set_mode((width, width))
    s = snake ((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color = (0,255,0))
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        # WAIT
        pygame.time.delay(50)
        clock.tick(10)
        # MOVE
        s.move()
        # IF HEAD GOT SNACK
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color = (0,255,0))
        # IF HEAD BITE BODY
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.boady[x+1:])):
                print('Score: ', len(s.body))
                message_box()
                s.reset((10, 10))
                break        
        
        redrawWindow(win)
        
    
main()






print(20 // 3)


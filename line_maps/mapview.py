#!/usr/bin/env python
'''
Make a scrollable line digagram to show static information.

JL only so atart with.

'''
import os
import pygame
from pygame.locals import *

from line_data import line_maps



line_name = line_maps.jl_name
line_colour = line_maps.jl_colour
line_stations = line_maps.jl_stations

def main():
    pygame.init()
    
    screen_x = 0
    screen_y = 0
    
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((1000, 300))
    pygame.display.set_caption(line_name)
    
    background = pygame.Surface((4000,300))
    background = background.convert()
    background.fill((255,255,255))
    
    # Generate the line.
    line_top = 50
    line_left = 50
    line_height = 20
    this_line = pygame.Rect(line_left, line_top, background.get_width()-(5*line_left), line_height)
    pygame.draw.rect(background, line_colour, this_line, 0)
    
    # Generate the stations & distribute them evenly along the line
    number_stations = len(line_stations)
    for station in range(0, number_stations):
    
        centre_x = (background.get_width()-(2*line_left))/number_stations*station + line_left
        
        if line_stations[station][1] == line_maps.STN_INTER:  # Interchange, not step free.
            circle_centre = (centre_x, line_top + line_height/2)
            pygame.draw.circle(background, (0,0,0), circle_centre, 15, 5)
            pygame.draw.circle(background, (255,255,255), circle_centre, 10, 0)
        elif line_stations[station][1] == line_maps.STN_PSTEP: # Partially step free
            circle_centre = (centre_x, line_top + line_height/2)
            pygame.draw.circle(background, (0,103,193), circle_centre, 15, 5)
            pygame.draw.circle(background, (255,255,255), circle_centre, 12, 0)
        elif line_stations[station][1] == line_maps.STN_FSTEP: # Fully step free
            circle_centre = (centre_x, line_top + line_height/2)
            pygame.draw.circle(background, (0,103,193), circle_centre, 15, 0)
        elif line_stations[station][1] == line_maps.STN_MINOR: # No interchange, not step free.
            this_rect = pygame.Rect(centre_x-(line_height/2), line_top-line_height, line_height, line_height)
            pygame.draw.rect(background, line_colour, this_rect, 0)
            
        if pygame.font:
            font = pygame.font.Font(None, 20)
            text = font.render(line_stations[station][0], 1, (0,0,0))
            textpos = text.get_rect(centerx = centre_x)
            background.blit(text, textpos)
        

        
    screen.blit(background, (screen_x, screen_y))
    pygame.display.flip()
    
    while 1:
        clock.tick(60)
        LeftButton = 0
        drag_accelerate = 2
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                if event.buttons[LeftButton]:
                    rel = event.rel
                    if (screen_x <= 50) and rel[0] > 0:
                        screen_x += drag_accelerate*rel[0]
                        
                    if (screen_x != background.get_width()-1000) and rel[0] < 0:
                        screen_x += drag_accelerate*rel[0]
            elif event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_LEFT:
                if screen_x != background.get_width()-1000: screen_x -= 10
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                if screen_x != 50: screen_x += 10
        #allsprites.update()
        
        screen.blit(background, (screen_x, screen_y))
        #allsptites.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()

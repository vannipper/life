import pygame

"""
Key:
BLUE  = (0, 0, 255) # 0
RED   = (255, 0, 0) # 1
GREEN = (0, 255, 0) # 2
PURPLE = (255, 0, 255) # 3
ORANGE = (255, 165, 0) # 4
YELLOW = (255, 255, 0) # 5
"""

class Particle:

    def __init__ (self, x, y, size, color, forces):
        self.xpos = x
        self.ypos = y
        self.xvelo = 0
        self.yvelo = 0
        self.xacc = 0
        self.yacc = 0
        self.size = size
        self.color = color
        self.forces = forces[self.convert(color)]

    def move(self, particles, resx, resy):

        min_dist = 20 # parameter
        max_dist = 100 # parameter
        friction = 10 # parameter

        # Reset accelerations to zero
        self.xacc = 0
        self.yacc = 0

        for particle in particles:

            if particle != self:

                xdist = self.xpos - particle.xpos
                ydist = self.ypos - particle.ypos
                totaldist = (xdist ** 2 + ydist ** 2) ** 0.5

                # Update acceleration if within range
                if totaldist < max_dist:
                    if min_dist < xdist:
                        self.xacc += self.forces[self.convert(particle.color)] * xdist / totaldist
                    if min_dist < ydist:
                        self.yacc += self.forces[self.convert(particle.color)] * ydist / totaldist
                
        # Update velocity
        self.xvelo += self.xacc
        self.yvelo += self.yacc

        if abs(self.xvelo) > 0:
            self.xvelo -= friction * self.xvelo / abs(self.xvelo)
        
        if abs(self.yvelo) > 0:
            self.yvelo -= friction * self.yvelo / abs(self.yvelo)

        # Update position
        self.xpos += self.xvelo 
        self.ypos += self.yvelo
        
        if self.xpos > resx:
            self.xpos -= resx

        if self.xpos < 0:
            self.xpos += resx

        if self.ypos > resy:
            self.ypos -= resy

        if self.ypos < 0:
            self.ypos += resy
    
    def draw(self, screen, resx, resy):

        # if self.xpos - self.size > 0 and self.ypos - self.size > 0:
        #     pygame.draw.circle(screen, self.color, (self.xpos + resx, self.ypos + resy), self.size)
        # 
        # elif self.xpos + self.size < resx and self.ypos + self.size < resy:
        #     pygame.draw.circle(screen, self.color, (self.xpos - resx, self.ypos - resy), self.size)
# 
        # elif self.xpos - self.size > 0 and self.ypos + self.size < resy:
        #     pygame.draw.circle(screen, self.color, (self.xpos + resx, self.ypos - resy), self.size)
# 
        # elif self.xpos + self.size < resx and self.ypos - self.size > 0:
        #     pygame.draw.circle(screen, self.color, (self.xpos - resx, self.ypos + resy), self.size)
        # 
        # elif self.xpos - self.size > 0:
        #     pygame.draw.circle(screen, self.color, (self.xpos + resx, self.ypos), self.size)
        # 
        # elif self.xpos + self.size < resx:
        #     pygame.draw.circle(screen, self.color, (self.xpos - resx, self.ypos), self.size)
        # 
        # elif self.ypos - self.size > 0:
        #     pygame.draw.circle(screen, self.color, (self.xpos, self.ypos + resy), self.size)
        # 
        # elif self.ypos + self.size < resy:
        #     pygame.draw.circle(screen, self.color, (self.xpos, self.ypos - resy), self.size)
            
        pygame.draw.circle(screen, self.color, (self.xpos, self.ypos), self.size)
    
    def convert(self, color):
        if color == (0, 0, 255):
            return 0
        
        elif color == (255, 0, 0):
            return 1
        
        elif color == (0, 255, 0):
            return 2
        
        elif color == (255, 0, 255):
            return 3
        
        elif color == (255, 165, 0):
            return 4
        
        else:
            return 5
### Time
import pygame
import datetime
import time
import calendar
import math
import sys

## Start the program
if __name__ == "__main__":
    # Stuff that needs to be defined, font and screen size
    pygame.font.init()
    screen = pygame.display.set_mode((250,300))
    # Decide middle point of clock as a tuple
    middle = (120,150)
    icon = pygame.image.load('ic_schedule_black_18dp_2x.png').convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Time")
    myfont = pygame.font.SysFont("roboto", 25)
    clock_string= [""]
    
    z = ""
    while z == "":
        
        #Getting the time and date
        dtime = datetime.datetime.now()
        month = dtime.month
        year = dtime.year
        seconds = dtime.second + 0.000001*dtime.microsecond
        minutes = int(dtime.minute)
        hours = (dtime.hour)
        cal = calendar.month(year, month)
        local_time = time.asctime( time.localtime(time.time()))

        ## Function for giving back the X or Y value to the second, minute or hour pointer
        def positionXY(deg, length, x_or_y):
            if x_or_y == 'X':
                position = middle[0] + length*math.sin(math.radians(deg))
            if x_or_y == 'Y':
                position = middle[1] - length*math.cos(math.radians(deg))
            return(position)

        # decide the x and y coordinate of the second pointer of the clock
        # seconds goes between 0 and 60. In order to get this in degrees we need to multiply it by 6.
        secDeg = seconds*6
        # Get X and Y coordinates for the second pointer, set length of pointer to 90.
        secX = positionXY(secDeg,90, "X")
        secY = positionXY(secDeg,90,"Y")

        # decide the x and y coordinate of the minutes pointer of the clock
        # seconds goes between 0 and 60. In order to get this in degrees we need to multiply it by 6.
        minDeg = minutes*6
        # Let's set the X coordinate using sinus since at min = 0 the pointer is standing straight up, ie x = 0
        minX = positionXY(minDeg,90, "X")
        minY = positionXY(minDeg,90, "Y")

        # decide the x and y coordinate of the minutes pointer of the clock
        # seconds goes between 0 and 60. In order to get this in degrees we need to multiply it by 6.
        hourDeg = hours*30
        # Let's set the X coordinate using sinus since at min = 0 the pointer is standing straight up, ie x = 0
        hourX = positionXY(hourDeg,60, "X")
        hourY = positionXY(hourDeg,60, "Y")

        # Rendering a white background
        screen.fill((255,255,255))
        # Draw a gray clock face
        pygame.draw.circle(screen, (180,180,180),middle,100)
        # Draw a black frame
        pygame.draw.circle(screen, (0,0,0),middle,100,1)
        # Draw a second black frame
        pygame.draw.circle(screen, (0,0,0),middle,105,1)

        # Draw the numbers of the clock
        for i in range(0,12):
            if i == 0:
                b = 12
            else:
                b = i
            number = myfont.render(str(b), 1, (0,100,100))
            deg = i*(360/12)
            L = 80
            x = middle[0] + L*math.sin(math.radians(deg))-6
            y = middle[1] - L*math.cos(math.radians(deg))-8
            screen.blit(number,(x,y))
            
        # Draw the seconds pointer
        pygame.draw.line(screen, (0,0,0),middle,(secX,secY), 1)
        # Draw the minutes pointer
        pygame.draw.line(screen, (0,0,0),middle,(minX,minY), 2)
        # Draw the minutes pointer
        pygame.draw.line(screen, (0,0,0),middle,(hourX,hourY), 4)
        
        #Displaying time as text on background
        label = myfont.render(local_time, 1, (0,100,100))
        screen.blit(label,(15,15))
        pygame.display.flip()
        #keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Escape will quit the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        time.sleep(0.1)
        
        
    

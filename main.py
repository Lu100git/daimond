import pygame, time, math
pygame.init()
white = (255,255,255)
SW = 640
SH = 480
window = pygame.display.set_mode((SW,SH))
x = 100
y = 50
w = 50
h = 50
angle = 0
angle2 = 3.1
difference = [640 / 2 , 100]
rect = pygame.Surface((w,h))
rect.fill((127,0,255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.event.key == pygame.K_ESCAPE:
                running = False
    angle %= 6.2
    angle += 0.006
    window.fill(0)
    pygame.draw.line(window, white, (difference[0], difference[1] - 60), (x * math.cos(angle) + difference[0],difference[1]))
    pygame.draw.line(window, white, (difference[0], difference[1] - 60), (x * math.cos(angle + 1.5) + difference[0],difference[1]))
    pygame.draw.line(window, white, (difference[0], difference[1] - 60), (x * math.cos(angle + 3.1) + difference[0],difference[1]))
    pygame.draw.line(window, white, (difference[0], difference[1] - 60), (x * math.cos(angle + 4.6) + difference[0],difference[1]))
    pygame.draw.line(window, white, (x * math.cos(angle) + difference[0], difference[1]), (x * math.cos(angle) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (x * math.cos(angle + 1.5) + difference[0], difference[1]), (x * math.cos(angle + 1.5) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (x * math.cos(angle + 3.1) + difference[0], difference[1]), (x * math.cos(angle + 3.1) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (x * math.cos(angle + 4.6) + difference[0], difference[1]), (x * math.cos(angle + 4.6) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (difference[0], difference[1] + 300), (x * math.cos(angle) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (difference[0], difference[1] + 300), (x * math.cos(angle + 1.5) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (difference[0], difference[1] + 300), (x * math.cos(angle + 3.1) + difference[0],difference[1] + 200))
    pygame.draw.line(window, white, (difference[0], difference[1] + 300), (x * math.cos(angle + 4.6) + difference[0],difference[1] + 200))
    pygame.display.update()
    time.sleep(10/1000)

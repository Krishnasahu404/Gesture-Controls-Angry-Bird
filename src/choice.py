import pygame
import subprocess
import sys


pygame.init()

screen_width = 1200
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Angry Birds")  # Set window title

# Load kiye background image
original_background_image = pygame.image.load("D:/python/PycharmProjects/ty/theAngryBirds/resources/images/red_bird.jpg")
background_image = pygame.transform.scale(original_background_image, (screen_width, screen_height))
background_rect = background_image.get_rect()

# Create clock object to control frame rate
clock = pygame.time.Clock()

# Set button dimensions and positions
button_width = 250
button_height = 70
button_padding_x = 300
button_padding_y = 150
button_radius = 20
button1_rect = pygame.Rect(button_padding_x, screen_height // 2 + button_padding_y - button_height // 2, button_width, button_height)
button2_rect = pygame.Rect(screen_width - button_width - button_padding_x, screen_height // 2 + button_padding_y - button_height // 2, button_width, button_height)

# Set "The Angry Bird" text with positon 
text_font_size = 60
font = pygame.font.Font(None, text_font_size)
text_width = 300
text_height = 60
text_rect = pygame.Rect(screen_width // 2 - text_width // 2, screen_height // 2 - button_padding_y - text_height - 40, text_width, text_height)

# Set button colors
button_color = (63, 81, 181)  # Deep Blue shade for the button
hover_color = (33, 150, 243)  # Lighter Blue shade for hover effect
text_color_run_game = (255, 255, 255)  # White text color for "Run Game 1" and "Run Game 2"
text_color_angry_bird = (255, 255, 0)  #  text color for "The Angry Bird"

def draw_rounded_button(rect, text, hover):
    color = hover_color if hover else button_color
    pygame.draw.rect(screen, color, rect, border_radius=button_radius)
    
    text_color = text_color_run_game if "Run Game" in text else text_color_angry_bird
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def draw_text(rect, text):
    text_color = text_color_angry_bird if "The Angry Bird" in text else text_color_run_game
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, rect.topleft)

def launch_game(file_path):
    subprocess.Popen(["python", file_path])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos): #hand_gas
                launch_game("D:/python/PycharmProjects/ty/theAngryBirds/src/main.py")
                running = False 
            elif button2_rect.collidepoint(event.pos):#eye_gas
                launch_game("D:/python/PycharmProjects/ty/theAngryBirds/src/eye.py")
                running = False 

    hover1 = button1_rect.collidepoint(pygame.mouse.get_pos())
    hover2 = button2_rect.collidepoint(pygame.mouse.get_pos())

    screen.blit(background_image, background_rect)

    draw_rounded_button(button1_rect, "hand_Gas", hover1)
    draw_rounded_button(button2_rect, "Eye_Gas", hover2)

    draw_text(text_rect, "The Angry Bird")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


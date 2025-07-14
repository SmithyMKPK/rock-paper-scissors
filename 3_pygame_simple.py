# Rock Paper Scissors Game
# Copilot Prompt: Create a simple Rock Paper Scissors game using Pygame. Make it interactive with buttons for each choice and display the result of each round. Always import os os.environ["DISPLAY"] = ":1"

import pygame
import random
import sys
import os
os.environ["DISPLAY"] = ":1"
# or run DISPLAY=:1 python main.py 

pygame.init()


WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors (Simple)")


choices = ["Rock", "Paper", "Scissors"]
button_rects = [
    pygame.Rect(50, 200, 80, 40),
    pygame.Rect(160, 200, 80, 40),
    pygame.Rect(270, 200, 80, 40)
]

result_text = "Choose your move!"
player_choice = ""
computer_choice = ""

def draw_buttons():
    for i, rect in enumerate(button_rects):
        pygame.draw.rect(screen, GRAY, rect)
        txt = FONT.render(choices[i], True, BLACK)
        screen.blit(txt, (rect.x + 10, rect.y + 5))

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

running = True
while running:
    screen.fill(WHITE)
    draw_buttons()

    # Display choices and result
    pc_txt = FONT.render(f"Player: {player_choice}", True, BLACK)
    cc_txt = FONT.render(f"Computer: {computer_choice}", True, BLACK)
    res_txt = FONT.render(result_text, True, BLACK)
    screen.blit(pc_txt, (50, 50))
    screen.blit(cc_txt, (50, 90))
    screen.blit(res_txt, (50, 130))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(event.pos):
                    player_choice = choices[i]
                    computer_choice = random.choice(choices)
                    result_text = get_winner(player_choice, computer_choice)

    pygame.display.flip()

pygame.quit()
sys.exit()

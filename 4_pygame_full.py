#make a rock paper sissor game with scores as a pygame
# Copilot Prompt: Create a simple copy of Retro Bowl, where if you're on offense, you will be able to play as the Quarterback and throw the ball or choose to hand it off. Always import os os.environ["DISPLAY"] = ":1"

import pygame
import random
import sys
import os
os.environ["DISPLAY"] = ":1"

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Retro Bowl: Offense Demo")
FONT = pygame.font.Font(None, 36)
BIG_FONT = pygame.font.Font(None, 60)

# Game states
STATE_CHOOSE = 0
STATE_THROW = 1
STATE_HANDOFF = 2
STATE_RESULT = 3

state = STATE_CHOOSE
result_text = ""

"""
Bortnite: Simple Battle Royale-Inspired Game
Controls:
  1/2/3: Switch weapon (Pistol, Shotgun, AR)
  Q/E: Switch skin
  Arrow keys: Move player
  Space: Shoot
"""

# Weapons and skins
WEAPONS = ["Pistol", "Shotgun", "AR"]
WEAPON_COLORS = [(100,100,100), (200,100,50), (50,100,200)]
SKINS = ["Blue", "Red"]
SKIN_COLORS = [BLUE, RED]

# Player
player_pos = [WINDOW_WIDTH//2, WINDOW_HEIGHT//2]
player_radius = 25
player_skin = 0
player_weapon = 0
# Aim direction (WASD)
aim_dir = [0, -1]  # Default aim up


# Bullets
bullets = []  # Each bullet: [x, y, dx, dy, color, owner]

# Enemy
enemy_pos = [WINDOW_WIDTH//2, 100]
enemy_radius = 25
enemy_skin = 1  # Red
enemy_weapon = 2  # AR
enemy_dir = [random.choice([-1,1]), random.choice([-1,1])]
enemy_shoot_timer = 0

clock = pygame.time.Clock()
running = True

def draw_field():
    screen.fill(GREEN)
    pygame.draw.rect(screen, LIGHT_GRAY, (50, 50, WINDOW_WIDTH-100, WINDOW_HEIGHT-100), 5)


def draw_player():
    pygame.draw.circle(screen, SKIN_COLORS[player_skin], player_pos, player_radius)
    skin_txt = FONT.render(f"Skin: {SKINS[player_skin]}", True, WHITE)
    weapon_txt = FONT.render(f"Weapon: {WEAPONS[player_weapon]}", True, WHITE)
    screen.blit(skin_txt, (20, 20))
    screen.blit(weapon_txt, (20, 60))
    # Draw aim direction
    end_x = int(player_pos[0] + aim_dir[0]*40)
    end_y = int(player_pos[1] + aim_dir[1]*40)
    pygame.draw.line(screen, WHITE, player_pos, (end_x, end_y), 4)


def draw_enemy():
    pygame.draw.circle(screen, SKIN_COLORS[enemy_skin], enemy_pos, enemy_radius)
    skin_txt = FONT.render("Enemy", True, WHITE)
    screen.blit(skin_txt, (enemy_pos[0]-20, enemy_pos[1]-40))


def draw_bullets():
    for b in bullets:
        pygame.draw.circle(screen, b[4], (int(b[0]), int(b[1])), 8)


def shoot():
    # Shoots a bullet in aim direction
    dx, dy = aim_dir
    mag = max((dx**2 + dy**2)**0.5, 1)
    speed = 10
    dx = dx / mag * speed
    dy = dy / mag * speed
    color = WEAPON_COLORS[player_weapon]
    bullets.append([player_pos[0], player_pos[1], dx, dy, color, "player"])

def enemy_shoot():
    # Shoots a bullet toward player
    dx = player_pos[0] - enemy_pos[0]
    dy = player_pos[1] - enemy_pos[1]
    dist = max((dx**2 + dy**2)**0.5, 1)
    speed = 8
    dx = dx / dist * speed
    dy = dy / dist * speed
    color = RED
    bullets.append([enemy_pos[0], enemy_pos[1], dx, dy, color, "enemy"])


while running:
    clock.tick(60)
    draw_field()
    draw_player()
    draw_enemy()
    draw_bullets()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player_weapon = 0
            elif event.key == pygame.K_2:
                player_weapon = 1
            elif event.key == pygame.K_3:
                player_weapon = 2
            elif event.key == pygame.K_q:
                player_skin = (player_skin - 1) % len(SKINS)
            elif event.key == pygame.K_e:
                player_skin = (player_skin + 1) % len(SKINS)
            elif event.key == pygame.K_SPACE:
                shoot()
            # WASD aiming
            elif event.key == pygame.K_w:
                aim_dir = [aim_dir[0], -1]
            elif event.key == pygame.K_s:
                aim_dir = [aim_dir[0], 1]
            elif event.key == pygame.K_a:
                aim_dir = [-1, aim_dir[1]]
            elif event.key == pygame.K_d:
                aim_dir = [1, aim_dir[1]]

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Enemy AI: move randomly, bounce off walls
    enemy_pos[0] += enemy_dir[0] * 3
    enemy_pos[1] += enemy_dir[1] * 3
    if enemy_pos[0] < 50+enemy_radius or enemy_pos[0] > WINDOW_WIDTH-50-enemy_radius:
        enemy_dir[0] *= -1
    if enemy_pos[1] < 50+enemy_radius or enemy_pos[1] > WINDOW_HEIGHT-50-enemy_radius:
        enemy_dir[1] *= -1
    # Randomly change direction
    if random.random() < 0.01:
        enemy_dir = [random.choice([-1,1]), random.choice([-1,1])]

    # Enemy shoots at intervals
    enemy_shoot_timer += 1
    if enemy_shoot_timer > 60:
        enemy_shoot()
        enemy_shoot_timer = 0

    # Move bullets
    for b in bullets:
        b[0] += b[2]
        b[1] += b[3]
    bullets[:] = [b for b in bullets if 0 < b[0] < WINDOW_WIDTH and 0 < b[1] < WINDOW_HEIGHT]

    pygame.display.flip()

pygame.quit()
sys.exit()

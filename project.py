import pygame
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Changing Mandala")

clock = pygame.time.Clock()

# Load WAV music
pygame.mixer.init()
pygame.mixer.music.load("assets/664621__cigaro30__meditation-track-morning.wav")
pygame.mixer.music.play(-1)  # loop forever


def draw_mandala(surface, center, base_radius, color_shift):
    cx, cy = center

    for layer in range(6):
        radius = base_radius - layer * 25

        for i in range(36):
            angle = math.radians(i * 10 + layer * 5)

            x = cx + math.cos(angle) * radius
            y = cy + math.sin(angle) * radius

            color = (
                (color_shift + i * 6 + layer * 20) % 255,
                (color_shift + layer * 40) % 255,
                (255 - color_shift + i * 3) % 255
            )

            size = 10

            pygame.draw.polygon(surface, color, [
                (x, y - size),      # top
                (x + size, y),      # right
                (x, y + size),      # bottom
                (x - size, y)       # left
            ])

            

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Convert movement into color shift
    color_shift = (mouse_x + mouse_y) // 2

    # Draw mandala in center
    draw_mandala(screen, (WIDTH // 2, HEIGHT // 2), 250, color_shift)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
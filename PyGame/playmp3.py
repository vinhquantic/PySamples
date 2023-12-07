# Install pygame
# pip install pygame
#

import pygame

# Initialize pygame
pygame.init()

# Load the MP3 file
pygame.mixer.music.load("taratata-6264.mp3")

# Play the MP3 file
pygame.mixer.music.play()

# Wait for the MP3 to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Quit pygame
pygame.quit()

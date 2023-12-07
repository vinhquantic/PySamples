import moviepy
from moviepy.editor import *
import pygame

clip = VideoFileClip('football.mp4')
clip.preview()

pygame.quit()
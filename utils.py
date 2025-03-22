import pygame

def load_sprite_strip(filename, frame_width, frame_height, num_frames):
    """
    Load a sprite strip and split it into individual frames.
    """
    sprite_strip = pygame.image.load(filename).convert_alpha()
    frames = []
    for i in range(num_frames):
        frame = sprite_strip.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

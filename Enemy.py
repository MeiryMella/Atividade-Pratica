from Code.Const import ENTITY_SPEED
from Code.Entity import Entity
from Code.Player import Player


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprite_strip, entity_list):
        super().__init__(name, position)
        self.sprite_strip = sprite_strip  # List of images for the animation
        self.current_frame = 0  # Current frame of the animation
        self.animation_delay = 10  # Controls animation speed
        self.attack_delay = 60  # Delay between attacks
        self.attack_timer = self.attack_delay
        self.is_attacking = False  # Whether the zombie is currently attacking
        self.entity_list = entity_list  # Reference to entity_list for collision detection

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def update_animation(self):
        self.animation_delay -= 1
        if self.animation_delay == 0:
            self.animation_delay = 10  # Reset the delay
            self.current_frame = (self.current_frame + 1) % len(self.sprite_strip)
            self.surf = self.sprite_strip[self.current_frame]  # Update the current frame

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_delay
            for entity in self.entity_list:
                if isinstance(entity, Player) and self.rect.colliderect(entity.rect):
                    entity.health -= self.damage  # Deal damage to the player
                    print(f"{self.name} attacked {entity.name} for {self.damage} damage!")

    def update(self):
        self.move()
        self.update_animation()
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer == 0:
                self.is_attacking = False

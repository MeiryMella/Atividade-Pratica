from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player
from Code.utils import load_sprite_strip  # Import the helper function

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):  # level2bg images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Zombie1':
                # Load the zombie sprite strip
                zombie_sprite_strip = load_sprite_strip('asset/zombie_strip.png', frame_width=64, frame_height=64, num_frames=8)
                return Enemy('Zombie1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), zombie_sprite_strip)
            case 'Zombie2':
                # Load the zombie sprite strip
                zombie_sprite_strip = load_sprite_strip('asset/zombie_strip.png', frame_width=64, frame_height=64, num_frames=8)
                return Enemy('Zombie2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), zombie_sprite_strip)




